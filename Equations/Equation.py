from Abstracts.AbstractEquation import AbstractEquation
import numpy as np


class Equation(AbstractEquation):
    def __init__(self,
                 x_0,
                 y_0):
        super().__init__()
        self.x_0 = x_0
        self.y_0 = y_0

    def constant(self):
        return self.y_0 / (pow(self.x_0, 2) * (np.exp(-3/self.x_0)))

    def y_exact(self, x):
        return self.constant() * pow(self.x_0, 2) * (np.exp(-3/self.x_0))

    def y_prime(self, x, y):
        return (3 * y + 2 * x * y) / (x * x)

