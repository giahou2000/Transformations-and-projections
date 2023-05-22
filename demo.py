import numpy as np
from photography import RenderObject

# Load and separate the data of the 3D image
data = np.load('h2.npy', allow_pickle=True).tolist()
data = dict(data)
p3d = np.array(data['verts3d'])
faces = np.array(data['faces'])
vcolors = np.array(data['vcolors'])
u = np.array(data['u'])
cK = np.array(data['c_lookat'])
cup = np.array(data['c_up'])
cv = np.array(data['c_org'])
t1, t2 = np.array(data['t_1']), np.array(data['t_2'])
phi = np.array(data['phi'])

# Print the first version of the image
H = 15
W = 15
Rows = 512
Columns = 512
f = 70
p3d = np.transpose(p3d)
I = RenderObject(p3d, faces, vcolors, H, W, Rows, Columns, f, cv, cK, cup)