from sklearn.ensemble import IsolationForest

def detect_anomalies(df):

    features = df[
        ['failed_login_attempts',
         'files_accessed',
         'sensitive_files_accessed',
         'download_count',
         'session_duration_hours',
         'risk_score']
    ]

    model = IsolationForest(contamination=0.2, random_state=42)

    df['anomaly'] = model.fit_predict(features)

    df['anomaly'] = df['anomaly'].apply(
        lambda x: "Anomaly" if x == -1 else "Normal"
    )

    return df