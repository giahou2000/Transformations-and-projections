import numpy as np
from photography import RenderObject
import matplotlib.pyplot

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
# matplotlib.pyplot.savefig('flat.png')
matplotlib.pyplot.show()