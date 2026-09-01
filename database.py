import sqlite3
import pandas as pd
import os

# --------------------------------------------------
# DATABASE PATH
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, "ecommerce.db")

# --------------------------------------------------
# CONNECT TO DATABASE
# --------------------------------------------------

connection = sqlite3.connect(DATABASE_PATH)

print("✓ Connected to SQLite database")

# --------------------------------------------------
# LOAD PROCESSED DATA
# --------------------------------------------------

customers = pd.read_csv(
    os.path.join(BASE_DIR, "processed_data", "customers_processed.csv")
)

products = pd.read_csv(
    os.path.join(BASE_DIR, "processed_data", "products_processed.csv")
)

orders = pd.read_csv(
    os.path.join(BASE_DIR, "processed_data", "orders_processed.csv")
)

# --------------------------------------------------
# CREATE DATABASE TABLES
# --------------------------------------------------

customers.to_sql(
    "customers",
    connection,
    if_exists="replace",
    index=False
)

products.to_sql(
    "products",
    connection,
    if_exists="replace",
    index=False
)

orders.to_sql(
    "orders",
    connection,
    if_exists="replace",
    index=False
)

# --------------------------------------------------
# CLOSE DATABASE
# --------------------------------------------------

connection.close()

print("✓ Customers table created")
print("✓ Products table created")
print("✓ Orders table created")
print("✓ Database integration completed successfully")