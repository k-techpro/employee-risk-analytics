def add_features(df):
    
    # Session duration
    df['session_duration_hours'] = (
        (df['logout_datetime'] - df['login_datetime']).dt.total_seconds() / 3600
    )

    # After-hours activity
    df['after_hours'] = df['login_datetime'].dt.hour.apply(
        lambda x: 1 if x < 8 or x > 20 else 0
    )

    return df