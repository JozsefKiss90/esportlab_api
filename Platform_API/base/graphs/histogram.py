import numpy as np
import matplotlib.pyplot as plt

# Example generators
data = np.random.randn(1000)  # Random normal distribution generators

# Create histogram
plt.hist(data, bins=30)
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.show()
