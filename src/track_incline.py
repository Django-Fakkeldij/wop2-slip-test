import numpy as np
from track import track_x, track_y


dy_dx = np.append(np.diff(track_y) / np.diff(track_x), 0)
