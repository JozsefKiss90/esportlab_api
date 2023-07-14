import numpy as np
import matplotlib.pyplot as plt

# Example data
data = np.random.randn(1000)  # Random normal distribution data

# Create histogram
plt.hist(data, bins=30)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
