import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, PillowWriter

fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
line, = ax.plot(x, y)

def update(frame):
    line.set_ydata(np.sin(x + 0.5*frame))
    return line,

animation = FuncAnimation(fig, update, frames=500, blit=True)

plt.show()