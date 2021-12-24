import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set()
fig, axes = plt.subplots(3, 1,
                         sharex=True,
                         constrained_layout=True)
data = np.linspace(0, 5, 1000)

linear, = axes[0].plot(data, 'r')
sqrt, = axes[1].plot(np.sqrt(data), 'g')
exp, = axes[2].plot(np.exp(data), 'b')

handles = [linear, sqrt, exp]
labels = ['Linear', 'Square Root', 'Exponential']

axes[0].legend(handles, labels)

plt.savefig('ShareAxis.png')
plt.show()
