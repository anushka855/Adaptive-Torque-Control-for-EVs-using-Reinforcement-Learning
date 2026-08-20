# Adaptive Torque Control for EVs using Reinforcement Learning

## Overview

This project implements a Reinforcement Learning (RL)–based torque controller for an Electric Vehicle (EV) drive system. The controller replaces a conventional PI-based control strategy with a learned policy trained using PPO in a MATLAB–Python co-simulation environment.

The objective is to reduce torque ripple, minimize speed overshoot, and enhance overall driving smoothness under varying road and load conditions.

---

## Motivation

Traditional PI controllers use fixed-gain arithmetic control to generate voltage commands for PMSM drives. Under dynamic conditions (slope, wind, varying torque demand), this can introduce torque ripple, overshoot, and reduced efficiency.

This project explores a data-driven control alternative using Reinforcement Learning to achieve adaptive and smoother torque control.

---

## System Architecture

- IPMSM-based EV drive model designed via MATLAB/Simulink  
- Python RL agent integrated via MATLAB Engine API  

The RL agent replaces the conventional PI controller by directly generating dq-axis current commands.

---

## Reinforcement Learning Formulation

### State (Observed by Agent)

- Torque demand (Treq)  
- Load (slope + wind effects)  
- Vehicle speed  

### Action (Agent Output)

- [Id, Iq] current commands  

These are converted into three-phase voltages and fed to the inverter.

### Reward Design

The reward function encourages:

- Accurate torque tracking  
- Minimal overshoot  
- Reduced torque ripple  
- Lower energy consumption  
- Stable voltage and current behavior  

---

## Training Setup

- Algorithm: PPO (Stable-Baselines3)  
- Environment: MATLAB–Simulink motor model  
- Integration: MATLAB Engine API  
- Scenarios: Uphill, downhill, variable load, wind disturbances, mixed scenrios.  

---

## Performance Evaluation

The RL controller is compared against a conventional PI controller using:

### Metrics  
- Speed overshoot (%)  
- Rise time / settling time  
- Torque ripple (%)  

### Graphical Comparisons
- Torque vs Time (raw and smoothed torque response)  
- Speed vs Time  
- Mean episode reward vs training timesteps  
- RL convergence loss vs training time  
- Convergence heatmap (policy improvement visualization)
- 
---

## Results

- Torque ripple reduced to 4–6%  
- Speed overshoot limited to 1–4%  

---

## Tech Stack

- Python  
- Stable-Baselines3  
- MATLAB / Simulink  
- MATLAB Engine API  
- Streamlit / Plotly  

---

## Future Work/ Possible Improvements

- Driver personalization via continual learning  
- Mode switching (Eco / Sport / Balanced)  
- Hardware-in-the-loop validation  
- Embedded implementation  

---

VIT Vellore, 7th sem project.  
Sep – Dec 2025
