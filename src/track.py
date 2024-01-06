import math
import numpy as np

# Look in assets for math behind this
# points format: (x, y)

track_start = [
    (0, 1.29),
    (7.32, 0),
]

track_curve = []

offset_x = track_start[-1][0]
offset_y = track_start[-1][1]

# Delete because no dupplicate points
track_start.pop()

# Because sin(negative n) = negative number, thus normalize to zero point
local_offset_x = 0
# Same for y
local_offset_y = 0
for x in range(-10, 80):
    local_x = math.sin((x / 180) * math.pi) * 0.4
    local_y = 0.4 - (math.cos((x / 180) * math.pi) * 0.4)
    if x == -10:
        local_offset_x = -local_x
        local_offset_y = -local_y

    track_curve.append(
        (
            local_x + offset_x + local_offset_x,
            local_y + offset_y + local_offset_y,
        )
    )

offset_x = track_curve[-1][0]
offset_y = track_curve[-1][1]
track_curve.pop()

track_end = [
    (offset_x, offset_y),
    (0.21 + offset_x, 1.19 + offset_y),
]

# Add all pieces together and interpolate to make delta x constant
track = track_start + track_curve + track_end
raw_x = np.array([i[0] for i in track])
raw_y = np.array([i[1] for i in track])
xvals = np.linspace(0, raw_x[-1], 1_000)
yvals = np.interp(xvals, raw_x, raw_y)
track_x = xvals
track_y = yvals
# track = track_curve
