from scipy import stats
import numpy as np

before = np.array([10, 12, 15, 18, 20])
after = np.array([8, 11, 13, 17, 19])

t_statistic, p_value = stats.ttest_rel(before, after)

print("t-statistic:", t_statistic)
print("p-value:", p_value)
