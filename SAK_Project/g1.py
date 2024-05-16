import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import numpy as np

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
            x, y = self.calculate_zero_drag(velocity, angle, time)
        elif drag_type == "Linear Drag":
            x, y = self.calculate_linear_drag(velocity, angle, time)
        elif drag_type == "Quadratic Drag":
            x, y = self.calculate_quadratic_drag(velocity, angle, time)

        # Plot trajectory in a separate window
        self.plot_trajectory(x, y)


    def calculate_zero_drag(self, velocity, angle, time):
        # Calculate trajectory without drag
        x = velocity * np.cos(np.radians(angle)) * time
        y = velocity * np.sin(np.radians(angle)) * time - 0.5 * 9.81 * time**2
        return x, y

    def calculate_linear_drag(self, velocity, angle, time):
        # Constants
        mass = 1  # mass of the projectile (kg)
        density_air = 1.225  # density of air (kg/m^3)
        drag_coefficient = 0.1  # coefficient of drag for linear drag

        # Initial conditions
        x0 = 0
        y0 = 0
        vx0 = velocity * np.cos(np.radians(angle))
        vy0 = velocity * np.sin(np.radians(angle))

        # Arrays to store position values
        x_values = np.zeros_like(time)
        y_values = np.zeros_like(time)

        # Perform simulation
        for i, t in enumerate(time):
            # Calculate drag force
            v = np.sqrt(vx0**2 + vy0**2)
            F_drag_x = -drag_coefficient * density_air * v * vx0
            F_drag_y = -drag_coefficient * density_air * v * vy0

            # Calculate acceleration due to drag
            ax_drag = F_drag_x / mass
            ay_drag = (F_drag_y / mass) - 9.81

            # Update velocity components
            vx = vx0 + ax_drag * t
            vy = vy0 + ay_drag * t

            # Update position components
            x = x0 + vx0 * t + 0.5 * ax_drag * t**2
            y = y0 + vy0 * t + 0.5 * ay_drag * t**2

            # Store values
            x_values[i] = x
            y_values[i] = y

            # Update initial conditions for next iteration
            x0 = x
            y0 = y
            vx0 = vx
            vy0 = vy

        return x_values, y_values

    def calculate_quadratic_drag(self, velocity, angle, time):
        # Constants
        mass = 1  # mass of the projectile (kg)
        density_air = 1.225  # density of air (kg/m^3)
        drag_coefficient = 0.1  # coefficient of drag for quadratic drag
        cross_sectional_area = 0.01  # cross-sectional area of the projectile (m^2)

        # Initial conditions
        x0 = 0
        y0 = 0
        vx0 = velocity * np.cos(np.radians(angle))
        vy0 = velocity * np.sin(np.radians(angle))

        # Arrays to store position values
        x_values = np.zeros_like(time)
        y_values = np.zeros_like(time)

        # Perform simulation
        for i, t in enumerate(time):
            # Calculate drag force
            v = np.sqrt(vx0**2 + vy0**2)
            F_drag_x = -0.5 * drag_coefficient * density_air * v**2 * cross_sectional_area * np.sign(vx0)
            F_drag_y = -0.5 * drag_coefficient * density_air * v**2 * cross_sectional_area * np.sign(vy0)

            # Calculate acceleration due to drag
            ax_drag = F_drag_x / mass
            ay_drag = (F_drag_y / mass) - 9.81

            # Update velocity components
            vx = vx0 + ax_drag * t
            vy = vy0 + ay_drag * t

            # Update position components
            x = x0 + vx0 * t + 0.5 * ax_drag * t**2
            y = y0 + vy0 * t + 0.5 * ay_drag * t**2

            # Store values
            x_values[i] = x
            y_values[i] = y

            # Update initial conditions for next iteration
            x0 = x
            y0 = y
            vx0 = vx
            vy0 = vy

        return x_values, y_values


    def plot_trajectory(self, x, y):
        # Plot trajectory in a new window
        fig, ax = plt.subplots()
        ax.plot(x, y)
        ax.set_xlabel("Horizontal Distance (m)")
        ax.set_ylabel("Vertical Distance (m)")
        ax.set_title("Projectile Motion")
        plt.show()

# Create main application window
root = tk.Tk()
app = ProjectileMotionApp(root)
root.mainloop()
