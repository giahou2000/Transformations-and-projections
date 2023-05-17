import numpy as np
from RotationMatrix import rotmat

# Rotaion matrix calculation example
theta = np.pi  # 180 degrees/pi rads clockwise rotation
u = np.array([1, 0, 0])  # Unit vector along the x-axis
rotation_mat = rotmat(theta, u)
a = np.array([1, 2, 3])
print(a)
print(np.dot(rotation_mat, a))

