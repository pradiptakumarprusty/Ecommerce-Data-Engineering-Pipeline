python
import pandas as pd
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

# Create output directory if it does not exist
OUTPUT_DIR.mkdir(exist_ok=True)


def load_data():
    """Load raw e-commerce datasets."""

    customers = pd.read_csv(DATA_DIR / "customers.csv")
    products = pd.read_csv(DATA_DIR / "products.csv")
    orders = pd.read_csv(DATA_DIR / "orders.csv")

    return customers, products, orders


def clean_data(customers, products, orders):
    """Clean and validate the datasets."""

    # Remove duplicate records
    customers = customers.drop_duplicates()
    products = products.drop_duplicates()
    orders = orders.drop_duplicates()

    # Remove rows with missing values
    customers = customers.dropna()
    products = products.dropna()
    orders = orders.dropna()

    return customers, products, orders


def transform_data(customers, products, orders):
    """Join customer, product, and order data."""

    # Join orders with products
    orders_products = orders.merge(
        products,
        on="product_id",
        how="left"
    )

    # Join with customers
    final_data = orders_products.merge(
        customers,
        on="customer_id",
        how="left"
    )

    # Calculate total order value
    final_data["total_amount"] = (
        final_data["quantity"] * final_data["price"]
    )

    return final_data


def save_data(final_data):
    """Save processed data."""

    output_file = OUTPUT_DIR / "ecommerce_processed.csv"

    final_data.to_csv(
        output_file,
        index=False
    )

    print(f"Processed data saved to: {output_file}")


def main():
    """Run the complete ETL pipeline."""

    print("Starting E-Commerce ETL Pipeline...")

    # Extract
    customers, products, orders = load_data()
    print("✓ Data extraction completed")

    # Transform
    customers, products, orders = clean_data(
        customers,
        products,
        orders
    )
    print("✓ Data cleaning completed")

    final_data = transform_data(
        customers,
        products,
        orders
    )
    print("✓ Data transformation completed")

    # Load
    save_data(final_data)
    print("✓ ETL Pipeline completed successfully")


if __name__ == "__main__":
    main()
