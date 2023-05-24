import numpy as np

def rasterize(p2d, Rows, Columns, H, W):
    """
    p2d: the coordinates of the points of the camera system
    Rows: height for the final image
    Columns: width for the final image
    H: dimension of the camera canvas in inches
    W: dimension of the camera canvas in inches
    
    """
    # Create an empty image
    n2d = []

    # Calculate scaling factors
    scale_x = Rows / W
    scale_y = Columns / H

    for point in p2d:
        x = round(point[0] * scale_x + Rows/2)
        y = round(point[1] * scale_y + Columns/2)
        # Set pixel value to 255 at the computed coordinates
        n2d.append([x, y])
    n2d = np.array(n2d)
    
    return n2d