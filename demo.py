import numpy as np
from RotationMatrix import rotmat
from RotationDisplacement import RotateTranslate
from CoordinateSystems import ChangeCoordinateSystem

# Extra details
theta = np.pi  # 180 degrees/pi rads clockwise rotation
u = np.array([1, 0, 0])  # Unit vector along the x-axis

# # 1) Rotaion matrix calculation example
# rotation_mat = rotmat(theta, u)
# a = np.array([1, 2, 3])
# # print(a)
# # print(np.dot(rotation_mat, a))

# 2) Rotaion/Displacement calculation example
cp = np.array([[1, 2, 3], [2, 4, 5]])
# cp = np.array([1, 2, 3])
A = np.array([1, 1, 4])
t = np.array([3, 3, 3])
cq = RotateTranslate(cp, theta, u, A, t)

# 3) Change of coordinate systems example
R = np.array([[3, 3, 0], [0, 4, 0], [1, 0, 1]])
c0 = np.array([0, 0, 0])
cq = ChangeCoordinateSystem(cp, R, c0)
print("cq:")
print(cq)