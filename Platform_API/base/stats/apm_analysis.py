import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        print(f"Failed to fetch data: Status code {response.status_code}")
        return pd.DataFrame()

def convert_performance(data):
    # Convert the 'performance' column to an integer after removing leading zeros
    data['performance'] = data['performance'].apply(lambda x: int(x.lstrip('0')) if x.lstrip('0') else 0)
    return data

def analyze_and_save_data(data, filename):
    # Summary Statistics
    print("Summary Statistics for Performance:\n", data['performance'].describe())

    # Visualization
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=data['performance'])
    plt.title("APM Performance Distribution")
    plt.xlabel("APM Performance")
    plt.show()

    # Saving to CSV
    data.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main(api_url, output_filename):
    # Fetching the data
    df = fetch_data(api_url)

    # Convert performance to numeric format
    df = convert_performance(df)

    # Analyze and Save Data
    analyze_and_save_data(df[['email', 'performance']], output_filename)

if __name__ == "__main__":
    api_url = "http://127.0.0.1:8000/api/apm/"
    output_csv = "apm_data.csv"
    main(api_url, output_csv)
