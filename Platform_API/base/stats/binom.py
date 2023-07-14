import numpy as np
import matplotlib.pyplot as plt

n = 10  # Number of trials
p = 0.5  # Probability of success

num_samples = 1000  # Number of samples to simulate
samples = np.random.binomial(n, p, size=num_samples)

plt.hist(samples, bins=np.arange(n + 2) - 0.5, density=True, alpha=0.7)
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title('Binomial Distribution (n=10, p=0.5)')
plt.show()
