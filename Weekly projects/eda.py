import scipy.stats as stats
import pandas as pd
from statsmodels.formula.api import ols
import statsmodels.api as sm
import numpy as np
from scipy.stats import chi2_contingency

# create a contingency table
observed = np.array([[10, 20, 30], [15, 25, 35]])

# perform the chi-squared test
chi2, p, dof, expected = chi2_contingency(observed)

# print the results
print('Chi-squared statistic:', chi2)
print('Degrees of freedom:', dof)
print('P-value:', p)
print('Expected frequencies:\n', expected)


# ANOVA

# Create a dataframe with the data
data = {'group': ['A', 'A', 'B', 'B', 'C', 'C'],
        'score': [10, 12, 8, 9, 11, 13]}
df = pd.DataFrame(data)

# Fit the ANOVA model
model = ols('score ~ group', data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

# Print the ANOVA table
print(anova_table)

# ANOVA

# Load data into a DataFrame
df = pd.read_csv('data.csv')

# Perform ANOVA test
f_statistic, p_value = stats.f_oneway(df['group1'], df['group2'], df['group3'])

# Print results
print("F-statistic:", f_statistic)
print("p-value:", p_value)
