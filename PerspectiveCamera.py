import numpy as np

def PinHole(f, cv, cx, cy, cz, p3d):

    _, points_num = p3d.shape()
    p2d = np.array((2, points_num))
    p2d, depth = 0
    return p2d, depth