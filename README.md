# 🛒 E-Commerce Data Engineering & Analytics Pipeline

## 📌 Project Overview

This project demonstrates an end-to-end **E-Commerce Data Engineering and Analytics Pipeline** built to process, validate, transform, store, and analyze customer, product, and order data.

The project uses **Python, Pandas, SQL, SQLite, and Streamlit** to transform raw CSV data into structured, analytics-ready data and interactive business insights.

---

## 🎯 Project Objectives

* Build an end-to-end ETL pipeline using Python and Pandas.
* Perform data quality validation and cleaning.
* Remove duplicate records and handle missing values.
* Transform raw order data and calculate business metrics.
* Store structured data in a SQLite database.
* Perform SQL-based business analysis.
* Build an interactive Streamlit analytics dashboard.
* Maintain the project using Git and GitHub.

---

## 📂 Dataset

The project uses three primary datasets:

| Dataset         | Description                                |
| --------------- | ------------------------------------------ |
| `customers.csv` | Customer information                       |
| `products.csv`  | Product details and pricing                |
| `orders.csv`    | Customer order and transaction information |

### Dataset Columns

**Customers**

* `customer_id`
* `customer_name`
* `email`
* `city`
* `state`

**Products**

* `product_id`
* `product_name`
* `category`
* `price`

**Orders**

* `order_id`
* `customer_id`
* `product_id`
* `quantity`
* `order_date`

---

## 🏗️ Project Architecture

```text
Raw CSV Data
     ↓
Data Extraction
     ↓
Data Quality Validation
     ↓
Data Cleaning
     ↓
Data Transformation
     ↓
Processed CSV Data
     ↓
SQLite Database
     ↓
SQL Analytics
     ↓
Streamlit Dashboard
```

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **SQL**
* **SQLite**
* **Streamlit**
* **Git**
* **GitHub**

---

## 🔄 ETL Pipeline

### 1. Extract

The pipeline reads customer, product, and order data from CSV files using Pandas.

### 2. Validate

Data quality checks are performed for:

* Missing values
* Duplicate records
* Invalid product prices
* Invalid order quantities

### 3. Clean

The pipeline:

* Removes duplicate records
* Handles missing customer and product values
* Handles missing order quantities

### 4. Transform

Order data is transformed by calculating:

```text
total_amount = quantity × price
```

The transformed datasets are then saved into the `processed_data/` directory.

### 5. Load

The processed data is loaded into a **SQLite database** containing:

* `customers`
* `products`
* `orders`

---

## 🗄️ Data Model

```text
Customers
    │
    │ customer_id
    ↓
Orders
    │
    │ product_id
    ↓
Products
```

This relational structure enables customer, order, and product-level analysis.

---

## 📊 SQL Analytics

The project includes SQL queries for business analysis such as:

* Total revenue
* Average order value
* Top-selling products
* Revenue by product category
* Customer purchasing behavior
* Daily sales trends
* State-wise revenue
* Order-level analysis

SQL queries are available in:

```text
sql/analytics_queries.sql
```

---

## 📈 Streamlit Dashboard

An interactive **Streamlit dashboard** was developed to visualize key business metrics and sales insights.

The dashboard provides:

* Customer count
* Order count
* Products sold
* Total revenue
* Average order value
* Revenue by category
* Top-selling products
* Daily revenue
* Revenue by state
* Order details

Dashboard application:

```text
dashboard/app.py
```

### Run the Dashboard

```bash
python -m streamlit run dashboard/app.py
```

---

## 📁 Project Structure

```text
Ecommerce-Data-Engineering-Pipeline/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   └── orders.csv
│
├── dashboard/
│   └── app.py
│
├── processed_data/
│   ├── customers_processed.csv
│   ├── products_processed.csv
│   └── orders_processed.csv
│
├── sql/
│   └── analytics_queries.sql
│
├── src/
│   └── etl_pipeline.py
│
├── database.py
├── README.md
└── .gitignore
```

---

## 🔐 Data Quality

The pipeline checks for the following data quality issues during processing.

The pipeline checks:

* Missing values
* Duplicate records
* Invalid prices
* Invalid quantities

Pipeline logs are generated automatically when the ETL pipeline runs and are written to:

```text
logs/etl_pipeline.log
```

---

## 🚀 Future Enhancements

Future improvements may include:

* Apache Spark implementation
* Bronze, Silver, and Gold data layers
* Delta Lake integration
* Databricks implementation
* Databricks Workflows automation
* Advanced data quality monitoring
* Additional business dashboards

---

## 👨‍💻 Author

**Pradipta Kumar Prusty**

BCA Student | Data Engineering Enthusiast

### Skills

`Python` `Pandas` `SQL` `SQLite` `Streamlit` `Git` `GitHub`

---

## ⭐ Project Status

**✅ Core Pipeline Completed**

The project currently includes a functional Python ETL pipeline, data validation, SQLite database integration, SQL analytics, and an interactive Streamlit dashboard.

---

## 🔗 GitHub

[View the complete project on GitHub](https://github.com/pradiptakumarprusty/Ecommerce-Data-Engineering-Pipeline)
