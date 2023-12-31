import numpy as np

# Set the degrees of freedom
df = 5

# Number of chi-square random variables to generate
num_samples = 100

# Generate standard normal random variables
standard_normal = np.random.standard_normal((num_samples, df))

# Square and sum the values within each distribution
squared_vars = standard_normal**2
chi_squared = np.sum(squared_vars, axis=1)
print(squared_vars)
# Plot the histogram of the chi-square distribution
import matplotlib.pyplot as plt
plt.hist(chi_squared, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Chi-square Distribution')
plt.show()
