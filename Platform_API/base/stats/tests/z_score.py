import numpy as np
import matplotlib.pyplot as plt

# Generate random generators with a normal distribution
np.random.seed(0)
data = np.random.normal(0, 1, 1000)

# Calculate z-scores for the generators
mean = np.mean(data)
std_dev = np.std(data)
z_scores = [(x - mean) / std_dev for x in data]

# Plot a histogram of the z-scores
plt.hist(z_scores, bins=30)
plt.xlabel('Z-score')
plt.ylabel('Frequency')
plt.title('Z-score Distribution')
plt.show()
