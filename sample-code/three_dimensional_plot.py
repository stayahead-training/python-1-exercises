import numpy as np
import matplotlib.pyplot as plt

# [0, 1, 2, 3, 4, 5] (numpy array)
xticks = np.arange(5)

# [0, 1, 2, 3, 4]
yticks = np.arange(4)

# returns a tuple of matrices
# x_grid:
# [[0 1 2 3 4]
#  [0 1 2 3 4]
#  [0 1 2 3 4]
#  [0 1 2 3 4]]
# y_grid:
# [[0 0 0 0 0]
#  [1 1 1 1 1]
#  [2 2 2 2 2]
#  [3 3 3 3 3]]
xgrid, ygrid = np.meshgrid(xticks, yticks)

# flatten the grids into 1D arrays (see also flatten)
# x_pos = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
# y_pos = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
xpositions = xgrid.ravel()
ypositions = ygrid.ravel()

# create an array of zeros with the same shape as x_pos
zpositions = np.zeros_like(xpositions)

bar_width = 0.6
bar_depth = 0.6

# the actual (random, in this case) data
# np.random.default_rng creates a random number generator
# 0 is a seed - you get the same numbers every time
# integers produces size * numbers in the range 1 to 10
bar_height = np.random.default_rng(1).integers(1, 10, size=xgrid.size)

# create a page
figure = plt.figure(figsize=(8, 6))

# add a plot to the page
axes = figure.add_subplot(projection="3d")
axes.bar3d(
    xpositions, 
    ypositions, 
    zpositions, 
    bar_width, 
    bar_depth, 
    bar_height, 
    color="steelblue", 
    shade=True
)

axes.set_xlabel("X")
axes.set_ylabel("Y")
axes.set_zlabel("Value")
axes.set_title("Simple 3D Bar Chart")

plt.savefig('three_dimensional_plot.pdf')