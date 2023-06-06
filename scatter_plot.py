import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(10, 0.5, 100)
y = np.random.uniform(0, 20, 100)

fig = plt.figure()
ax = plt.axes()
ax.scatter(x, y, marker='o', color='red', label='data1', alpha=0.5)
ax.scatter(x * 0.5, y * 0.5, marker='v', color='black', label='data2', alpha=0.7)
ax.legend()

plt.show()
