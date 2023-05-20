import numpy as np

# Load and separate the data of the 3D image
data = np.load('h2.npy', allow_pickle=True).tolist()
data = dict(data)
p3d = np.array(data['verts3d'])
faces = np.array(data['faces'])
vcolors = np.array(data['vcolors'])
u = data['u']
ck = data['c_lookat']
cu = data['c_up']
cv = data['c_org']
t1, t2 = data['t_1'], data['t_2']
phi = data['phi']

