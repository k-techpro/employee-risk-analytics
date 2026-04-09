import pandas as pd

def save_data(df, path):
    df.to_csv(path, index=False)


def load_data(path):
    return pd.read_csv(path)