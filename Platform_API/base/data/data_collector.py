import pandas as pd


def save_data_to_excel(data, filename):
    df = pd.DataFrame(data)
    df.to_excel(filename, index=False)
