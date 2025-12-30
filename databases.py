import sqlite3
import pandas as pd

# 1. Establish connection
conn = sqlite3.connect("business_sales.db")
cursor = conn.cursor()

# 2. Create the table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Product TEXT,
        Category TEXT,
        Quantity_Sold INTEGER,
        Price REAL,
        Cost REAL
    )
""")

# Optional: Clear table to prevent duplicate entries if run multiple times
cursor.execute("DELETE FROM sales")

# 3. Data to insert
sales_data = [
    ("Item A", "Category 1", 120, 250, 180),
    ("Item B", "Category 1", 80, 800, 600),
    ("Item C", "Category 2", 60, 1500, 1100),
    ("Item D", "Category 2", 40, 1200, 900),
    ("Item E", "Category 3", 50, 900, 650)
]

# 4. Insert data
cursor.executemany(
    "INSERT INTO sales (Product, Category, Quantity_Sold, Price, Cost) VALUES (?, ?, ?, ?, ?)",
    sales_data
)
conn.commit()
print("Database updated successfully.")

# 5. Read into Pandas (IMPORTANT: Must be done while connection is still OPEN)
query = "SELECT * FROM sales"
df = pd.read_sql(query, conn)

# 6. NOW close the connection
conn.close()

# 7. Display the DataFrame
print("\nRetrieved Data from SQLite:")
print(df)

# Bonus: Calculate a quick metric to verify data
df['Total_Revenue'] = df['Quantity_Sold'] * df['Price']
print(f"\nTotal Portfolio Value: ${df['Total_Revenue'].sum():,.2f}")


# 1. Calculate the sum of quantity sold per product
product_totals = df.groupby("Product")["Quantity_Sold"].sum().reset_index()

# 2. Display the numerical results
print("Total Quantity Sold Per Product:")
print(product_totals)

# Profit greater than 20,000
greater_profit = df[df["Total_Revenue"]>20000]

print("product with profit greater than 20, 000", greater_profit)

# print(greater_profit[["products", "Total_revenue"]])

print(greater_profit)


# export to cvs

df.to_csv("business_sales_report.csv", index=False)

