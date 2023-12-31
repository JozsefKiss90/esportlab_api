import pandas as pd
import requests
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        # Manually parse the JSON response
        data = response.json()
        # Flatten the generators and extract performance and email
        flattened_data = []
        for entry in data:
            performance = entry['performance']
            email = entry['email']
            performance['email'] = email
            flattened_data.append(performance)
        return pd.DataFrame(flattened_data)
    else:
        print(f"Failed to fetch data: Status code {response.status_code}")
        return pd.DataFrame()

def filter_outliers(data):
    # Assuming outliers are defined as values more than 3 standard deviations from the mean
    return data[np.abs(stats.zscore(data)) < 3]

def analyze_and_save_data(data, filename):
    # Summary Statistics
    print("Summary Statistics for Correct Percent:\n", data['correctPercent'].describe())
    print("Summary Statistics for Simon Effect:\n", data['simonEffect'].describe())

    # Visualization
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(data=data['correctPercent'], ax=axes[0])
    axes[0].set_title("Correct Percent Distribution")
    axes[0].set_ylabel("Correct Percent")

    sns.boxplot(data=data['simonEffect'], ax=axes[1])
    axes[1].set_title("Simon Effect Distribution")
    axes[1].set_ylabel("Simon Effect (ms)")
    plt.show()

    # Saving to CSV
    data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main(api_url, output_filename):
    # Fetching and preparing the generators
    df = fetch_data(api_url)
    print(df.head())  # Debug: print the first few rows of the DataFrame to check its structure

    # Filtering out outliers
    df['correctPercent'] = filter_outliers(df['correctPercent'].astype(float))
    df['simonEffect'] = filter_outliers(df['simonEffect'].astype(float))

    # Analyze and Save Data
    analyze_and_save_data(df[['email', 'correctPercent', 'simonEffect']], output_filename)

if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/api/simontask/"
    output_csv = "filtered_simon_data.csv"
    main(api_url, output_csv)
