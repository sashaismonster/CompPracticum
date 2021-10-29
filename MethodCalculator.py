import math

class MethodCalculator:

    def __init__(self,
                 method,
                 equation):
        self.algorithm = method
        self.equation = equation

        self.x_res = [self.equation.x_0]
        self.y_res = [self.equation.y_0]
        self.y_method = [self.equation.y_0]
        self.lte = [0.0]

    def reset(self, n):
        self.x_res = [self.equation.x_0] * n
        self.y_res = [self.equation.y_exact(self.equation.x_0)] * n
        self.y_method = [self.y_res[0]] * n
        self.lte = [0.0] * n

    def build(self, step, n):
        self.reset(n + 1)

        for i in range(n):
            self.x_res[i + 1] = self.x_res[i] + step

            self.y_res[i + 1] = self.equation.y_exact(self.x_res[i + 1])

            self.y_method[i + 1] = self.algorithm.method(self.algorithm, self.equation, step, self.x_res[i], self.y_method[i])

            self.lte[i + 1] = math.fabs(self.algorithm.method(self.algorithm, self.equation, step, self.x_res[i], self.y_res[i]) -
                                        (self.y_res[i + 1]))

    def get_gte(self):
        return max(self.lte)
