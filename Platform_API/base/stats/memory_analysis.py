import pandas as pd
import requests
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        print(f"Failed to fetch data: Status code {response.status_code}")
        return pd.DataFrame()

def filter_outliers(data):
    # Assuming outliers are defined as values more than 3 standard deviations from the mean
    return data[np.abs(stats.zscore(data)) < 3]

def analyze_and_save_data(data, filename):
    # Summary Statistics
    print("Summary Statistics for Memory Span:\n", data['memorySpan'].describe())

    # Visualization
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data['memorySpan'])
    plt.title("Memory Span Distribution")
    plt.xlabel("Memory Span")
    plt.show()

    # Saving to CSV
    data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main(api_url, output_filename):
    # Fetching the data
    df = fetch_data(api_url)

    # Assuming the structure is straightforward with 'memorySpan' and 'email' fields
    # Filter out outliers in memorySpan
    df['memorySpan'] = filter_outliers(df['memorySpan'])

    # Analyze and Save Data
    analyze_and_save_data(df[['email', 'memorySpan']], output_filename)

if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/api/memory/"
    output_csv = "filtered_memory_data.csv"
    main(api_url, output_csv)
