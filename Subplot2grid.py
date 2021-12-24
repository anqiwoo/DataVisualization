import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
fig = plt.figure()

ax1 = fig.add_subplot(122)
ax2 = fig.add_subplot(321)
ax3 = plt.subplot2grid((3, 2), (1, 0), rowspan=2)

plt.tight_layout()
plt.show()
plt.savefig('Subplot2grid.png')
