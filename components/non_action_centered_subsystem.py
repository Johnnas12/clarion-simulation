import numpy as np
from sklearn.neural_network import MLPClassifier

# Implicit Declarative Process (Associative memory via MLP)
class ImplicitDeclarativeProcess:
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
            # If untrained, return random association category
            return np.random.randint(0, 2)
        return self.model.predict([state_features])[0]


# Explicit Declarative Process (Symbolic rules)
class ExplicitDeclarativeProcess:
    def __init__(self):
        self.associations = {}  # Dictionary to hold associations
    def add_association(self, key, value):
        self.associations[key] = value

    def query(self, key):
        return self.associations.get(key, None)
