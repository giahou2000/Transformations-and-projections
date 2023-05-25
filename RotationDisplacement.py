from RotationMatrix import rotmat
import numpy as np

def RotateTranslate(cp, theta, u, A, t):

    """
    cp: a point in 3D space
    theta: the angle of clockwise rotation
    u: vector parallel to the axis of rotation
    A: point of the axis of rotation
    t: displacement vector
    
    """

    # Calculate the rotation matrix
    R = rotmat(theta, u)
    # print("R: ")
    # print(R)
    
    # Translate the point cp to a coordinate system centered at point A
    translated_cp = cp - A
    # print("translated_cp: ")
    # print(translated_cp)

    # Rotate the translated point
    temp = []
    if len(translated_cp.shape) == 1:
        rotated_cp = np.dot(R, translated_cp)
    else:
        for i in range(len(translated_cp.shape)):
            temp.append(np.dot(R, translated_cp[i]))
        rotated_cp = np.array(temp)
    # print("rotated_cp: ")
    # print(rotated_cp)
    
    # Translate the rotated point back to the original coordinate system
    rotated_cp = rotated_cp + A
    # print("rotated_cp: ")
    # print(rotated_cp)

    cq = rotated_cp + t
    # print("cq: ")
    # print(cq)

    return cq