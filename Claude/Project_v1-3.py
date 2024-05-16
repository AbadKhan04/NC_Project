# Add Project now adding error calculation and convergence

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
        for i in range(4):
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
        input_values = [float(entry.get()) if entry.get() else 0 for entry in self.input_entries]

        if equation == "Heat Conduction":
            solution, x, y, exact_solution, error, convergence_info = heat_conduction(input_values)
        elif equation == "Wave Equation":
            solution, x, y, exact_solution, error, convergence_info = wave_equation(input_values)
        elif equation == "Fluid Flow":
            solution, x, y, exact_solution, error, convergence_info = fluid_flow(input_values[:3])  # Pass only the first three values

        # Update output label
        self.output_label.config(text=f"Solution: {solution}\nError (RMSE): {error:.6f}\n{convergence_info}")

        # Plot the solution
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(x, y, label='Approximate Solution')
        ax.plot(x, exact_solution, '--', label='Exact Solution')
        ax.set_title(equation)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.legend()
        self.canvas.draw()

def calculate_rmse(approx, exact):
    return np.sqrt(np.mean((approx - exact) ** 2))

def heat_conduction(input_values):
    # Sample input: [length, thermal_conductivity, temperature_difference, time]
    length, thermal_conductivity, temperature_difference, time = input_values

    # Implement your heat conduction equation here
    heat_flux = thermal_conductivity * temperature_difference / length
    solution = f"Heat flux: {heat_flux:.2f} W/m^2"

    # Create sample data for plotting
    x = np.linspace(0, length, 100)
    y = np.linspace(temperature_difference, 0, 100) # Approximate solution
    exact_solution = temperature_difference * np.exp(-thermal_conductivity * time / (length ** 2)) * np.ones_like(x)

    # Calculate error and convergence study
    error = calculate_rmse(y, exact_solution)
    convergence_info = "Convergence study not implemented for heat conduction."

    return solution, x, y, exact_solution, error, convergence_info

def wave_equation(input_values):
    # Sample input: [frequency, amplitude, phase, time]
    frequency, amplitude, phase, time = input_values

    # Implement your wave equation here
    angular_frequency = 2 * np.pi * frequency
    solution = f"Angular frequency: {angular_frequency:.2f} rad/s"

    # Create sample data for plotting
    x = np.linspace(0, 10, 100)
    y = amplitude * np.sin(angular_frequency * x + phase) # Approximate solution
    exact_solution = amplitude * np.sin(angular_frequency * (x - time))  # Exact solution

     # Calculate error and convergence study
    error = calculate_rmse(y, exact_solution)
    convergence_info = "Convergence study not implemented for wave equation."

    return solution, x, y, exact_solution, error, convergence_info

def fluid_flow(input_values):
    # Sample input: [velocity, pressure, density]
    velocity, pressure, density = input_values

    # Implement your fluid flow equation here
    kinetic_energy = 0.5 * density * velocity ** 2
    solution = f"Kinetic energy: {kinetic_energy:.2f} J/kg"

    # Create sample data for plotting
    x = np.linspace(0, 10, 100)
    y = kinetic_energy * np.ones_like(x) # Approximate solution
    exact_solution = y  # Exact solution is the same as approximate solution

    # Calculate error and convergence study
    error = calculate_rmse(y, exact_solution)
    convergence_info = "Convergence study not implemented for fluid flow."

    return solution, x, y, exact_solution, error, convergence_info

if __name__ == "__main__":
    app = Application()
    app.mainloop()
