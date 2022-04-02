import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from random import *
from matplotlib.animation import FuncAnimation


x_values = []
y_values = []

for i in range (100):

    x_values.append(randint(0,100))
    y_values.append(randint (0,100))

    if i % 5  == 0:
        plt.xlim(0,100)
        plt.ylim(0,100)
        plt.scatter (x_values, y_values, color='black')
        plt.pause (0.001)

plt.show()

val = [0] * 50

for i in range (50):
    val[i] = randint(0,100)
    plt.xlim(0,50)
    plt.ylim(0,100)
    plt.bar (list(range(50)), val)
    plt.pause (0.0001)
plt.show()


x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 105)
ax.set_ylim(0, 12)
line, = ax.plot(0, 0)

def animation_frame(i):
    x_data.append(i* 10)
    y_data.append (i)

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, 10, 0.01), interval=18)
plt.show()