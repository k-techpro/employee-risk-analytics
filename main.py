from src.data_preprocessing import load_data, preprocess_data
from src.feature_engineering import add_features
from src.risk_scoring import calculate_risk_score, categorize_risk
from src.anomaly_detection import detect_anomalies
from src.utils import save_data

RAW_PATH = "data/raw/employee_activity.csv"
PROCESSED_PATH = "data/processed/cleaned_employee_activity.csv"


def run_pipeline():
    df = load_data(RAW_PATH)
    df = preprocess_data(df)
    df = add_features(df)
    df = calculate_risk_score(df)
    df = categorize_risk(df)
    df = detect_anomalies(df)
    save_data(df, PROCESSED_PATH)
    print("Pipeline executed successfully.")
    print(f"Processed file saved at: {PROCESSED_PATH}")


if __name__ == "__main__":
    run_pipeline()