from __future__ import division
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

from scipy.interpolate import PchipInterpolator as pchip
import PCA as PCA
import hyperalign as hyp

import seaborn as sns
sns.set_style("whitegrid")
sns.set_palette(palette="Set2", n_colors=3)

# this will be moved to utils.py
def is_list(x):
    if type(x[0][0])==np.ndarray:
        return True
    elif type(x[0][0])==np.int64 or type(x[0][0])==int:
        return False

# #  this will be moved to utils.py
def interp_array(arr,interp_val=10):
    x=np.arange(0, len(arr), 1)
    xx=np.arange(0, len(arr)-1, 1/interp_val)
    q=pchip(x,arr)
    return q(xx)

# #  this will be moved to utils.py
def interp_array_list(arr_list,interp_val=10):
    smoothed= [np.zeros(arr_list[0].shape) for item in arr_list]
    for idx,arr in enumerate(arr_list):
        smoothed[idx] = interp_array(arr,interp_val)
    return smoothed

def get_cube_scale(x):
    if x is list:
        x = np.vstack(x)
    x = np.square(x)
    x = np.sum(x,1)
    return np.max(x)

def animate(x):

    def update_lines(num, dataLines, lines, trailLines, tail_len=50, tail_style=':', speed=1, cam_dist=5):

        if hasattr(update_lines, 'planes'):
            for plane in update_lines.planes:
                plane.remove()

        update_lines.planes = plot_cube()
        ax.view_init(elev=10, azim=speed*num/5)
        # ax.dist=cam_dist

        for line, data, trail in zip(lines, dataLines, trailLines):
            if num<=tail_len:
                    line.set_data(data[0:num+1, 0:2].T)
                    line.set_3d_properties(data[0:num+1, 2])

            else:
                line.set_data(data[num-tail_len:num+1, 0:2].T)
                line.set_3d_properties(data[num-tail_len:num+1, 2])
            if num>=tail_len:
                if num>=tail_len*2:
                    trail.set_data(data[num-tail_len*2:1+num-tail_len, 0:2].T)
                    trail.set_3d_properties(data[num-tail_len*2:1+num-tail_len, 2])
                    trail.set_linestyle(tail_style)
                else:
                    trail.set_data(data[0:1+num-tail_len, 0:2].T)
                    trail.set_3d_properties(data[0:1+num-tail_len, 2])
                    trail.set_linestyle(tail_style)
        return lines,trailLines

    # Attaching 3D axis to the figure
    fig = plt.figure()
    ax = p3.Axes3D(fig)

    x = interp_array_list(x)

    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1], linewidth=3)[0] for dat in x]
    trail = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in x]

    # Setting the axes properties
    ax.set_xlim3d([0, 1])
    ax.set_ylim3d([0, 1])
    ax.set_zlim3d([0, 1])

    # ax.grid(False)

    ax.set_axis_off()


    def plot_cube(scale=1):
        cube = {
            "top"    : ( [[-1,1],[-1,1]], [[-1,-1],[1,1]], [[1,1],[1,1]] ),
            "bottom" : ( [[-1,1],[-1,1]], [[-1,-1],[1,1]], [[-1,-1],[-1,-1]] ),
            "left"   : ( [[-1,-1],[-1,-1]], [[-1,1],[-1,1]], [[-1,-1],[1,1]] ),
            "right"  : ( [[1,1],[1,1]], [[-1,1],[-1,1]], [[-1,-1],[1,1]] ),
            "front"  : ( [[-1,1],[-1,1]], [[-1,-1],[-1,-1]], [[-1,-1],[1,1]] ),
            "back"   : ( [[-1,1],[-1,1]], [[1,1],[1,1]], [[-1,-1],[1,1]] )
            }

        plane_list = []
        for side in cube:
            (Xs, Ys, Zs) = (
                np.asarray(cube[side][0])*scale,
                np.asarray(cube[side][1])*scale,
                np.asarray(cube[side][2])*scale
                )
            plane_list.append(ax.plot_wireframe(Xs, Ys, Zs, rstride=1, cstride=1, color='black', linewidth=3))
        return plane_list


    # Creating the Animation object
    line_ani = animation.FuncAnimation(fig, update_lines, 1000, fargs=(x, lines, trail),
                                   interval=8, blit=False, repeat=True)
    plt.show()

################################################################################
################################################################################

def Gen_RandLine(length, dims=2):
    """
    Create a line using a random walk algorithm

    length is the number of points for the line.
    dims is the number of dimensions the line has.
    """
    lineData = np.empty((dims, length))
    lineData[:, 0] = np.random.rand(dims)
    for index in range(1, length):
        # scaling the random numbers by 0.1 so
        # movement is small compared to position.
        # subtraction by 0.5 is to change the range to [-0.5, 0.5]
        # to allow a line to move backwards.
        step = ((np.random.rand(dims) - 0.5) * 0.1)
        lineData[:, index] = lineData[:, index - 1] + step

    return lineData

import scipy.io as sio

data = sio.loadmat('extras/example_data/weights.mat')
test_data=data['weights'][0][1]
test_data2=data['weights'][0][2]
test_data3=data['weights'][0][3]
data = np.array([test_data, test_data2, test_data3])

# data = [Gen_RandLine(1000,3).T for index in range(3)]
animate(data)
