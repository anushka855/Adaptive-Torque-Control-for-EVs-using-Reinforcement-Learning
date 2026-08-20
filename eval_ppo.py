import numpy as np
import matplotlib.pyplot as plt
from stable_baselines3 import PPO
from env_ev_pedal import EVAccelEnv

TEST_SCENARIO = "mixed"  # choose scenario to evaluate

env = EVAccelEnv(scenarios=[TEST_SCENARIO], Ts=0.01, ep_time=2.0)
model = PPO.load("ppo_ev_accel_fast")


obs, _ = env.reset()
Treqs, Tes, ws, accs = [], [], [], []

done = False
while not done:
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, trunc, info = env.step(action)
    Treqs.append(info["Treq"])
    Tes.append(info["Te"])
    ws.append(info["w"])
    accs.append(info["acc"])

t = np.arange(len(Treqs)) * env.Ts

plt.figure(); plt.plot(t, Treqs, label="Treq"); plt.plot(t, Tes, label="Te")
plt.xlabel("Time (s)"); plt.ylabel("Torque (Nm)"); plt.legend(); plt.title("Torque Tracking")

plt.figure(); plt.plot(t, ws); plt.xlabel("Time (s)"); plt.ylabel("Speed (rad/s)"); plt.title("Speed Curve")

plt.figure(); plt.plot(t, accs); plt.xlabel("Time (s)"); plt.ylabel("Accelerator"); plt.title("Pedal Input")

plt.show()
