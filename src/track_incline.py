import numpy as np
from track import track_x, track_y

dy = np.diff(track_y)
dx = np.diff(track_x)
dy_dx = np.append(dy / dx, 0)
angle_from_vertical = 0.5 * np.pi - np.arctan2(dy_dx, 1)
