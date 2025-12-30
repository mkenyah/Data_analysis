import pandas as pd 

# 1. Load Data with Raw String (r) to handle Windows backslashes
df = pd.read_csv(r"C:\Users\Joseph kirika\Desktop\sales_data.csv")

# 2. Clean the Data (Modern Syntax for 2025)
df["Quantity_Sold"] = df["Quantity_Sold"].fillna(0)
df["Price"] = df["Price"].fillna(df["Price"].mean())
df["Cost"] = df["Cost"].fillna(df["Cost"].mean())

# 3. Create Business Columns
df["Revenue"] = df["Quantity_Sold"] * df["Price"]
# Fixed Profit calculation logic
df["Profit"] = df["Revenue"] - (df["Cost"] * df["Quantity_Sold"])

# 4. Analysis and Sorting
total_rev = df["Revenue"].sum()
# Ensure column names match your CSV capitalization (e.g., "Product" or "product")
performance = df[["Product", "Revenue", "Profit"]]
df_sorted = df.sort_values(by="Revenue", ascending=False)

# 5. Export and Verify
print(f"Total Revenue: ${total_rev:,.2f}")
print(df_sorted.head())

df_sorted.to_csv("cleaned_sales_data.csv", index=False)
