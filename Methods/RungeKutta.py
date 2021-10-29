from Abstracts.AbstractMethod import AbstractMethod


class RungeKutta(AbstractMethod):
    def method(self, equation, step, x, y):
        k1 = equation.y_prime(x, y)
        k2 = equation.y_prime(x + step / 2, y + step * k1 / 2)
        k3 = equation.y_prime(x + step / 2, y + step * k2 / 2)
        k4 = equation.y_prime(x + step, y + step * k3)

        return y + step / 6 * (k1 + 2 * k2 + 2 * k3 + k4)

    name = "Runge-Kutta method"
