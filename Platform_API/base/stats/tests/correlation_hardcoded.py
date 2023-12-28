import numpy as np
from scipy.stats import pearsonr, t


def correlation_hardcoded(x, y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    diff_x = [x_i - mean_x for x_i in x]
    diff_y = [y_i - mean_y for y_i in y]

    sum_prod = np.sum(np.array(diff_x) * np.array(diff_y))

    sum_sq_x = np.sum(np.array(diff_x) ** 2)
    sum_sq_y = np.sum(np.array(diff_y) ** 2)

    denominator = np.sqrt(sum_sq_x * sum_sq_y)

    pearson_corr = sum_prod / denominator

    n = len(x)
    se = np.sqrt((1 - pearson_corr ** 2) / (n - 2))

    # Calculate the t-value
    t_value = pearson_corr / se

    # Calculate the degrees of freedom
    df = n - 2

    # Calculate the p-value
    p_value = 2 * (1 - t.cdf(np.abs(t_value), df))

    return pearson_corr, p_value


def pearson_scipy(x, y):
    pearson_corr, _ = pearsonr(x, y)
    return pearson_corr,_
