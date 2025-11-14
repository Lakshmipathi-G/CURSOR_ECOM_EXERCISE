WITH item_totals AS (
  SELECT
    oi.order_id,
    SUM(oi.quantity * oi.unit_price) AS subtotal,
    SUM(oi.quantity) AS num_items,
    COUNT(DISTINCT oi.product_id) AS distinct_products
  FROM order_items oi
  GROUP BY oi.order_id
),
top_cat AS (
  SELECT
    oi.order_id,
    c.category_name,
    SUM(oi.quantity) AS qty
  FROM order_items oi
  JOIN products p ON oi.product_id = p.product_id
  JOIN categories c ON p.category_id = c.category_id
  GROUP BY oi.order_id, c.category_name
)
SELECT
  o.order_id,
  o.order_date,
  c.first_name || ' ' || c.last_name AS customer_name,
  c.city,
  it.num_items,
  it.distinct_products,
  it.subtotal AS calculated_subtotal,
  o.total_amount,
  (SELECT category_name 
   FROM top_cat tc 
   WHERE tc.order_id = o.order_id 
   ORDER BY qty DESC LIMIT 1) AS top_category
FROM orders o
LEFT JOIN customers c ON c.customer_id = o.customer_id
LEFT JOIN item_totals it ON it.order_id = o.order_id
ORDER BY o.order_id ASC;
