import numpy as np
from RotationMatrix import rotmat
from RotationDisplacement import RotateTranslate

# Extra details
theta = np.pi  # 180 degrees/pi rads clockwise rotation
u = np.array([1, 0, 0])  # Unit vector along the x-axis

# Rotaion matrix calculation example
rotation_mat = rotmat(theta, u)
a = np.array([1, 2, 3])
# print(a)
# print(np.dot(rotation_mat, a))

# Rotaion/Displacement calculation example
cp = np.array([[1, 2, 3], [2, 4, 5]])
# cp = np.array([1, 2, 3])
A = np.array([1, 1, 4])
t = np.array([3, 3, 3])
cq = RotateTranslate(cp, theta, u, A, t)