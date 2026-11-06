import numpy as np
import matplotlib.pyplot as plt

# Bar positions and heights
x = np.arange(5)
y = np.arange(4)
xpos, ypos = np.meshgrid(x, y)
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = np.zeros_like(xpos)

dx = dy = 0.6
dz = np.random.default_rng(0).integers(1, 10, size=xpos.size)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(projection="3d")
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color="steelblue", shade=True)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Value")
ax.set_title("Simple 3D Bar Chart")

plt.show()