import sys
import os
from components.non_action_centered_subsystem import ImplicitDeclarativeProcess, ExplicitDeclarativeProcess

# Implicit test
implicit_mem = ImplicitDeclarativeProcess()

# Dummy training data
X_train = [[2,3], [4,5], [1,1], [3,2]]
y_train = [1, 0, 0, 1]  # 1=obstacle, 0=safe
implicit_mem.train(X_train, y_train)

prediction = implicit_mem.predict([2,3])
print(f"Implicit association prediction for (2,3): {prediction}")

# Explicit test
explicit_mem = ExplicitDeclarativeProcess()
explicit_mem.add_association("(2,3)", "Obstacle")

assoc = explicit_mem.query("(2,3)")
print(f"Explicit association at (2,3): {assoc}")
