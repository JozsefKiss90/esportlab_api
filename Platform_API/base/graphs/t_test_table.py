import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

plt.style.use("dark_background")

for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # very light grey

for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#494661'  # white

np.random.seed(100)

mean_tc = [6, 6]  # Mean for teal/cyan dataset
cov_tc = [[0.1, 0.05], [0.05, 0.1]]  # Covariance matrix for teal/cyan dataset with reduced spread
teal_cyan_data = np.random.multivariate_normal(mean_tc, cov_tc, 100).T

mean_pink = [7, 7]  # Mean for pink dataset
cov_pink = [[0.1, 0.05], [0.05, 0.1]]  # Covariance matrix for pink dataset with reduced spread
pink_data = np.random.multivariate_normal(mean_pink, cov_pink, 100).T

# Perform t-test
t_stat, p_value = ttest_ind(teal_cyan_data[0], pink_data[0])

# Calculate standard deviations
std_dev_tc = np.std(teal_cyan_data[0])
std_dev_pink = np.std(pink_data[0])

# Create table generators
table_data = [
    ['', 'Mean', 'Std Dev'],
    ['Team One', f'{np.mean(teal_cyan_data[0]):.2f}', f'{std_dev_tc:.2f}'],
    ['Team Two', f'{np.mean(pink_data[0]):.2f}', f'{std_dev_pink:.2f}'],
    ['t-statistic', f'{t_stat:.2f}', ''],
    ['p-value', f'{p_value:.2f}', '']
]

# Create table
fig, ax = plt.subplots()
table = ax.table(cellText=table_data, loc='center', cellLoc='center', colWidths=[0.2, 0.1, 0.1])

# Color the cells
colors = [['#212946', '#212946', '#212946'],
          ['#212946', '#212946', '#212946'],
          ['#212946', '#212946', '#212946'],
          ['#212946', '#212946', '#212946'],
          ['#212946', '#212946', '#212946']]

for i in range(len(table_data)):
    for j in range(len(table_data[0])):
        cell = table.get_celld()[i, j]
        cell.set_facecolor(colors[i][j])
        cell.set_edgecolor('#494661')

# Format table
table.set_fontsize(14)
table.scale(1.5, 1.5)

# Remove axis
ax.axis('off')

# Display table
plt.show()
