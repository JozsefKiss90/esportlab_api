import numpy as np
from scipy.stats import norm

# Function to calculate the 95% confidence interval for a given sample
def confidence_interval_95(sample):
    sample_mean = np.mean(sample)
    sample_std = np.std(sample, ddof=1)  # using Bessel's correction (ddof=1)
    sample_size = len(sample)
    z_value = norm.ppf(0.975)  # Z-value for 95% confidence interval

    margin_of_error = z_value * (sample_std / np.sqrt(sample_size))
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error

    return lower_bound, upper_bound

# Generating three different samples
np.random.seed(42)  # For reproducibility

sample1 = np.random.normal(loc=50, scale=10, size=100)  # Mean=50, Std Dev=10, Sample size=100
sample2 = np.random.normal(loc=30, scale=5, size=100)   # Mean=30, Std Dev=5, Sample size=100
sample3 = np.random.normal(loc=75, scale=15, size=100)  # Mean=75, Std Dev=15, Sample size=100

samples = [sample1, sample2, sample3]

# Calculating and printing 95% confidence intervals for the samples
for index, sample in enumerate(samples, 1):
    lower, upper = confidence_interval_95(sample)
    print(f"Sample {index} - 95% Confidence Interval: ({lower:.2f}, {upper:.2f})")

