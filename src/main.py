import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 150
from track import track_x, track_y
from track_incline import angle_from_vertical
from normal_force import normal_force
from wheel_torque import wheel_torque


fig, ax = plt.subplots(3, 1, sharex=True)


# Plot de baan
ax[0].plot(track_x, track_y)
ax[0].set_ylabel("Hoogte (m)")
ax[0].set_title("Baan")

# # Plot de baan hoek vanaf verticaal
# ax[1].plot(track_x, angle_from_vertical, color="red")
# ax[1].set_ylabel("Baan helling ($\\theta$)")

# Plot de normaal kracht
ax[1].plot(track_x, normal_force, color="green")
ax[1].set_ylabel("Normaal kracht (N)")

# Plot het maximale wielkoppel
ax[2].plot(track_x, wheel_torque, color="orange")
ax[2].set_ylabel("Wiel Koppel (Nm)")


ax[-1].set_xlabel("Afstand (m)")
plt.show()
