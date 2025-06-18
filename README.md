# 🧠 CLARION-Inspired Cognitive Agent Simulation

This project implements a simple cognitive agent-based simulation inspired by the **CLARION cognitive architecture**.  
The system simulates an agent navigating a grid world to reach a goal, using a combination of **implicit decision-making**, **explicit reasoning**, and **episodic memory**.

---

## 🎯 How It Works

At each step:
1. The **agent observes its current state** in the environment.
2. An **implicit procedure suggests an action** (e.g. 'DOWN', 'RIGHT').
3. The agent checks:
   - Is the move **within the grid bounds**?
   - Is there a **memorized obstacle** at the intended position?
4. If the move is invalid:
   - The agent **memorizes the obstacle** (if applicable).
   - Chooses an alternative valid action from remaining options.
5. The agent **moves to the new position** and repeats the process until:
   - It reaches the goal.
   - A maximum number of steps is exceeded.

---

## ⚙️ Components

| Module             | Description                                              |
|:------------------|:---------------------------------------------------------|
| `Environment`      | Defines the grid, goal position, and boundary checks.     |
| `Agent`            | Handles decision-making using implicit and explicit logic.|
| `ImplicitProcedure`| Provides suggested actions based on the current state.    |
| `run_simulation.py`| Orchestrates an episode, logging each step.               |

---

## 📊 Example Run

```
Step 1
Agent at: [0, 0], Goal at: (4, 4)
Implicit Action: RIGHT
Intended Position: [1, 0]

Step 2
Agent at: [1, 0], Goal at: (4, 4)
Implicit Action: RIGHT
Intended Position: [2, 0]

...

✅ Goal reached in 8 steps!
```

---

## 🚀 Running the Simulation

### Prerequisites:
- Python 3.x

### Run:
```bash
python run_simulation.py
```

---

## 📖 Cognitive Principles Demonstrated

- **Implicit Decision-Making**: Predictive, automatic action suggestions.
- **Explicit Reasoning**: Alternative selection when implicit moves fail.
- **Episodic Memory**: Memorizing encountered obstacles to avoid loops.
- **Adaptive Planning**: Choosing valid moves dynamically based on environment state.

---
