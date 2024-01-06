import numpy as np
from track_incline import angle_from_vertical

g = 9.81  # m/(s*s)
mass = 1.2  # kg
Fz = g * mass  # Newton

# print((angle_from_vertical - 0.5 * np.pi) / np.pi * 180)
normal_force = np.cos(angle_from_vertical - 0.5 * np.pi) * Fz
