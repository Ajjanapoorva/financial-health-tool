import pandas as pd
import sys
import json

file_path = sys.argv[1]
df = pd.read_csv(file_path)

df = df.dropna()

total_revenue = df["revenue"].sum()
total_expenses = df["expenses"].sum()

profit = total_revenue - total_expenses
profit_margin = (profit / total_revenue) * 100

# Risk
if profit_margin < 5:
    risk = "High Risk"
elif profit_margin < 15:
    risk = "Medium Risk"
else:
    risk = "Low Risk"

# Insight
def insight(pm):
    if pm < 10:
        return "Reduce expenses."
    elif pm < 25:
        return "Improve efficiency."
    return "Business performing well."

# ---- Revenue Forecast ----
growth = df["revenue"].pct_change().mean()
forecast = df["revenue"].iloc[-1] * (1 + growth)

# ---- Loan Eligibility ----
if profit_margin > 20:
    loan_status = "Eligible"
elif profit_margin > 10:
    loan_status = "Review Required"
else:
    loan_status = "Not Eligible"

result = {
    "revenue": float(total_revenue),
    "expenses": float(total_expenses),
    "profit": float(profit),
    "profit_margin": float(profit_margin),
    "risk": risk,
    "forecast": float(forecast),
    "loan_status": loan_status,
    "insight": insight(profit_margin)
}

print(json.dumps(result))
