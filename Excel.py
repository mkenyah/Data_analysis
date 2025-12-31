import pandas as pd
import matplotlib.pyplot as plt
import os

# Path to Excel file
excel_path = r"C:\Users\Joseph kirika\Desktop\monthly_sales.xlsx"

# Check if file exists
if not os.path.exists(excel_path):
    raise FileNotFoundError(f"Excel file not found at {excel_path}")

# Load Excel file
xls = pd.ExcelFile(excel_path)
print("Sheets in Excel file:", xls.sheet_names)

# Load the first sheet
# Try to detect header automatically
df = pd.read_excel(excel_path, sheet_name=0, header=0)
print("Raw data preview:\n", df.head())

# If DataFrame has no columns, try loading without headers
if df.columns.empty:
    df = pd.read_excel(excel_path, sheet_name=0, header=None)
    df.columns = df.iloc[0]  # use first row as header
    df = df[1:]  # remove the header row from data

# Clean column names
df.columns = df.columns.astype(str).str.strip().str.lower().str.replace(" ", "_")
print("Columns after cleaning:", df.columns.tolist())

# Define expected columns and map to closest match
expected_columns = ["quantity", "price", "cost", "category"]
for col in expected_columns:
    if col not in df.columns:
        # Attempt simple fuzzy match
        match = [c for c in df.columns if col in c]
        if match:
            df.rename(columns={match[0]: col}, inplace=True)
        else:
            raise KeyError(f"Expected column '{col}' not found in Excel file")

# Convert numeric columns to float
for col in ["quantity", "price", "cost"]:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Business calculations
df["revenue"] = df["quantity"] * df["price"]
df["profit"] = (df["price"] - df["cost"]) * df["quantity"]
df["profit_margin"] = (df["profit"] / df["revenue"]) * 100
df["profit_margin"] = df["profit_margin"].fillna(0)

# Summary report by category
summary = df.groupby("category")[["revenue", "profit"]].sum().reset_index()
print("Summary report generated:\n", summary)

# Export to Excel
output_file = "Automated_sales_report.xlsx"
with pd.ExcelWriter(output_file, engine="xlsxwriter") as writer:
    summary.to_excel(writer, sheet_name="Summary", index=False)
    df.to_excel(writer, sheet_name="Detailed_sales", index=False)
print(f"Reports exported to {output_file}")

# Create bar chart for revenue by category
plt.figure(figsize=(8, 6))
summary.plot(x="category", y="revenue", kind="bar", legend=False, color="skyblue", title="Revenue by Category")
plt.ylabel("Revenue")
plt.tight_layout()
chart_file = "revenue_chart.png"
plt.savefig(chart_file)
plt.show()
print(f"Revenue chart saved as {chart_file}")
