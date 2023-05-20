import numpy as np
from CoordinateSystems import ChangeCoordinateSystem

def PinHole(f, cv, cx, cy, cz, p3d):

    # Find the rotation matrix for the change pf coordinates
    rotation_matrix = np.column_stack((cx, cy, cz))

    # Change coordinate system
    new_p3d = ChangeCoordinateSystem(p3d, rotation_matrix, cv)

    # Compute the projections
    _, points_num = new_p3d.shape()
    p2d = []
    depth = []
    for i in range(points_num):
        p2d.append((f*new_p3d[i][0])/new_p3d[i][2], (f*new_p3d[i][1])/new_p3d[i][2])
        depth.append(new_p3d[i][2])

    return p2d, depth

def CameraLookingAt(f, cv, cK, cup, p3d):

    # cz computation
    CK = cK - cv
    CKnorm = np.linalg.norm(CK)
    cz = CK/CKnorm

    # cy computation
    dot_product = np.dot(cup, cz)
    cz_norm_squared = np.linalg.norm(cz) ** 2
    projection = (dot_product / cz_norm_squared) * cz
    t = cup - projection
    cy = t / np.linalg.norm(t)

    # cx computation
    cx = np.outer(cy, cz)

    p2d, depth = PinHole(f, cv, cx, cy, cz, p3d)

    return p2d, depth