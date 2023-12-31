import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.diagnostic import lilliefors


class CorrelationAnalysis:
    def __init__(self, filepath1, filepath2):
        self.data1 = pd.read_excel(filepath1)
        self.data2 = pd.read_excel(filepath2)

    def check_normality(self, data):
        _, p_value = lilliefors(data)
        return p_value > 0.05  # return True if generators is normal

    def perform_correlation(self):
        if self.check_normality(self.data1) and self.check_normality(self.data2):
            corr_coef, p_value = stats.pearsonr(self.data1, self.data2)
        else:
            corr_coef, p_value = stats.spearmanr(self.data1, self.data2)
        return corr_coef, p_value

    def plot_data(self):
        plt.scatter(self.data1, self.data2)
        plt.xlabel('Data1')
        plt.ylabel('Data2')
        plt.title('Scatter plot of Data1 and Data2')
        plt.show()


if __name__ == "__main__":
    analysis = CorrelationAnalysis('../../base/files/data1.xlsx', '../../base/files/data2.xlsx')
    corr_coef, p_value = analysis.perform_correlation()
    print(f'Correlation Coefficient: {corr_coef}, P-value: {p_value}')
    analysis.plot_data()
