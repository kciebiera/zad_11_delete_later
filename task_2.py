"""
Program generates sample image (Figure 4) for Problem 2
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.transform import Rotation as R
import sys


def plot_matrix(transformation_matrix, ax, s='a'):
    for v, c in zip([[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1]], ['r', 'g', 'b']):
        zero = [0, 0, 0, 1]
        x, y, z, _ = zip(zero, v)
        # plt.plot(x, y, z, f'--{c}', linewidth=1)
        x, y, z, _ = zip(np.dot(transformation_matrix, zero),
                         np.dot(transformation_matrix, v))
        plt.plot(x, y, z, f'-{c}', linewidth=1)
        ax.text(x[0], y[0], z[0], s=s)


def plot_plot(case=1):
    fig = plt.figure(figsize=[10, 8])
    ax = fig.add_subplot(1, 1, 1, projection='3d')

    matrix_1 = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]]

    plot_matrix(matrix_1, ax, '0')

    matrix_2 = [
        [1, 0, 0, -2],
        [0, 1, 0, 2],
        [0, 0, 1, 1],
        [0, 0, 0, 1]]
    print(matrix_2)
    plot_matrix(matrix_2, ax, '1')

    matrix_5 = np.zeros((4, 4))
    matrix_5[:3, :3] = R.from_euler('x', -90, degrees=True).as_matrix()
    matrix_5[3, 3] = 1
    matrix_5 = np.dot(matrix_5, matrix_2)
    print(matrix_5.astype(int))
    matrix_5 = np.dot(matrix_2, matrix_5)
    # matrix_5 = np.dot(np.dot(matrix_5, matrix_2), matrix_2)
    plot_matrix(matrix_5, ax, '2')

    points = np.array([
        [1, 0, 0],
        [-1, 0, 0],
        [0, 1, 0],
        [0, -1, 0],
        [0, 0, 1],
        [0, 0, -1]]) / 2
    print(points)
    points = np.dot(matrix_5, np.hstack([points, np.ones((6, 1))]).T).T
    xs = points[:, 0]
    ys = points[:, 1]
    zs = points[:, 2]

    ax.scatter(xs, ys, zs, c='r')
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_zlim(-3, 3)

    plt.show()

# For every single one of eight cases, without looking at the source code, just by looking at
# plots, find a matrix


plot_plot()
