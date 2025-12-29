import pandas as pd

#pandas is used for data analysis and manipulation of data

data = {
    "products" : ["Beer", "Wine", "Whisky"],
    "Quantity": [120, 190, 150],
    "prices": [250, 300, 500]
}


df= pd.DataFrame(data)
df["Total"] = df["Quantity"] * df["prices"]
df["Total_Revenue"] = df["Total"].sum()

print("The Best sellikng product is: ", df.loc[df["Quantity"].idxmax()])



print(df)
