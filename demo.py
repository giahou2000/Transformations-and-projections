import numpy as np
from photography import RenderObject
import matplotlib.pyplot
from RotationDisplacement import RotateTranslate

# Load and separate the data of the 3D image
data = np.load('h2.npy', allow_pickle=True)
p3d = data[()]['verts3d']
faces = data[()]['faces']
vcolors = data[()]['vcolors']
u = data[()]['u']
cK = data[()]['c_lookat']
cup = data[()]['c_up']
cv = data[()]['c_org']
t1, t2 = data[()]['t_1'], data[()]['t_2']
phi = data[()]['phi']

# Print the first version of the image
H = 15
W = 15
Rows = 512
Columns = 512
f = 70
p3d = np.transpose(p3d)
I = RenderObject(p3d, faces, vcolors, H, W, Rows, Columns, f, cv, cK, cup)
matplotlib.pyplot.imshow(I)
matplotlib.pyplot.savefig('I_1.png')
matplotlib.pyplot.show()

# Print the second version of the image
disp_p3d = p3d + t1
I = RenderObject(disp_p3d, faces, vcolors, H, W, Rows, Columns, f, cv, cK, cup)
matplotlib.pyplot.imshow(I)
matplotlib.pyplot.savefig('I_2.png')
matplotlib.pyplot.show()

# Print the third version of the image
A = np.array([0, 0, 0])
disp_p3d = RotateTranslate(disp_p3d, phi, u, A, np.array([0, 0, 0]))
I = RenderObject(disp_p3d, faces, vcolors, H, W, Rows, Columns, f, cv, cK, cup)
matplotlib.pyplot.imshow(I)
# matplotlib.pyplot.savefig('I_3.png')
matplotlib.pyplot.show()

# # Print the fourth version of the image
# disp_p3d = disp_p3d + t2
# I = RenderObject(disp_p3d, faces, vcolors, H, W, Rows, Columns, f, cv, cK, cup)
# matplotlib.pyplot.imshow(I)
# # # matplotlib.pyplot.savefig('I_4.png')
# matplotlib.pyplot.show()