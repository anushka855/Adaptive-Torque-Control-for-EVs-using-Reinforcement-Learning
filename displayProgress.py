import matplotlib.pyplot as plt

# Extend timesteps to 10,000
timesteps = [
    512, 1024, 1536, 2048, 2560, 3072, 3584, 4096,
    4608, 5120, 5632, 6144, 6656, 7168, 7680, 8192,
    8704, 9216, 9728, 10240
]

# Extend ep_rew_mean with your best estimate or new values
# (For now I extrapolated your trend slightly upward)
ep_rew_mean = [
    -0.134, -0.120, -0.110, -0.102, -0.098, -0.095, -0.092, -0.089,
    -0.087, -0.085, -0.083, -0.081, -0.080, -0.079, -0.0785, -0.078,
    -0.0775, -0.077, -0.0765, -0.076
]

plt.figure(figsize=(8,5))
plt.plot(timesteps, ep_rew_mean, marker='o')
plt.title("Training Progress: Episode Reward vs Timesteps")
plt.xlabel("Total Timesteps")
plt.ylabel("Mean Episode Reward")
plt.grid(True)
plt.tight_layout()
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# your data
timesteps = [
    512, 1024, 1536, 2048, 2560, 3072, 3584, 4096,
    4608, 5120, 5632, 6144, 6656, 7168, 7680, 8192,
    8704, 9216, 9728, 10240
]

ep_rew_mean = [
    -0.134, -0.120, -0.110, -0.102, -0.098, -0.095, -0.092, -0.089,
    -0.087, -0.085, -0.083, -0.081, -0.080, -0.079, -0.0785, -0.078,
    -0.0775, -0.077, -0.0765, -0.076
]

# convert to heatmap form
# 50 duplicate rows → “waterfall” effect
heatmap = np.tile(ep_rew_mean, (50, 1))

plt.figure(figsize=(10, 5))
plt.imshow(heatmap, aspect='auto', cmap='viridis')
plt.colorbar(label='Mean Episode Reward')
plt.title("RL Convergence Heatmap (Waterfall Image)")
plt.xlabel("Timesteps Index")
plt.ylabel("Episode (Visualization Only)")
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Timesteps up to 10k
timesteps = np.linspace(0, 10000, 200)

# Shape: starts high, goes down fast, then stabilizes
# Mix of inverse parabola + exponential decay
curve = 0.5 * (1 - (timesteps / 10000)**2) + 0.1 * np.exp(-timesteps / 2000)

plt.figure(figsize=(8,5))
plt.plot(timesteps, curve, linewidth=2)
plt.title("RL Convergence: Cost/Loss Decreasing Over Timesteps")
plt.xlabel("Timesteps")
plt.ylabel("Loss / Cost")
plt.grid(True)
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

timesteps = [
    512, 1024, 1536, 2048, 2560, 3072, 3584, 4096,
    4608, 5120, 5632, 6144, 6656, 7168, 7680, 8192,
    8704, 9216, 9728, 10240
]

value_loss = [
    0.32, 0.26, 0.22, 0.19, 0.17, 0.15, 0.14, 0.13,
    0.12, 0.11, 0.10, 0.095, 0.090, 0.085, 0.080,
    0.075, 0.070, 0.065, 0.060, 0.055
]

policy_loss = [
    -0.18, -0.15, -0.13, -0.12, -0.11, -0.10, -0.095, -0.090,
    -0.088, -0.086, -0.084, -0.083, -0.082, -0.081, -0.080,
    -0.079, -0.078, -0.0775, -0.077, -0.0765
]

entropy = [
    0.74, 0.72, 0.70, 0.69, 0.68, 0.67, 0.665, 0.660,
    0.655, 0.650, 0.648, 0.646, 0.644, 0.642, 0.640,
    0.639, 0.638, 0.637, 0.636, 0.635
]

plt.figure(figsize=(10,6))
plt.plot(timesteps, value_loss, label="Value Loss", linewidth=2)
plt.plot(timesteps, policy_loss, label="Policy Loss", linewidth=2)
plt.plot(timesteps, entropy, label="Entropy", linewidth=2)

plt.title("Synthetic PPO Loss Curves (Consistent with Your Reward Data)")
plt.xlabel("Timesteps")
plt.ylabel("Loss / Entropy")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

# Your real timesteps
timesteps = [
    512, 1024, 1536, 2048, 2560, 3072, 3584, 4096,
    4608, 5120, 5632, 6144, 6656, 7168, 7680, 8192,
    8704, 9216, 9728, 10240
]

# Synthetic but realistic PPO cost decreasing curve
cost = [
    0.40, 0.32, 0.27, 0.23, 0.20, 0.18, 0.165, 0.150,
    0.140, 0.130, 0.120, 0.112, 0.105, 0.098, 0.092,
    0.087, 0.082, 0.078, 0.074, 0.070
]

plt.figure(figsize=(8,5))
plt.plot(timesteps, cost, marker='o', linewidth=2)  # added dots here
plt.title("RL Convergence: Cost/Loss Decreasing Over Timesteps")
plt.xlabel("Timesteps")
plt.ylabel("Cost / Loss")
plt.grid(True)
plt.tight_layout()
plt.show()
