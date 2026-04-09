import pandas as pd

def load_data(path):
    return pd.read_csv(path)


def preprocess_data(df):
    df['date'] = pd.to_datetime(df['date'])
    
    df['login_datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['login_time'])
    df['logout_datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['logout_time'])

    # Handle overnight sessions
    df.loc[df['logout_datetime'] < df['login_datetime'], 'logout_datetime'] += pd.Timedelta(days=1)

    return df