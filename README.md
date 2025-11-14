
# 📦 E-Commerce Data Pipeline (CSV → SQLite → SQL Summary)

This project demonstrates a complete mini data engineering workflow:

* Creating synthetic e-commerce data in CSV format
* Ingesting CSV data into a SQLite database using Python
* Running SQL queries to join multiple tables
* Producing a consolidated order summary
* Managing code using Git & GitHub

This is similar to real-world data ingestion tasks used in technical assessments.

---

## 📁 Folder Structure

```
cursor-ecom-exercise/
├── customers.csv
├── categories.csv
├── products.csv
├── orders.csv
├── order_items.csv
│
├── ingest_to_sqlite.py
├── order_summary.sql
├── run_query.py
│
└── ecom.db
```

---

## 🗂️ CSV Datasets

Five CSV files are included:

### 1. `customers.csv`

Customer information (name, email, city, signup date).

### 2. `categories.csv`

Product categories.

### 3. `products.csv`

Product details and category mapping.

### 4. `orders.csv`

Order-level information (customer, date, status, total).

### 5. `order_items.csv`

Line items inside each order.

These datasets simulate a simplified e-commerce application.

---

## 🛠️ Python Ingestion (CSV → SQLite)

`ingest_to_sqlite.py`:

* Reads all CSV files using pandas
* Creates tables in a SQLite database (`ecom.db`)
* Inserts the CSV data into tables
* Prints row counts for verification

### ▶️ Run the ingestion script

```
python ingest_to_sqlite.py
```

Expected output:

```
customers: 5 rows inserted.
categories: 5 rows inserted.
products: 6 rows inserted.
orders: 4 rows inserted.
order_items: 5 rows inserted.
Database created successfully → ecom.db
```

---

## 📊 SQL Query (Order Summary)

`order_summary.sql` contains a SQL query that:

* Joins orders, customers, products, categories, and order_items
* Computes totals and metrics:

  * Number of items
  * Number of distinct products
  * Calculated subtotal
  * Total order amount
  * Top category in each order
* Produces a consolidated order summary

### ▶️ Run the SQL using Python

```
python run_query.py
```

### ✔️ Example Output

```
Order Summary:

(1, '2025-01-05', 'Rahul Patel', 'Hyderabad', 2, 2, 2098.0, 2098.0, 'Electronics')
(2, '2025-01-10', 'Aisha Khan', 'Bangalore', 1, 1, 399.0, 399.0, 'Fashion')
(3, '2025-01-11', 'Sneha Iyer', 'Mumbai', 2, 1, 1598.0, 1798.0, 'Groceries')
```

---

## 🚀 Tech Stack Used

* Python
* Pandas
* SQLite
* SQL Joins + Aggregations
* Git / GitHub

---

## 🔁 How to Reproduce

1. Download or clone the repository.
2. Install required package:

```
pip install pandas
```

3. Run the ingestion script:

```
python ingest_to_sqlite.py
```

4. Run the SQL execution script:

```
python run_query.py
```

---

## 📌 Purpose of This Project

This project demonstrates:

* Working with CSV datasets
* Designing normalized database tables
* Ingesting data into SQLite
* Writing SQL queries involving joins & aggregations
* Creating a clean, reproducible data pipeline

Useful for Data Engineering, Analytics, and coding assessments.

---


