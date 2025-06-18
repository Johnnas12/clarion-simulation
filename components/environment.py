import numpy as np

ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']

class GridWorldEnvironment:
    def __init__(self, width, height, start_pos, goal_pos, obstacles=None):
        self.width = width
        self.height = height
        self.start_pos = start_pos
        self.goal_pos = goal_pos
        self.obstacles = obstacles if obstacles else []
        self.agent_pos = list(start_pos)

    def reset(self):
        self.agent_pos = list(self.start_pos)
        return self.get_state_features()

    def step(self, action):
        x, y = self.agent_pos

        if action == 'UP' and y > 0:
            y -= 1
        elif action == 'DOWN' and y < self.height - 1:
            y += 1
        elif action == 'LEFT' and x > 0:
            x -= 1
        elif action == 'RIGHT' and x < self.width - 1:
            x += 1

        if (x, y) not in self.obstacles:
            self.agent_pos = [x, y]

        done = (self.agent_pos == list(self.goal_pos))
        return self.get_state_features(), done

    def get_state_features(self):
        x, y = self.agent_pos
        gx, gy = self.goal_pos
        dist = np.linalg.norm([gx - x, gy - y])
        obstacle_up = int((x, y - 1) in self.obstacles)
        obstacle_down = int((x, y + 1) in self.obstacles)
        obstacle_left = int((x - 1, y) in self.obstacles)
        obstacle_right = int((x + 1, y) in self.obstacles)

        return [x, y, gx, gy, dist, obstacle_up, obstacle_down, obstacle_left, obstacle_right]
