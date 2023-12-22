import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from statsmodels.stats.power import TTestIndPower
from statsmodels.stats.weightstats import DescrStatsW

class ReactionTimeAnalysis:
    def __init__(self, filepath):
        self.df = pd.read_excel(filepath)
        self.group_cs = self.df[self.df['game'] == 'cs']['rt']
        self.group_lol = self.df[self.df['game'] == 'lol']['rt']

    def perform_t_test(self):
        t_stat, p_val = stats.ttest_ind(self.group_cs, self.group_lol, nan_policy='omit')
        return t_stat, p_val

    def check_normality(self):
        _, p_val_cs = stats.shapiro(self.group_cs)
        _, p_val_lol = stats.shapiro(self.group_lol)
        return p_val_cs, p_val_lol

    def check_variance_homogeneity(self):
        _, p_val = stats.levene(self.group_cs, self.group_lol)
        return p_val

    def calculate_effect_size(self):
        return np.mean(self.group_cs) - np.mean(self.group_lol)

    def calculate_cohen_d(self):
        return self.calculate_effect_size() / np.sqrt(((np.std(self.group_cs)**2 + np.std(self.group_lol)**2) / 2))

    def confidence_interval(self, group):
        descr = DescrStatsW(group)
        conf_int = descr.tconfint_mean()
        return conf_int

    def power_analysis(self, effect_size, alpha=0.05, power=0.8):
        analysis = TTestIndPower()
        sample_size = analysis.solve_power(effect_size=effect_size, power=power, alpha=alpha)
        return sample_size

    def descriptive_statistics(self):
        t_stat, p_val = self.perform_t_test()
        effect_size = self.calculate_effect_size()
        cohen_d = self.calculate_cohen_d()

        results = pd.DataFrame({
            'CS': self.group_cs.describe(),
            'LoL': self.group_lol.describe()
        })

        results.loc['t-statistic', :] = [t_stat, '-']
        results.loc['p-value', :] = [p_val, '-']
        results.loc['effect size', :] = [effect_size, '-']
        results.loc['Cohen\'s d', :] = [cohen_d, '-']
        results.loc['normality (Shapiro)', :] = self.check_normality()
        results.loc['homogeneity of variance (Levene)', :] = self.check_variance_homogeneity()

        ci_cs_lower, ci_cs_upper = self.confidence_interval(self.group_cs)
        ci_lol_lower, ci_lol_upper = self.confidence_interval(self.group_lol)

        results.loc['Confidence Interval CS (lower)', :] = [ci_cs_lower, '-']
        results.loc['Confidence Interval CS (upper)', :] = [ci_cs_upper, '-']
        results.loc['Confidence Interval LoL (lower)', :] = ['-', ci_lol_lower]
        results.loc['Confidence Interval LoL (upper)', :] = ['-', ci_lol_upper]

        return results

    def plot_results_chart(self):
        # Create a bar graph for mean reaction time
        plt.figure(figsize=(10, 10))  # increase figure size
        plt.subplot(2, 2, 1)  # change subplot layout
        plt.bar(['CS', 'LoL'], [self.group_cs.mean(), self.group_lol.mean()], color=['blue', 'orange'])
        plt.title('Mean Reaction Time')
        plt.ylabel('Reaction Time')

        # Create a boxplot for reaction times
        plt.subplot(2, 2, 2)  # change subplot layout
        plt.boxplot([self.group_cs, self.group_lol], labels=['CS', 'LoL'])
        plt.title('Reaction Time Distribution')

        plt.show()

    def plot_results_table(self):
        fig = plt.figure()  # Create a figure

        # Create a table for descriptive statistics
        ax = fig.add_subplot(2, 2, 3)  # add this subplot for the table
        ax.axis('tight')
        ax.axis('off')

        descriptives = self.descriptive_statistics()
        descriptives_table = plt.table(cellText=descriptives.values,
                                       colLabels=descriptives.columns,
                                       rowLabels=descriptives.index,
                                       cellLoc='center', rowLoc='center',
                                       loc='center')
        descriptives_table.auto_set_font_size(False)
        descriptives_table.set_fontsize(10)
        descriptives_table.scale(1, 1.5)

        fig.suptitle('Descriptive Statistics')  # Use suptitle here

        plt.show()


if __name__ == "__main__":
    analysis = ReactionTimeAnalysis('../../base/files/reaction_times.xlsx')
    print(analysis.descriptive_statistics())
    analysis.plot_results_table()
