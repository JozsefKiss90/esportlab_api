import requests
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        print(f"Failed to fetch generators: Status code {response.status_code}")
        return pd.DataFrame()

def filter_outliers(data):
    return data[np.abs(stats.zscore(data)) < 3]

def process_handeye_data(df):
    # Separate generators into two experiments based on length of performance array
    exp1 = df[df['performance'].map(len) == 12]  # Experiment 1 has 12 generators points
    exp2 = df[df['performance'].map(len) == 5]   # Experiment 2 has 5 generators points

    # Calculate average performance for each user in each experiment
    exp1_avg = exp1.groupby('email')['performance'].apply(lambda x: np.mean([filter_outliers(np.array(item)) for item in x])).reset_index()
    exp2_avg = exp2.groupby('email')['performance'].apply(lambda x: np.mean([filter_outliers(np.array(item)) for item in x])).reset_index()

    # Merge the two datasets
    merged_df = pd.merge(exp1_avg, exp2_avg, on='email', how='outer')
    merged_df.columns = ['email', 'avg_perf_exp1', 'avg_perf_exp2']
    return merged_df

def analyze_and_save_data(data, filename):
    # Summary Statistics
    print("Summary Statistics for Experiment 1:\n", data['avg_perf_exp1'].describe())
    print("Summary Statistics for Experiment 2:\n", data['avg_perf_exp2'].describe())

    # Visualization for Experiment 1
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data['avg_perf_exp1'])
    plt.title("Hand-Eye Coordination Data Distribution - Experiment 1")
    plt.ylabel("Performance (ms)")
    plt.show()

    # Visualization for Experiment 2
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=data['avg_perf_exp2'])
    plt.title("Hand-Eye Coordination Data Distribution - Experiment 2")
    plt.ylabel("Performance (ms)")
    plt.show()

    # Saving to CSV
    data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")


def main(api_url, output_filename):
    df = fetch_data(api_url)
    processed_df = process_handeye_data(df)
    analyze_and_save_data(processed_df, output_filename)

if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/api/handeye/"
    output_csv = "filtered_handeye_data.csv"
    main(api_url, output_csv)
