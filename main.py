import sys
import tkinter
import matplotlib.pyplot as plt

import MethodAnalyzer as mA

import Equations
import Abstracts
from Abstracts.AbstractEquation import AbstractEquation
from Utility.filemanip import import_from_dir


if __name__ == '__main__':
    import_from_dir("Equations")
    equations = Abstracts.AbstractEquation.AbstractEquation.__subclasses__()

    for i in range(len(equations)):
        equations[i] = str(equations[i]).split('.').pop()
        equations[i] = equations[i][:len(str(equations[i])) - 2]

    master = tkinter.Tk()
    master.title('Computational Practicum')

    tkinter.Label(master, text="Calculating numerical method solutions").grid(row=0)
    tkinter.Label(master, text="x_0").grid(row=1)
    tkinter.Label(master, text="y_0").grid(row=2)
    tkinter.Label(master, text="N").grid(row=3)
    tkinter.Label(master, text="X").grid(row=4)
    tkinter.Label(master, text="Calculating error to N dependency").grid(row=5)
    tkinter.Label(master, text="n_0").grid(row=6)
    tkinter.Label(master, text="Max N").grid(row=7)
    tkinter.Label(master, text="").grid(row=8)

    x_0_field = tkinter.Entry(master)
    y_0_field = tkinter.Entry(master)
    n_field = tkinter.Entry(master)
    x_field = tkinter.Entry(master)
    n_0_field = tkinter.Entry(master)
    n_max_field = tkinter.Entry(master)

    current_chosen_equation = tkinter.StringVar()
    current_chosen_equation.set(equations[0])
    options = equations
    dropdown_menu = tkinter.OptionMenu(master, current_chosen_equation, *options)

    x_0_field.grid(row=1, column=1)
    y_0_field.grid(row=2, column=1)
    n_field.grid(row=3, column=1)
    x_field.grid(row=4, column=1)
    n_0_field.grid(row=6, column=1)
    n_max_field.grid(row=7, column=1)
   # dropdown_menu.grid(row=8, column=1)

    def plot_all():
        x_0 = int(x_0_field.get())
        y_0 = int(y_0_field.get())
        n = int(n_field.get())
        x = int(x_field.get())
        n_0 = int(n_0_field.get())
        n_max = int(n_max_field.get())
        equation_type = current_chosen_equation.get()

        import_from_dir("Methods")

        algorithms = Abstracts.AbstractMethod.AbstractMethod.__subclasses__()
        current_equation = getattr(sys.modules["Equations." + equation_type], equation_type)(x_0, y_0)

        method_analyzer = mA.MethodAnalyzer(algorithms, current_equation)

        plt.close()

        plot_sols = plt.subplot(221)
        plot_lte = plt.subplot(222)
        plot_gte = plt.subplot(212)

        method_analyzer.build((x - x_0) / n, n)
        method_analyzer.plot_solutions(plot_sols)
        method_analyzer.plot_lte(plot_lte)
        method_analyzer.plot_gte(n_0, n_max, x, plot_gte)

        plt.show()

    calculate_button = tkinter.Button(text="Plot", width=15, height=3)
    calculate_button.grid(row=9, column=1)
    calculate_button.config(command=plot_all)

    master.mainloop()

