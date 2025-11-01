# Benchmark Visualization Snippets

Copy the following snippets into your README.md:

## Benchmark Results

### Training Performance

**Training Reward Components — Agent-WEAVER Base**

Reward components during hexapod locomotion policy training. Total reward saturates around 0.85, with position tracking contributing the largest share. Energy penalty remains minimal, indicating efficient gait discovery.

```markdown
![Training Reward Curves](docs/figures/fig1_training_reward.png)
```

### Thermal-Aware RL

**Thermal-Aware Reward Shaping — Agent-WEAVER Policy**

Thermal-aware reward shaping keeps servo temperature below T_max (80°C) by modulating torque output. Joint tracking error increases marginally (~15%) as a tradeoff, but prevents thermal shutdown during extended operation.

```markdown
![Thermal Comparison](docs/figures/fig2_thermal_comparison.png)
```

### Sim-to-Real Transfer

**Sim-to-Real Temperature Model Validation**

Sim-to-real temperature model validation. Simulated thermal profile closely matches physical servo measurements (RMSE: 2.3°C) across varied gait patterns including walking, climbing, and recovery cycles.

```markdown
![Sim-to-Real Temperature](docs/figures/fig3_sim2real_temperature.png)
```

### Impact Reduction

**Foot Impact Reduction During Step-Down Events**

Foot impact reduction during step-down events. The RL policy learns to decelerate leg endpoints before ground contact, reducing peak impact force by 43% compared to baseline IK control.

```markdown
![Impact Reduction](docs/figures/fig4_impact_reduction.png)
```

### Trajectory Tracking

**Walking Trajectory — Reference vs Policy**

Natural hexapod walking with sinusoidal lateral sway. The policy closely tracks the reference trajectory with minimal drift across 3.77 m of forward locomotion.

```markdown
![Walking Trajectory](docs/figures/fig5_walking_trajectory.png)
```

**Running Trajectory — Reference vs Policy**

High-speed hexapod gait over 11.31 m. Policy maintains trajectory tracking despite increased ground reaction forces and dynamic instability during aerial phases.

```markdown
![Running Trajectory](docs/figures/fig6_running_trajectory.png)
```

**Vertical Climb Trajectory — Reference vs Policy**

Vertical mesh climbing using alternating tripod grip-release gait. Policy achieves 1.82 m vertical ascent with 94% grip success rate. Slip events at 0.6 m and 1.3 m are autonomously recovered.

```markdown
![Climbing Trajectory](docs/figures/fig7_climbing_trajectory.png)
```

### Reward Design

**Reward Component Weights — Agent-WEAVER Policy**

Reward component weights for walking and climbing policies. Climbing mode increases grip force and terrain adaptation rewards while reducing orientation constraints to allow body tilting.

```markdown
![Reward Weights](docs/figures/fig8_reward_weights.png)
```

### Navigation Success Rate

**Motion Tracking Success Rate — Agent-WEAVER vs Baseline**

Agent-WEAVER outperforms decoupled IK baseline across all scenarios, with the largest gains in vertical climbing (+48.3%) and flip recovery (+53.1%). NL Command Chain is exclusive to Claude-integrated pipeline.

```markdown
![Benchmark Success](docs/figures/fig9_benchmark_success.png)
```
