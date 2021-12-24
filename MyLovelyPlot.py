import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
fig, (ax1, ax2) = plt.subplots(1, 2, constrained_layout=True)

# First Plot - 3 lines
ax1.set_title('many')
ax1.set_xlabel('lines')
ax2.set_ylabel('of code')

# Second Plot - 1 line
ax2.set(title='one', xlabel='line', ylabel='of code')

# Overall title
plt.suptitle('My Lovely Plot')
plt.savefig('MyLovelyPlot.png', dpi=200)
plt.show()
