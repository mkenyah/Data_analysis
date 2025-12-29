import pandas as pd

products = ["Beer", "Wine", "Whisky", "Vodka", "Gin"]
quantity_sold = [120, 80, 60, 40, 50]
price_per_unit = [250, 800, 1500, 1200, 900]


data = {
    "Products": ["Beer", "Wine", "Whisky", "Vodka", "Gin"],
    "quantity_sold": [120, 80, 60, 40, 50],
    "price_per_unit":[250, 800, 1500, 1200, 900]

}


df = pd.DataFrame(data)

df["Total_revenue"] = df["price_per_unit"] * df["quantity_sold"]

df["Most_Sellng_product"] = df["quantity_sold"].idxmax()


print("Individual Products Revenue")

print(df[["Products", "Total_revenue"]])

print("The Most selling product is:", df.loc[df["Most_Sellng_product"].iloc[0], "Products"])

print("Total revenue is : ", df["Total_revenue"].sum())







