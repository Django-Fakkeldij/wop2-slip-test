import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 150
from track import track_x, track_y
from track_incline import dy_dx


fig, ax = plt.subplots(2, 1, sharex=True)


# Plot de baan
ax[0].plot(track_x, track_y)
ax[0].set_ylabel("Hoogte (m)")
ax[0].set_title("Baan")


# Plot de baan helling
ax[1].plot(track_x, dy_dx, color="green")
ax[1].set_xlabel("Afstand (m)")
ax[1].set_ylabel("Baan helling ($\\Delta$ m)")

plt.show()
