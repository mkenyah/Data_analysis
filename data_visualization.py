import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = {
    "Product": ["Beer", "Wine", "Whisky", "Vodka", "Gin"],
    "Quantity_Sold": [120, 80, 60, 40, 50],
    "Price": [250, 800, 1500, 1200, 900],
    "Cost": [180, 600, 1100, 900, 650]
}

df = pd.DataFrame(data)

df["Revenue"] = df["Quantity_Sold"] * df["Price"]
df["Profit"] = (df["Price"] - df["Cost"]) * df["Quantity_Sold"]
df["Profit_Margin_%"] = (df["Profit"] / df["Revenue"]) * 100


# SALES BY PRODUCT BAR CHART


# plt.figure(figsize = (8,5))
# plt.bar(df["Product"], df["Revenue"])
# plt.title("Revenue by product")
# plt.xlabel("product")
# plt.ylabel("Revenue")
# plt.show()

# PROFIT COMPARISON
# plt.figure(figsize=(8, 5))
# sns.barplot(x="Product", y ="Profit", data = df)
# plt.title("profit by product")
# plt.show()


# PROFIT MARGIN VISUALIZATION

# plt.figure(figsize=(8, 5))
# sns.lineplot(x= "Product", y = "Profit_Margin_%", data = df, markers="o")
# plt.title("profit margin by product")
# plt.ylabel("profit margin (%)")
# plt.xlabel("Products")
# plt.show()


# Quantity sold per product

# plt.figure(figsize=(8, 5))
# sns.barplot(x="Product", y ="Quantity_Sold", data = df)
# plt.title("Quantity sold per product")
# plt.xlabel("Product")
# plt.ylabel("Quantity sold")
# plt.show()

# Top 3 products by profit
top_3_profit = df.nlargest(3, "Profit")[["Product", "Profit"]]
plt.figure(figsize=(8,5))
sns.barplot(x="Product", y="Profit", data=top_3_profit)

plt.title("Top 3 products by Profit")
plt.xlabel("Product")
plt.ylabel("Profit")
plt.show()
