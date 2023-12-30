import pandas as pd

# Replace with your actual file paths
rt_path = './filtered_rt_data.csv'
handeye_path = './filtered_handeye_data.csv'
memory_path = './filtered_memory_data.csv'
simon_path = './filtered_simon_data.csv'
apm_path = './filtered_apm_data.csv'

# Load each dataset
rt_data = pd.read_csv(rt_path)
handeye_data = pd.read_csv(handeye_path)
memory_data = pd.read_csv(memory_path)
simon_data = pd.read_csv(simon_path)
apm_data = pd.read_csv(apm_path)

# Merge the datasets on 'email'
merged_data = pd.merge(rt_data, handeye_data, on='email', how='outer')
merged_data = pd.merge(merged_data, memory_data, on='email', how='outer')
merged_data = pd.merge(merged_data, simon_data, on='email', how='outer')
merged_data = pd.merge(merged_data, apm_data, on='email', how='outer')

# Handle NaN values if necessary
# merged_data.fillna(0, inplace=True)

# Save the merged dataset
merged_data.to_csv('./merged_dataset.csv', index=False)
