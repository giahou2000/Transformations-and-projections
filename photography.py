from PerspectiveCamera import CameraLookingAt
from Imaging import rasterize
from render import render

def RenderObject(p3d, faces, vcolors, H, W, Rows, Columns, f, cv, cK, cup):
    # Compute 2D projection and depth of the image
    p2d, depth = CameraLookingAt(f, cv , cK , cup , p3d)

    # Rasterize the 2D image
    n2d = rasterize(p2d, Rows, Columns, H, W)

    # Paint the triangles
    I = render(n2d, faces, vcolors, depth, 'gouraud')
    return I