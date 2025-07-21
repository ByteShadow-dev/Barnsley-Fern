import numpy as np
import matplotlib.pyplot as plt
import random

plt.rcParams['toolbar'] = 'None'

# Functions 
def f1(arr):
    matrix = np.array([[0, 0], [0, 0.16]])
    return np.dot(matrix, arr)

def f2(arr):
    matrix = np.array([[0.85, 0.04], [-0.04, 0.85]])
    matrix_add = np.array([[0], [1.6]])
    return np.dot(matrix, arr) + matrix_add

def f3(arr):
    matrix = np.array([[0.2, -0.26], [0.23, 0.22]])
    matrix_add = np.array([[0], [1.6]])
    return np.dot(matrix, arr) + matrix_add

def f4(arr):
    matrix = np.array([[-0.15, 0.28], [0.26, 0.24]])
    matrix_add = np.array([[0], [0.44]])
    return np.dot(matrix, arr) + matrix_add

# Setup plot
fig, ax = plt.subplots(facecolor='black')
ax.set_facecolor('black')
ax.set_xlim(-5, 5)
ax.set_ylim(0, 10)
ax.axis('off')

# Pre-create a Line2D object with empty data
line, = ax.plot([], [], linestyle='', marker='o', markersize=0.5, 
                markerfacecolor='red', markeredgecolor='green')

# Data storage
x_data = []
y_data = []

# Starting point
MATRIX = np.array([[1], [1]])

# Main loop
for count in range(100000):  # increase this if you want more points
    # Add new point
    x_data.append(MATRIX[0, 0])
    y_data.append(MATRIX[1, 0])

    val = 5
    if(count%val==0):
        line.set_data(x_data, y_data)
        plt.pause(0.001)

    # Transform point
    chance = random.randint(1, 100)
    if chance <= 85:
        MATRIX = f2(MATRIX)
    elif chance <= 92:
        MATRIX = f3(MATRIX)
    elif chance <= 99:
        MATRIX = f4(MATRIX)
    else:
        MATRIX = f1(MATRIX)

# Final update for any remaining points
line.set_data(x_data, y_data)
plt.show()

