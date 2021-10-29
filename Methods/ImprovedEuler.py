from Abstracts.AbstractMethod import AbstractMethod


class ImprovedEuler(AbstractMethod):
    def method(self, equation, step, x, y):
        return y + step * equation.y_prime(x + step / 2,
                                           y + step / 2 * equation.y_prime(x, y))

    name = "Improved Euler method"
