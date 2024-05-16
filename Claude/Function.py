# Firstly all functions are implement here and then in other files
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Equation Solver")
        self.geometry("800x600")
        self.equation_choice = tk.StringVar()
        self.equation_choice.set("Heat Conduction")
        self.create_widgets()

    def create_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Equation selection
        equation_frame = ttk.LabelFrame(main_frame, text="Select Equation")
        equation_frame.pack(fill="x", padx=10, pady=10)

        ttk.Radiobutton(equation_frame, text="Heat Conduction", variable=self.equation_choice, value="Heat Conduction").pack(side="left", padx=5)
        ttk.Radiobutton(equation_frame, text="Wave Equation", variable=self.equation_choice, value="Wave Equation").pack(side="left", padx=5)
        ttk.Radiobutton(equation_frame, text="Fluid Flow", variable=self.equation_choice, value="Fluid Flow").pack(side="left", padx=5)

        # Input parameters
        input_frame = ttk.LabelFrame(main_frame, text="Input Parameters")
        input_frame.pack(fill="x", padx=10, pady=10)

        self.input_labels = []
        self.input_entries = []
        for i in range(3):
            label = ttk.Label(input_frame, text=f"Parameter {i+1}:")
            label.grid(row=i, column=0, padx=5, pady=5, sticky="e")
            self.input_labels.append(label)

            entry = ttk.Entry(input_frame)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.input_entries.append(entry)

        # Solve button
        solve_button = ttk.Button(main_frame, text="Solve", command=self.solve_equation)
        solve_button.pack(pady=10)

        # Output label
        self.output_label = ttk.Label(main_frame, text="", font=("Arial", 12))
        self.output_label.pack(pady=10)

        # Plot area
        plot_frame = ttk.LabelFrame(main_frame, text="Plot")
        plot_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.figure = Figure(figsize=(6, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=plot_frame)
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

        toolbar = NavigationToolbar2Tk(self.canvas, plot_frame)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=True)

    def solve_equation(self):
        equation = self.equation_choice.get()
        input_values = [entry.get() for entry in self.input_entries]

        # Code for solving equations goes here
        output = f"Solution for {equation} with inputs {input_values} is ..."

        # Update output label
        self.output_label.config(text=output)

        # Plot the solution
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        ax.plot(x, y)
        self.canvas.draw()


    def solve_equation(self):
        equation = self.equation_choice.get()
        input_values = [float(entry.get()) for entry in self.input_entries]

        if equation == "Heat Conduction":
            solution, x, y = heat_conduction(input_values)
        elif equation == "Wave Equation":
            solution, x, y = wave_equation(input_values)
        elif equation == "Fluid Flow":
            solution, x, y = fluid_flow(input_values)

        # Update output label
        self.output_label.config(text=f"Solution: {solution}")

        # Plot the solution
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y)
        ax.set_title(equation)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        self.canvas.draw()

def heat_conduction(input_values):
    # Sample input: [length, thermal_conductivity, temperature_difference]
    length, thermal_conductivity, temperature_difference = input_values

    # Implement your heat conduction equation here
    heat_flux = thermal_conductivity * temperature_difference / length
    solution = f"Heat flux: {heat_flux:.2f} W/m^2"

    # Create sample data for plotting
    x = np.linspace(0, length, 100)
    y = np.linspace(temperature_difference, 0, 100)

    return solution, x, y

def wave_equation(input_values):
    # Sample input: [frequency, amplitude, phase]
    frequency, amplitude, phase = input_values

    # Implement your wave equation here
    angular_frequency = 2 * np.pi * frequency
    solution = f"Angular frequency: {angular_frequency:.2f} rad/s"

    # Create sample data for plotting
    x = np.linspace(0, 10, 100)
    y = amplitude * np.sin(angular_frequency * x + phase)

    return solution, x, y

def fluid_flow(input_values):
    # Sample input: [velocity, pressure, density]
    velocity, pressure, density = input_values

    # Implement your fluid flow equation here
    kinetic_energy = 0.5 * density * velocity ** 2
    solution = f"Kinetic energy: {kinetic_energy:.2f} J/kg"

    # Create sample data for plotting
    x = np.linspace(0, 10, 100)
    y = kinetic_energy * np.ones_like(x)

    return solution, x, y

if __name__ == "__main__":
    app = Application()
    app.mainloop()