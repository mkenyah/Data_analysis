import pandas as pd

# This is what is called a data frame

data = {
    "Product": ["Beer", "Wine", "Whisky", "Vodka", "Gin"],
    "Quantity_Sold": [120, 80, 60, 40, 50],
    "Price": [250, 800, 1500, 1200, 900],
    "Cost": [180, 600, 1100, 900, 650]
}

df = pd.DataFrame(data)

# BUSINESS COLUMNS CALCULATIONS

# Revenue
df["Revenue"] = df["Quantity_Sold"] * df["Price"]

# Profit
df["Profit"] = (df["Price"] - df["Cost"]) * df["Quantity_Sold"]

# profit margin

df["profit_margin_%"] = (df["Profit"] / df["Revenue"]) * 100



df["Revenue"].sum()
df["Profit"].sum()


#Best selling product
best_selling_product = df.loc[df["Quantity_Sold"].idxmax()]

most_profitable_product = df.loc[df["Profit"].idxmax()]

lowest_profit_margin =df[df["profit_margin_%"] < 26]


print("THe most selling product is : \n",best_selling_product )

print("The most profitable product is: \n",most_profitable_product)
print("The lowest profit margin is: \n",lowest_profit_margin)


# SORTING AND FILTERING ( sort revenue by Descending order)

# 1. Sort the entire DataFrame by the "Revenue" column
df = df.sort_values(by="Revenue", ascending=True)

# 2. Save the sorted DataFrame to a CSV file
# Use index=False to avoid saving the row numbers as a separate column
df.to_csv("Sales_report.csv", index=False)

# 3. Print the sorted results
print("Sorted Values are:\n", df)

