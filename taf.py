import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression

# Data frame
data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "Revenue": [30000, 32000, 35000, 33000, 36000, 37000, 40000, 39000, 41000, 42000, 45000, 47000]
}
df = pd.DataFrame(data)

# 1. Forecasting Linear Trend
df["Month_Num"] = np.arange(1, len(df) + 1)
x = df[["Month_Num"]] 
y = df["Revenue"]

model = LinearRegression()
model.fit(x, y)

# Predict next 3 months
future_months = np.array([13, 14, 15]).reshape(-1, 1)
forecast = model.predict(future_months)
print("Revenue Forecast for next 3 months:", forecast)

# 2. Plot Revenue Forecast
plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Revenue"], marker="o", label="Actual Revenue")
future_labels = ["Jan+1", "Feb+1", "Mar+1"]
plt.plot(future_labels, forecast, marker="o", linestyle="--", color="red", label="Forecasted Revenue")
plt.title("Monthly Revenue with Forecast (2025 Data)")
plt.ylabel("Revenue (Ksh)")
plt.legend()
plt.show()

# 3. Monthly Profit Trend (25% margin)
df["profit"] = df["Revenue"] * 0.25
plt.figure(figsize=(10, 5))
# Fixed typos: "Monnth" -> "Month", "Profit" -> "profit"
sns.lineplot(x="Month", y="profit", data=df, marker="o", color="green")
plt.title("Monthly Profit Trend (2025 Data)")
plt.ylabel("Profit (Ksh)")
plt.show()

# 4. Forecast Profit
future_profit = forecast * 0.25
print("Profit Forecast for the next 3 months:", future_profit)

# 5. PLOT Profit Forecast
plt.figure(figsize=(10, 5))
# Fixed syntax: df("Month") -> df["Month"]
plt.plot(df["Month"], df["profit"], marker="o", label="Actual Profit")
plt.plot(future_labels, future_profit, marker="o", linestyle="--", color="orange", label="Forecasted Profit")
plt.title("Monthly Profit with Forecast (2026 Data)")
plt.ylabel("Profit (Ksh)")
plt.legend()
plt.show()
