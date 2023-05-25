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
    print("My test")
    print(translated_cp.shape)
    if len(translated_cp.shape) == 1:
        rotated_cp = np.dot(translated_cp, R)
    else:
        for i in range(translated_cp.shape[0]):
            temp.append(np.dot(translated_cp[i], R))
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