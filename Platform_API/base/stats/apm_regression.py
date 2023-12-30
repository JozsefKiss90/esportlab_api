import pandas as pd
import statsmodels.api as sm
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.stats.outliers_influence import variance_inflation_factor

# Load the dataset
file_path = './merged_dataset.csv'
data = pd.read_csv(file_path)

# Data Cleaning: Removing the 'correctPercent' column and dropping rows with any missing values.
data_cleaned = data.drop(columns=['correctPercent', 'email']).dropna()

# Standardizing the data (excluding the dependent variable 'apm_performance')
scaler = StandardScaler()
X_scaled = scaler.fit_transform(data_cleaned.drop('apm_performance', axis=1))
y = data_cleaned['apm_performance']

# Convert the scaled features back into a DataFrame for convenience
X_scaled_df = pd.DataFrame(X_scaled, columns=data_cleaned.columns[:-1])

# Synchronizing the indices of the dependent and independent variables
y = y.reset_index(drop=True)
X_scaled_df = X_scaled_df.reset_index(drop=True)

# Adding a constant to the independent variables for the regression model.
X_with_constant = sm.add_constant(X_scaled_df)

# Fitting the regression model
model = sm.OLS(y, X_with_constant).fit()

# Checking for independence: VIF (Variance Inflation Factor)
vif_data = pd.DataFrame()
vif_data['feature'] = X_scaled_df.columns
vif_data['VIF'] = [variance_inflation_factor(X_scaled_df.values, i) for i in range(len(X_scaled_df.columns))]

# Checking for homoscedasticity: Residuals vs Fitted plot
# Fitting the regression model
model = sm.OLS(y, X_with_constant).fit()

# Storing the fitted values (the predicted values for the model)
model_fitted_y = model.fittedvalues

# Fitting the regression model
model = sm.OLS(y, X_with_constant).fit()

# Storing the fitted values (the predicted values for the model)
model_fitted_y = model.fittedvalues

# Checking for homoscedasticity: Residuals vs Fitted plot
model_residuals = model.resid
# Checking for homoscedasticity: Residuals vs Fitted plot
plt.figure(figsize=(6,4))
sns.residplot(x=model_fitted_y, y=y, lowess=True)
plt.title('Residuals vs Fitted')
plt.xlabel('Fitted values')
plt.ylabel('Residuals')
plt.show()

# Checking for normal distribution of residuals: QQ Plot
plt.figure(figsize=(6, 4))
sm.qqplot(model_residuals, line='45', fit=True, ax=plt.subplot(111))

# Displaying the regression model summary
model_summary = model.summary()
print(model_summary)
