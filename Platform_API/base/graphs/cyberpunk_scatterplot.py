import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("dark_background")

for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light grey

for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#212946'  # bluish dark grey

np.random.seed(100)

mean_tc = [6, 6]  # Mean for teal/cyan dataset
cov_tc = [[0.1, 0.05], [0.05, 0.1]]  # Covariance matrix for teal/cyan dataset with reduced spread
teal_cyan_data = np.random.multivariate_normal(mean_tc, cov_tc, 100).T

mean_pink = [7, 7]  # Mean for pink dataset
cov_pink = [[0.1, 0.05], [0.05, 0.1]]  # Covariance matrix for pink dataset with reduced spread
pink_data = np.random.multivariate_normal(mean_pink, cov_pink, 100).T

fig, ax = plt.subplots()

# Plot teal/cyan generators points without glow effect and unconnected
ax.scatter(teal_cyan_data[0], teal_cyan_data[1], color='#08F7FE', marker='o', s=50, zorder=2)

# Plot pink generators points without glow effect and unconnected
ax.scatter(pink_data[0], pink_data[1], color='#FE53BB', marker='s', s=50, zorder=2)

ax.grid(color='#2A3459')
ax.set_xlim([ax.get_xlim()[0] - 0.2, ax.get_xlim()[1] + 0.2])  # to not have the markers cut off
ax.set_ylim([ax.get_ylim()[0] - 0.2, ax.get_ylim()[1] + 0.2])  # to not have the markers cut off

# Remove the border of the plot
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)

# Create a legend
ax.legend(['Team One', 'Team Two'], loc='lower right')

plt.show()
