import numpy as np

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

