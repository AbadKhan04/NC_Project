import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0  # Length of the rod
T = 1.0  # Total time
alpha = 0.01  # Thermal diffusivity
N = 100  # Number of spatial grid points
M = 1000  # Number of time steps
dx = L / (N - 1)
dt = T / M

# Initial condition
u = np.zeros(N)
u[int(0.4 * N):int(0.6 * N)] = 100.0  # Initial temperature distribution

# Finite difference method
for n in range(M):
    u[1:-1] += alpha * dt / dx**2 * (u[:-2] - 2 * u[1:-1] + u[2:])

# Plotting
x = np.linspace(0, L, N)
plt.plot(x, u)
plt.xlabel('Position')
plt.ylabel('Temperature')
plt.title('Temperature Distribution in a Metal Rod')
plt.grid(True)
plt.show()
