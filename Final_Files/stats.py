import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

cell_population = pd.read_csv('cell-population-response.csv')

stats_results = {}
# Compute statistics for each population
for population in cell_population['population'].unique():
    cell_data = cell_population[cell_population['population'] == population]
    responders = cell_data[cell_data['response'] == 'y']['percentage']
    non_responders = cell_data[cell_data['response'] == 'n']['percentage']

    # Check for normality
    stat_resp, p_resp = stats.shapiro(responders)
    stat_nonresp, p_nonresp = stats.shapiro(non_responders)

    # If the distributions are normal
    if p_resp > 0.05 and p_nonresp > 0.05:
        # Check for equal variance
        stat_var, p_var = stats.levene(responders, non_responders)

        if p_var > 0.05:
            # T-test
            stat, p_value = stats.ttest_ind(responders, non_responders, equal_var=True)
            test_used = "T-test"
        else:
            # Welch's t-test
            stat, p_value = stats.ttest_ind(responders, non_responders, equal_var=False)
            test_used = "Welch's t-test"
    else:
        # Mann-Whitney U test
        stat, p_value = stats.mannwhitneyu(responders, non_responders, alternative='two-sided')
        test_used = "Mann-Whitney U test"

    # Store results
    stats_results[population] = {
        'Test Used': test_used,
        'Test Statistic': stat,
        'p-value': p_value,
        'mean_responders': responders.mean(),
        'mean_non_responders': non_responders.mean(),
        'median_responders': responders.median(),
        'median_non_responders': non_responders.median()
    }

stats_df = pd.DataFrame(stats_results).T
stats_df.reset_index(inplace=True)
stats_df.rename(columns={'index': 'population'}, inplace=True)

# Print statistically significant results
significant_populations = stats_df[stats_df['p-value'] < 0.05]
print("\nStatistically Significant Populations (p < 0.05):")
print(significant_populations[['population', 'p-value', 'Test Used', 'mean_responders', 'mean_non_responders']])
