from Abstracts.AbstractMethod import AbstractMethod


class Euler(AbstractMethod):
    def method(self, equation, step, x, y):
        return y + step * equation.y_prime(x, y)

    name = "Euler method"
