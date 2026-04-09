from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)

DATA_PATH = os.path.join("data", "processed", "cleaned_employee_activity.csv")


@app.route("/")
def dashboard():
    if not os.path.exists(DATA_PATH):
        return "Processed dataset not found. Run main.py first."

    df = pd.read_csv(DATA_PATH)

    total_employees = len(df)
    high_risk_count = len(df[df["risk_level"] == "HIGH"])
    medium_risk_count = len(df[df["risk_level"] == "MEDIUM"])
    low_risk_count = len(df[df["risk_level"] == "LOW"])
    anomaly_count = len(df[df["anomaly"] == "Anomaly"])

    top_risky = df.sort_values(by="risk_score", ascending=False)[
        ["employee_name", "department", "risk_score", "risk_level", "anomaly"]
    ].head(5)

    records = top_risky.to_dict(orient="records")

    return render_template(
        "index.html",
        total_employees=total_employees,
        high_risk_count=high_risk_count,
        medium_risk_count=medium_risk_count,
        low_risk_count=low_risk_count,
        anomaly_count=anomaly_count,
        records=records
    )


if __name__ == "__main__":
    app.run(debug=True)