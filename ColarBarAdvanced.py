import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set()
np.random.seed(0)

data1, data2, data3, data4 = [np.random.random((8, 8)) for _ in range(4)]

fig, axes = plt.subplots(2, 2, constrained_layout=True)

# First Column Heatmaps with Same Colormap
pcm1 = axes[0, 0].pcolormesh(data1, cmap='twilight')
pcm2 = axes[1, 0].pcolormesh(data2, cmap='twilight')

# First Column Colorbar - slicing selects all rows, first column
fig.colorbar(pcm1, ax=axes[:, 0], location='top')

# Second Column Heatmaps and Colorbar
pcm3 = axes[0, 1].pcolormesh(data3, cmap='rainbow')
pcm4 = axes[1, 1].pcolormesh(data4, cmap='rainbow')
fig.colorbar(pcm3, ax=axes[:, 1], shrink=0.5)

plt.savefig('ColorBarAdvanced.png')
plt.show()
