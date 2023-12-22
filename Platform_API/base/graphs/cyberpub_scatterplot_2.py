import numpy as np
import matplotlib.pyplot as plt

plt.style.use("dark_background")

# Adjust color, axes, and face color parameters
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light grey

for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  # bluish dark grey

np.random.seed(100)

# Adjust the means and covariance matrices
reaction_time_mean_tc = [300, 27]  # mean for teal/cyan dataset
cov_tc = [[625, 45], [45, 9]]  # covariance matrix for teal/cyan dataset to indicate a moderate positive correlation

reaction_time_mean_pink = [275, 27]  # mean for pink dataset
cov_pink = [[625, 45], [45, 9]]  # covariance matrix for pink dataset to indicate a moderate positive correlation

teal_cyan_data = np.random.multivariate_normal(reaction_time_mean_tc, cov_tc, 100).T
pink_data = np.random.multivariate_normal(reaction_time_mean_pink, cov_pink, 100).T

fig, ax = plt.subplots()

# Scatter the data points
ax.scatter(teal_cyan_data[0], teal_cyan_data[1], color='#08F7FE', marker='o', s=50, zorder=2)
ax.scatter(pink_data[0], pink_data[1], color='#FE53BB', marker='s', s=50, zorder=2)

ax.grid(color='#2A3459')

# Set the limits of the axes
ax.set_xlim([150, 450])
ax.set_ylim([18, 36])

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.legend(['Dota 2', 'CS:GO'], loc='lower right')

plt.xlabel('Reaction Time (ms)')
plt.ylabel('Age (Years)')

plt.show()
