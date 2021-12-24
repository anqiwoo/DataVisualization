import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
fig, axes = plt.subplots(2, 2)
plt.subplots_adjust(hspace=0.4, wspace=0.4)
plt.show()
plt.savefig('SubplotsAdjust.png')
