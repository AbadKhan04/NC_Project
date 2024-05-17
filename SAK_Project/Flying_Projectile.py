import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, radians, exp, log, cosh, tanh
import scipy.io

class ProjectileMotionApp:
    def __init__(self, master):
        self.master = master
        master.title("Projectile Motion Simulator")
        master.geometry("400x200")

        # Style for ttk
        style = ttk.Style()
        style.configure("TButton", foreground="blue", background="lightgreen")

        # Labels and Entries
        self.label_velocity = ttk.Label(master, text="Initial Velocity (m/s):")
        self.label_angle = ttk.Label(master, text="Launch Angle (degrees):")
        self.label_drag = ttk.Label(master, text="Type of Drag Force:")
        self.entry_velocity = ttk.Entry(master)
        self.entry_angle = ttk.Entry(master)
        self.drag_var = tk.StringVar(master)
        self.drag_var.set("Zero Drag")
        self.option_drag = ttk.OptionMenu(master, self.drag_var, "Zero Drag", "Linear Drag", "Quadratic Drag")

        # Button to run simulation
        self.button_run = ttk.Button(master, text="Run Simulation", command=self.run_simulation)

        # Grid Layout
        self.label_velocity.grid(row=0, column=0, pady=5, padx=5, sticky="e")
        self.label_angle.grid(row=1, column=0, pady=5, padx=5, sticky="e")
        self.label_drag.grid(row=2, column=0, pady=5, padx=5, sticky="e")
        self.entry_velocity.grid(row=0, column=1, pady=5, padx=5)
        self.entry_angle.grid(row=1, column=1, pady=5, padx=5)
        self.option_drag.grid(row=2, column=1, pady=5, padx=5)
        self.button_run.grid(row=3, columnspan=2, pady=10)

    def run_simulation(self):
        # Get input values
        velocity = float(self.entry_velocity.get())
        angle = float(self.entry_angle.get())
        drag_type = self.drag_var.get()

        # Perform simulation
        time = np.linspace(0, 10, 100)
        if drag_type == "Zero Drag":
            x_exact, y_exact, x_approx, y_approx = self.calculate_zero_drag(velocity, angle, time)
        elif drag_type == "Linear Drag":
            x_exact, y_exact, x_approx, y_approx = self.calculate_linear_drag(velocity, angle, time)
        elif drag_type == "Quadratic Drag":
            x_exact, y_exact, x_approx, y_approx = self.calculate_quadratic_drag(velocity, angle, time)

        # Plot trajectory in a separate window
        self.plot_trajectory(x_exact, y_exact, x_approx, y_approx)

        # save trajectories in MATLAB-compatible format
        python_results = {
            'python_exact': np.column_stack((x_exact, y_exact)),
            'python_approx': np.column_stack((x_approx, y_approx))
        }
        scipy.io.savemat('python_results.mat', python_results)

        # Reset drag type to "Zero Drag" after simulation
        self.drag_var.set("Zero Drag")

    def calculate_zero_drag(self, velocity, angle, time):
        # Calculate trajectory without drag
        x_exact = velocity * cos(radians(angle)) * time
        y_exact = velocity * sin(radians(angle)) * time - 0.5 * 9.81 * time**2
        x_approx = x_exact
        y_approx = y_exact
        return x_exact, y_exact, x_approx, y_approx

    def calculate_linear_drag(self, velocity, angle, time):
        # Constants
        mass = 1  # mass of the projectile (kg)
        k = 0.1  # linear drag coefficient

        # Initial conditions
        v0 = velocity
        theta = radians(angle)

        # Calculate exact trajectory with linear drag
        x_exact = (mass / k) * (1 - np.exp(-k * time / mass)) * v0 * np.cos(theta)
        y_exact = (mass / k) * (1 - np.exp(-k * time / mass)) * v0 * np.sin(theta) - (mass / k) * 9.81 * time

        # Calculate approximate trajectory without drag
        x_approx = v0 * cos(theta) * time
        y_approx = v0 * sin(theta) * time - 0.5 * 9.81 * time**2

        return x_exact, y_exact, x_approx, y_approx

    def calculate_quadratic_drag(self, velocity, angle, time):
        # Constants
        mass = 1  # mass of the projectile (kg)
        c = 0.1  # quadratic drag coefficient

        # Initial conditions
        v0 = velocity
        theta = radians(angle)

        # Calculate exact trajectory with quadratic drag
        x_exact = (mass / c) * np.log(np.cosh((v0 * cos(theta) + c * time) / mass))
        y_exact = (mass / c) * (np.tanh((v0 * sin(theta) + c * time) / mass) - np.tanh(v0 * sin(theta) / mass)) - (9.81 * mass / c) * time

        # Calculate approximate trajectory without drag
        x_approx = v0 * cos(theta) * time
        y_approx = v0 * sin(theta) * time - 0.5 * 9.81 * time**2

        return x_exact, y_exact, x_approx, y_approx

    def plot_trajectory(self, x_exact, y_exact, x_approx, y_approx):
        # Plot trajectory in a new window
        fig, ax = plt.subplots()
        ax.plot(x_exact, y_exact, 'b-', label='Exact Solution')
        ax.plot(x_approx, y_approx, 'r--', label='Approximate Solution (No Drag)')
        ax.set_xlabel("Horizontal Distance (m)")
        ax.set_ylabel("Vertical Distance (m)")
        ax.set_title("Projectile Motion Trajectory")
        ax.grid(True)
        ax.legend()
        plt.show()

# Create main application window
root = tk.Tk()
app = ProjectileMotionApp(root)
root.mainloop()