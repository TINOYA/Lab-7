import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создание массива значений x cо 100 точками 
x = np.linspace(-np.pi, np.pi, 100)

# Значения y равны x
y = x

# Значения z рассчитываются как tan(x)
z = np.tan(x)

# Построение трехмерного графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# График
ax.plot(x, y, z)

# Назначение меток
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()