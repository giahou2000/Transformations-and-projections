import numpy as np

def rasterize(p2d, Rows, Columns, H, W):
    """
    p2d: the coordinates of the points of the camera system
    Rows: height for the final image
    Columns: width for the final image
    H: dimension of the camera canvas in inches
    W: dimension of the camera canvas in inches
    
    """

    # Initialize p2d
    dim2 = len(p2d)
    n2d = np.ones((dim2, 2))

    # Compute rasterized image by finding the nearest pixel using floor
    for k in range(dim2):
        n2d[k][0] = np.floor((1 - (p2d[k][0] + W / 2) / W) * Rows)
        n2d[k][1] = np.floor((1 - (p2d[k][1] + H / 2) / H) * Columns)
    
    return n2d