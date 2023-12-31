import pandas as pd
import requests
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        print(f"Failed to fetch data: Status code {response.status_code}")
        return pd.DataFrame()

def filter_outliers(data, z_thresh=3):
    # Filtering outliers based on z-score
    z_scores = stats.zscore(data)
    abs_z_scores = np.abs(z_scores)
    filtered_entries = (abs_z_scores < z_thresh)
    return data[filtered_entries]

def convert_performance(data):
    # Convert the 'performance' column to an integer after removing leading zeros
    data['performance'] = data['performance'].apply(lambda x: int(x.lstrip('0')) if x.lstrip('0') else 0)
    return data

def analyze_and_save_data(data, filename):
    # Summary Statistics
    print("Summary Statistics for Performance:\n", data['apm_performance'].describe())

    # Visualization
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data['apm_performance'])
    plt.title("Filtered APM Performance Distribution")
    plt.xlabel("APM Performance")
    plt.show()

    # Saving to CSV
    data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main(api_url, output_filename):
    # Fetching the generators
    df = fetch_data(api_url)

    # Convert performance to numeric format
    df = convert_performance(df)

    # Group by email and average the performance
    df = df.groupby('email', as_index=False)['performance'].mean().rename(columns={'performance': 'apm_performance'})

    # Filter outliers
    df['apm_performance'] = filter_outliers(df['apm_performance'])

    # Analyze and Save Data
    analyze_and_save_data(df[['email', 'apm_performance']], output_filename)

if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/api/apm/"
    output_csv = "filtered_apm_data.csv"
    main(api_url, output_csv)
