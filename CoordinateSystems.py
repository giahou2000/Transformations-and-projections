import numpy as np

def ChangeCoordinateSystem(cp, R, c0):

    # Compute the displacement
    cp_disp = cp + c0

    # Compute the rotation
    temp = []
    if len(cp_disp.shape) == 1:
        dp = np.dot(R, cp_disp)
    else:
        for i in range(len(cp_disp.shape)):
            temp.append(np.dot(R, cp_disp[i]))
        dp = np.array(temp)

    return dp