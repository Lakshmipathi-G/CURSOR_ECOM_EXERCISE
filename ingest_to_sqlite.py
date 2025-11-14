import pandas as pd
import sqlite3

# CSV filenames
customers_fn = "customers.csv"
categories_fn = "categories.csv"
products_fn = "products.csv"
orders_fn = "orders.csv"
order_items_fn = "order_items.csv"

# Read CSVs
customers = pd.read_csv(customers_fn)
categories = pd.read_csv(categories_fn)
products = pd.read_csv(products_fn)
orders = pd.read_csv(orders_fn)
order_items = pd.read_csv(order_items_fn)

# Connect to SQLite (auto-creates file)
conn = sqlite3.connect("ecom.db")
cur = conn.cursor()

# Create tables
cur.executescript("""
DROP TABLE IF EXISTS order_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
  customer_id INTEGER PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  city TEXT,
  signup_date TEXT
);

CREATE TABLE categories (
  category_id INTEGER PRIMARY KEY,
  category_name TEXT
);

CREATE TABLE products (
  product_id INTEGER PRIMARY KEY,
  product_name TEXT,
  category_id INTEGER,
  price REAL,
  sku TEXT,
  FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  order_date TEXT,
  status TEXT,
  total_amount REAL,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
  order_item_id INTEGER PRIMARY KEY,
  order_id INTEGER,
  product_id INTEGER,
  quantity INTEGER,
  unit_price REAL,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")
conn.commit()

# Insert data using pandas
customers.to_sql("customers", conn, if_exists="append", index=False)
categories.to_sql("categories", conn, if_exists="append", index=False)
products.to_sql("products", conn, if_exists="append", index=False)
orders.to_sql("orders", conn, if_exists="append", index=False)
order_items.to_sql("order_items", conn, if_exists="append", index=False)

# Print confirmation
for t in ["customers","categories","products","orders","order_items"]:
    c = cur.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
    print(f"{t}: {c} rows inserted.")

conn.commit()
conn.close()
print("Database created successfully → ecom.db")
