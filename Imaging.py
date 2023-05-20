import numpy as np

def rasterize(p2d, Rows, Columns, H, W):
    """
    p2d: the coordinates of the points of the camera system
    Rows: height for the final image
    Columns: width for the final image
    H: dimension of the camera canvas in inches
    W: dimension of the camera canvas in inches
    
    """

    # Initialize Prast and arrays of normalized x and y
    _, dim2 = p2d.shape
    n2d = np.ones((2, dim2))

    # Compute rasterized image by finding the nearest pixel using floor
    for k in range(dim2):
        n2d[0, k] = np.floor((1 - (p2d[0, k] + W / 2) / W) * Rows)
        n2d[1, k] = np.floor((1 - (p2d[1, k] + H / 2) / H) * Columns)
    return n2d