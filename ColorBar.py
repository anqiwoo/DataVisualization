import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)  # Add seed to reproduce results
sns.set()

data1 = np.random.random((8, 8))
data2 = np.random.random((8, 8))

fig, axes = plt.subplots(1, 2, constrained_layout=True,
                         figsize=plt.figaspect(1/2))

pcm1 = axes[0].pcolormesh(data1, cmap='Blues')
fig.colorbar(pcm1, ax=axes[0])

pcm2 = axes[1].pcolormesh(data2, cmap='Oranges')
fig.colorbar(pcm2, ax=axes[1])

plt.savefig('ColorBar.png')
plt.show()
