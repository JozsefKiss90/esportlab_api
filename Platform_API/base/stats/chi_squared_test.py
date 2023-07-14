import numpy as np
from scipy.stats import chisquare

# Observed frequencies
observed = np.array([30, 45, 25, 20])

# Expected frequencies (null hypothesis)
expected = np.array([25, 40, 30, 25])

# Perform chi-square test
chi2, p_value = chisquare(observed, expected)

print("Chi-square statistic:", chi2)
print("p-value:", p_value)
