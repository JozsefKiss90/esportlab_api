import numpy as np
import matplotlib.pyplot as plt

# Example data
data = np.random.normal(loc=0, scale=1, size=1000)

# Calculate quantiles
quantiles = np.quantile(data, [0.25, 0.5, 0.75])  # Specify the desired quantiles

# Plot the data and quantiles
plt.hist(data, bins=30, alpha=0.5, label='Data')
plt.axvline(x=quantiles[0], color='r', linestyle='--', label='25th percentile')
plt.axvline(x=quantiles[1], color='g', linestyle='--', label='50th percentile (median)')
plt.axvline(x=quantiles[2], color='b', linestyle='--', label='75th percentile')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Quantiles and Data Distribution')
plt.legend()
plt.show()
