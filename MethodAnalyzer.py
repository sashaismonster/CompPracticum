import MethodCalculator

class MethodAnalyzer:

    def __init__(self,
                 methods,
                 equation):

        self.calculators = []
        for method in methods:
            self.calculators.append(MethodCalculator.MethodCalculator(method, equation))
        self.equation = equation

    def build(self, step, n):
        for calculator in self.calculators:
            calculator.build(step, n)

    def build_solutions(self, x, n):
        self.build((x - self.equation.x_0) / n, n)

    def plot_solutions(self, plot_target):
        plot_target.plot(self.calculators[0].x_res, self.calculators[0].y_res, label="Exact Solution")

        for calculator in self.calculators:
            plot_target.plot(calculator.x_res, calculator.y_method, label=calculator.algorithm.name)

        plot_target.legend()

    def plot_lte(self, plot_target):
        for calculator in self.calculators:
            plot_target.plot(calculator.x_res, calculator.lte, label=calculator.algorithm.name + ' LTE')

        plot_target.legend()

    def plot_gte(self, n0, N, X, plot_gte):

        gte = []
        names = []

        for calculator in self.calculators:
            gte.append([])
            names.append(calculator.algorithm.name)

        for i in range(n0, N):
            self.build(X / i, i)

            for j in range(len(self.calculators)):
                gte[j].append(self.calculators[j].get_gte())

        for i in range(len(names)):
            plot_gte.plot(range(n0, N), gte[i], label=names[i] + " dependency of GTE on N")

        plot_gte.legend()