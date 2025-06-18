from components.action_centered_subsystem import ImplicitProceduralProcess, ExplicitProceduralProcess, ACTIONS
import numpy as np

# Initialize subsystems
implicit_proc = ImplicitProceduralProcess()
explicit_proc = ExplicitProceduralProcess()

# Add explicit rule: "if obstacle above, don't move up — move right"
explicit_proc.add_rule(lambda s: s[4] < 1 and s[5] == 1, 'RIGHT')

# Example state: [x, y, goal_x, goal_y, distance, obstacle_up, obstacle_down, obstacle_left, obstacle_right]
state = [2, 2, 5, 5, 4.2, 1, 0, 0, 0]

# Check explicit decision
action = explicit_proc.decide(state)
if action:
    print(f"Explicit decision: {action}")
else:
    action = implicit_proc.predict(state)
    print(f"Implicit decision: {action}")
