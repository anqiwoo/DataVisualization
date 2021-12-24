import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set()

ratios = {'height_ratios': [2, 1], 'width_ratios': [2, 1]}

fig, axes = plt.subplots(2, 2, constrained_layout=True, gridspec_kw=ratios)

plt.savefig('Ratios.png')
plt.show()
