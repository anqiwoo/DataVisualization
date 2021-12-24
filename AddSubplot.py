import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
fig = plt.figure()

ax1 = fig.add_subplot(122)
ax2 = fig.add_subplot(421)
ax3 = fig.add_subplot(423)
ax4 = fig.add_subplot(223)

plt.tight_layout()
plt.savefig('AddSubplot.png')
plt.show()
