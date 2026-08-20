import gymnasium as gym
import numpy as np
import matlab.engine

MODEL = "IPMSMAxleDriveEVDQ"
SIGEDIT_PATH = f"{MODEL}/Inputs"
MATLAB_STEP_TIMEOUT = 60.0  # seconds


class EVAccelEnv(gym.Env):
    metadata = {"render_modes": []}

    def __init__(self, scenarios, Ts=0.01, ep_time=2.0, action_repeat=3):
        super().__init__()
        self.scenarios = list(scenarios)
        self.Ts = float(Ts)
        self.ep_time = float(ep_time)
        self.steps = int(round(self.ep_time / self.Ts))
        self.action_repeat = int(action_repeat)

        # Normalization constants
        self.Treq_max = 300.0
        self.w_max = 800.0

        # Define action and observation spaces
        self.action_space = gym.spaces.Box(low=0.0, high=1.0, shape=(1,), dtype=np.float32)
        self.observation_space = gym.spaces.Box(low=-2.0, high=2.0, shape=(3,), dtype=np.float32)

        # Episode counter for restart logic
        self.episode_count = 0

        print("Starting MATLAB engine...")
        self._start_matlab_engine()

        self.prev_Te = 0.0
        self.prev_acc = 0.0
        self.k = 0
        self._rng = np.random.default_rng()

    # ---------------- MATLAB ENGINE CONTROL ----------------
    def _start_matlab_engine(self):
        self.eng = matlab.engine.start_matlab()
        self.eng.eval("Simulink.sdi.clear; Simulink.sdi.setAutoArchiveMode(false);", nargout=0)
        self.h = self.eng.init_ev_noedit(MODEL, self.Ts, 0.0, self.ep_time, nargout=1)

    def _restart_matlab_engine(self):
        try:
            self.eng.quit()
        except:
            pass
        print("\n[ENV] Restarting MATLAB engine to clear memory...")
        self._start_matlab_engine()

    # ---------------- Helper Functions ----------------
    def _safe_result(self, future, where="step"):
        try:
            return future.result(MATLAB_STEP_TIMEOUT)
        except Exception as e:
            raise RuntimeError(f"MATLAB call timeout or error during {where}: {e}")

    def _obs_arr(self, Treq, Te, w):
        denom = max(abs(Treq), 1e-3)
        load = (Treq - Te) / denom
        obs = np.array([Treq / self.Treq_max, load, w / self.w_max], dtype=np.float32)
        return np.nan_to_num(obs, nan=0.0, posinf=1.0, neginf=-1.0)

    def _set_scenario(self, scen_name):
        self.eng.set_param(SIGEDIT_PATH, 'ActiveScenario', scen_name, nargout=0)

    # ---------------- Gym API ----------------
    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        if seed is not None:
            self._rng = np.random.default_rng(seed)

        # Restart every 5 episodes to avoid memory overflow
        self.episode_count += 1
        if self.episode_count % 5 == 0:
            self._restart_matlab_engine()

        scen = self._rng.choice(self.scenarios).item()
        print(f"\n[ENV] Starting new episode with scenario: {scen}")
        self._set_scenario(scen)

        self.prev_Te = 0.0
        self.prev_acc = 0.0
        self.k = 0

        fut = self.eng.step_ev_noedit(self.h, 0.0, 0.0, 0.0, 0.0, nargout=1, background=True)
        out = self._safe_result(fut, "reset")
        self.h = out["h"]

        Treq = float(out.get("Treq", 0.0))
        Te = float(out.get("Te", 0.0))
        w = float(out.get("w", 0.0))

        return self._obs_arr(Treq, Te, w), {}

    def step(self, action):
        acc = float(np.clip(action[0], 0.0, 1.0))
        total_reward = 0.0
        done = False
        Treq = Te = w = 0.0

        for _ in range(self.action_repeat):
            fut = self.eng.step_ev_noedit(self.h, acc, 0.0, 0.0, 0.0, nargout=1, background=True)
            out = self._safe_result(fut, "step")
            self.h = out["h"]

            Treq = float(out.get("Treq", 0.0))
            Te = float(out.get("Te", 0.0))
            w = float(out.get("w", 0.0))

            dTe = Te - self.prev_Te
            dacc = acc - self.prev_acc
            reward = -((Te - Treq)**2 + 0.05*(dTe**2) + 0.01*(dacc**2))
            total_reward += reward

            self.prev_Te = Te
            self.prev_acc = acc
            self.k += 1
            done = self.k >= self.steps

            if done:
                break

        obs = self._obs_arr(Treq, Te, w)
        info = {"Treq": Treq, "Te": Te, "w": w, "acc": acc}
        return obs, float(total_reward), bool(done), False, info
