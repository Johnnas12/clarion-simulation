import numpy as np
from sklearn.neural_network import MLPClassifier

ACTIONS = ['UP', 'DOWN', 'LEFT', 'RIGHT']

# Implicit Procedural Process (MLP)
class ImplicitProceduralProcess:
    def __init__(self, hidden_layer_sizes=(10,), max_iter=2000, learning_rate=0.001):
        self.model = MLPClassifier(
            hidden_layer_sizes=hidden_layer_sizes,
            max_iter=max_iter,
            learning_rate_init=learning_rate
        )
        self.trained = False

    def train(self, X, y):
        self.model.fit(X, y)
        self.trained = True
    
    def predict(self, state_features):
        if not self.trained:
            # If untrained, pick random action
            return np.random.choice(ACTIONS)
        action_index = self.model.predict([state_features])[0]
        return ACTIONS[action_index]


# Explicit Procedural Process (Symbolic Rules)
class ExplicitProceduralProcess:
    def __init__(self):
        self.rules = []  # List of (condition_function, action)
    
    def add_rule(self, condition_func, action):
        self.rules.append((condition_func, action))
    
    def decide(self, state_features):
        for condition_func, action in self.rules:
            if condition_func(state_features):
                return action
        return None
