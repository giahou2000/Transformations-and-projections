from PerspectiveCamera import CameraLookingAt
from Imaging import rasterize
from render import render

def RenderObject(p3d, faces, vcolors, H, W, Rows, Columns, f, cv, cK, cup):

    """
    p3d: 3D points
    faces: the points of the triangles
    vcolors: the colors of the points
    H: dimension of the camera canvas in inches
    W: dimension of the camera canvas in inches
    Rows: height for the final image
    Columns: width for the final image
    f: distance between the camera canvas and the camera center
    cv: camera center
    cK: the point where the camera is directed
    cup: unit up vector
    
    """

    # Compute 2D projection and depth of the image
    p2d, depth = CameraLookingAt(f, cv , cK , cup , p3d)

    # Rasterize the 2D image
    n2d = rasterize(p2d, Rows, Columns, H, W)

    # Paint the triangles
    I = render(n2d, faces, vcolors, depth, 'gouraud')
    return I