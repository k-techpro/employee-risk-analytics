def calculate_risk_score(df):

    df['risk_score'] = (
        df['failed_login_attempts'] * 10 +
        df['sensitive_files_accessed'] * 8 +
        df['download_count'] * 2 +
        df['after_hours'] * 15 +
        df['usb_usage'] * 10
    )

    return df


def categorize_risk(df):

    def label(score):
        if score < 30:
            return "LOW"
        elif score < 70:
            return "MEDIUM"
        else:
            return "HIGH"

    df['risk_level'] = df['risk_score'].apply(label)

    return df