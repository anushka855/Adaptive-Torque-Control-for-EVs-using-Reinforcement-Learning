from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import BaseCallback
from env_ev_pedal import EVAccelEnv

# Stable scenarios only
SCENARIOS = ["downhill", "uphill", "mixed"]

env = EVAccelEnv(scenarios=SCENARIOS, Ts=0.01, ep_time=2.0, action_repeat=3)

model = PPO(
    "MlpPolicy", env,
    learning_rate=3e-4,
    n_steps=384,
    batch_size=128,
    gamma=0.995,
    gae_lambda=0.95,
    clip_range=0.2,
    ent_coef=0.0,
    policy_kwargs=dict(net_arch=[64, 64]),
    verbose=1
)

class PrintCallback(BaseCallback):
    def _on_step(self) -> bool:
        if self.n_calls % 500 == 0:
            latest_reward = float(self.locals["rewards"])
            print(f"Step {self.n_calls} | reward {latest_reward}")
        return True

callback = PrintCallback()

print("\nStarting training for 10,000 timesteps...")
model.learn(total_timesteps=10_000, callback=callback)
model.save("ppo_ev_accel_fast")

print("\nDone. Saved model: ppo_ev_accel_fast.zip")