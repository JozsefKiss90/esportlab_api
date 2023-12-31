import requests
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        print(f"Failed to fetch generators: Status code {response.status_code}")
        return pd.DataFrame()

def filter_outliers(data):
    # Assuming outliers are defined as values more than 3 standard deviations from the mean
    return data[np.abs(stats.zscore(data)) < 3]

def analyze_and_save_data(data, filename):
    # Basic Summary Statistics
    print("Summary Statistics:\n", data.describe())

    # Visualization
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data['avg_rt'])
    plt.title("Filtered Reaction Time Data Distribution")
    plt.xlabel("Reaction Time (ms)")
    plt.show()

    # Saving to CSV
    data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main(api_url, output_filename):
    df = fetch_data(api_url)

    # Filter for rows where rtArray is not empty and user has multiple tests
    df = df[df['rtArray'].map(lambda d: len(d) > 0)]
    df['rtArray'] = df['rtArray'].apply(lambda x: np.mean(x))
    df = df.groupby('email', as_index=False).agg({'rtArray': 'mean'})
    df.columns = ['email', 'avg_rt']

    # Filter outliers
    df['avg_rt'] = filter_outliers(df['avg_rt'])

    # Analyze and Save Data
    analyze_and_save_data(df, output_filename)

if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/api/rt/"
    output_csv = "filtered_rt_data.csv"
    main(api_url, output_csv)
