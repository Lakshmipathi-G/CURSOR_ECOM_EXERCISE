import sqlite3

conn = sqlite3.connect("ecom.db")
cur = conn.cursor()

sql = open("order_summary.sql").read()
rows = cur.execute(sql).fetchall()

print("Order Summary:\n")
for row in rows:
    print(row)

conn.close()
