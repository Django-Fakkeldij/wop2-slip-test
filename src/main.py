import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["figure.dpi"] = 150
from track import track


fig, ax = plt.subplots(1, 1)

x = [i[0] for i in track]
y = [i[1] for i in track]


# Plot de data in het rechter assenstelsel
ax.plot(x, y)
ax.set_ylim([-0.1, 4])
ax.set_xlabel("Lengte (m)")
ax.set_ylabel("Hoogte (m)")
ax.set_title("Baan")

plt.show()
