import pandas as pd

# create data

data ={
    "products" : [

        "Beer",
        "Wine",
        "whisky"
    ],

    "sales" :[120,90, 150]
}

df = pd.DataFrame(data)
print(df)
print("Total sales", df["sales"].sum())