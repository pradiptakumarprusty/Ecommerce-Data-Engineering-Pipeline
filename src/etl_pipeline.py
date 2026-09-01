import pandas as pd
import os
import logging
# --------------------------------------------------
# LOGGING CONFIGURATION
# --------------------------------------------------

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/etl_pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

logger.info("Starting E-Commerce ETL Pipeline")

print("Starting E-Commerce ETL Pipeline...")

# --------------------------------------------------
# 1. DATA EXTRACTION
# --------------------------------------------------

try:
    customers = pd.read_csv("data/customers.csv")
    products = pd.read_csv("data/products.csv")
    orders = pd.read_csv("data/orders.csv")

    print("✓ Data extraction completed")
    logger.info("Data extraction completed")

except FileNotFoundError as e:
    print("❌ Error: Required data file not found.")
    logger.error(f"Data extraction failed: {e}")
    exit()

except Exception as e:
    print("❌ Error while extracting data:", e)
    logger.error(f"Data extraction failed: {e}")
    exit()

# --------------------------------------------------
# 2. DATA QUALITY VALIDATION
# --------------------------------------------------

print("\nRunning data quality checks...")

# Check missing values
print("\nMissing values:")

print("Customers:")
print(customers.isnull().sum())

print("\nProducts:")
print(products.isnull().sum())

print("\nOrders:")
print(orders.isnull().sum())


# Check duplicate records
print("\nDuplicate records:")

print("Customers:", customers.duplicated().sum())
print("Products:", products.duplicated().sum())
print("Orders:", orders.duplicated().sum())


# Check negative / invalid values
if "price" in products.columns:
    invalid_products = (products["price"] < 0).sum()
    print("\nInvalid product prices:", invalid_products)

if "quantity" in orders.columns:
    invalid_quantity = (orders["quantity"] <= 0).sum()
    print("Invalid order quantities:", invalid_quantity)


print("\n✓ Data quality validation completed")

logger.info("Data quality validation completed")

# --------------------------------------------------
# 3. DATA CLEANING
# --------------------------------------------------

customers = customers.drop_duplicates()
products = products.drop_duplicates()
orders = orders.drop_duplicates()

# Fill missing values
customers = customers.fillna("Unknown")
products = products.fillna("Unknown")

if "quantity" in orders.columns:
    orders["quantity"] = orders["quantity"].fillna(0)

print("✓ Data cleaning completed")

logger.info("Data cleaning completed")

# --------------------------------------------------
# 4. DATA TRANSFORMATION
# --------------------------------------------------

if "quantity" in orders.columns and "price" in orders.columns:
    orders["total_amount"] = orders["quantity"] * orders["price"]

print("✓ Data transformation completed")

logger.info("Data transformation completed")


# --------------------------------------------------
# 5. SAVE PROCESSED DATA
# --------------------------------------------------

output_folder = "processed_data"

os.makedirs(output_folder, exist_ok=True)

customers.to_csv(
    os.path.join(output_folder, "customers_processed.csv"),
    index=False
)

products.to_csv(
    os.path.join(output_folder, "products_processed.csv"),
    index=False
)

orders.to_csv(
    os.path.join(output_folder, "orders_processed.csv"),
    index=False
)

print("\nProcessed data saved to:", output_folder)

print("\nETL Pipeline completed successfully!")
logger.info("ETL Pipeline completed successfully")