from components.environment import GridWorldEnvironment

env = GridWorldEnvironment(5, 5, (0,0), (4,4), obstacles=[(0,1), (1,0)])

state = env.reset()
print(f"Initial State: {state}")

state, done = env.step('RIGHT')
print(f"After RIGHT: {state}, Done: {done}")

state, done = env.step('DOWN')
print(f"After DOWN: {state}, Done: {done}")
