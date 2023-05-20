import numpy as np

def rasterize(p2d, Rows, Columns, H, W):
    # Initialize Prast and arrays of normalized x and y
    _, dim2 = p2d.shape
    n2d = np.zeros((2, dim2))

    # Compute rasterized image by finding the nearest pixel using floor
    for k in range(dim2):
        n2d[0, k] = np.floor((1 - (p2d[0, k] + W / 2) / W) * Rows)
        n2d[1, k] = np.floor((1 - (p2d[1, k] + H / 2) / H) * Columns)
    return n2d