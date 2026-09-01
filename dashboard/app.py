import streamlit as st
import sqlite3
import pandas as pd
import os

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="E-Commerce Analytics Dashboard",
    page_icon="🛒",
    layout="wide"
)

# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE_PATH = os.path.join(BASE_DIR, "ecommerce.db")

connection = sqlite3.connect(DATABASE_PATH)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

customers = pd.read_sql_query(
    "SELECT * FROM customers",
    connection
)

products = pd.read_sql_query(
    "SELECT * FROM products",
    connection
)

orders = pd.read_sql_query(
    "SELECT * FROM orders",
    connection
)

connection.close()

# --------------------------------------------------
# MERGE ORDER + PRODUCT DATA
# --------------------------------------------------

orders = orders.merge(
    products[["product_id", "product_name", "category", "price"]],
    on="product_id",
    how="left"
)

# Calculate total amount
orders["total_amount"] = orders["quantity"] * orders["price"]

# --------------------------------------------------
# DASHBOARD TITLE
# --------------------------------------------------

st.title("🛒 E-Commerce Analytics Dashboard")

st.write(
    "Interactive sales, product and customer analytics"
)

# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------

total_customers = customers["customer_id"].nunique()

total_orders = orders["order_id"].nunique()

total_products_sold = orders["quantity"].sum()

total_revenue = orders["total_amount"].sum()

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "👥 Total Customers",
    total_customers
)

col2.metric(
    "🛒 Total Orders",
    total_orders
)

col3.metric(
    "📦 Products Sold",
    int(total_products_sold)
)

col4.metric(
    "💰 Total Revenue",
    f"₹{total_revenue:,.2f}"
)

# --------------------------------------------------
# REVENUE BY CATEGORY
# --------------------------------------------------

st.subheader("📊 Revenue by Category")

category_revenue = (
    orders
    .groupby("category")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(category_revenue)

# --------------------------------------------------
# TOP SELLING PRODUCTS
# --------------------------------------------------

st.subheader("🏆 Top-Selling Products")

top_products = (
    orders
    .groupby("product_name")["quantity"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_products)

# --------------------------------------------------
# DAILY REVENUE
# --------------------------------------------------

st.subheader("📅 Daily Revenue")

daily_revenue = (
    orders
    .groupby("order_date")["total_amount"]
    .sum()
)

st.line_chart(daily_revenue)

# --------------------------------------------------
# SALES BY STATE
# --------------------------------------------------

st.subheader("📍 Sales by State")

orders_with_customer = orders.merge(
    customers[["customer_id", "state"]],
    on="customer_id",
    how="left"
)

state_sales = (
    orders_with_customer
    .groupby("state")["total_amount"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(state_sales)

# --------------------------------------------------
# DATA TABLE
# --------------------------------------------------

st.subheader("📋 Order Details")

st.dataframe(
    orders[
        [
            "order_id",
            "customer_id",
            "product_name",
            "category",
            "quantity",
            "price",
            "total_amount",
            "order_date"
        ]
    ],
    use_container_width=True
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "E-Commerce Data Engineering Pipeline | "
    "Python + SQL + SQLite + Streamlit"
)