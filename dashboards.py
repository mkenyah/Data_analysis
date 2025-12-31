import streamlit as st
import pandas as pd
import sqlite3

st.set_page_config(page_title="Business Analytics Dashboard", layout="wide")

conn = sqlite3.connect("business_sales.db")
df = pd.read_sql("SELECT * FROM sales", conn)

# CLEAN COLUMN NAMES (Fixes KeyError)
df.columns = df.columns.str.strip().str.lower()

# Now your calculations will work correctly
df["revenue"] = df["quantity_sold"] * df["price"]
df["profit"] = (df["price"] - df["cost"]) * df["quantity_sold"]




# Dashboard layout
st.title("📊 Business Sales Dashboard")

col1, col2, col3, col4 , col5 = st.columns(5)

col1.metric("Total Revenue", f"Ksh {df['revenue'].sum():,.0f}")
col2.metric("Total Profit", f"Ksh {df['profit'].sum():,.0f}")
col3.metric("Total Units Sold", df["quantity_sold"].sum())
profit_margin = (df["profit"].sum() / df["revenue"].sum()) * 100
col4.metric("Profit Margin", f"{profit_margin:.2f}%")
col5.metric("Top performing product", df.groupby("product")["revenue"].sum().idxmax())



# Revenue by Product
st.subheader("Revenue by Product")
st.bar_chart(df.groupby("product")["revenue"].sum())



# Interactive Filters

product_filter = st.selectbox(
    "Select Product",
    options=["All"] + list(df["product"].unique())
)

if product_filter != "All":
    df = df[df["product"] == product_filter]

    # Data table

st.subheader("Sales Data")
st.dataframe(df)




