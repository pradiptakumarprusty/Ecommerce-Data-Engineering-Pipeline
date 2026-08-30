```sql
-- E-Commerce Data Engineering Pipeline
-- SQL Analysis & Business Insights


-- 1. View all customers
SELECT *
FROM customers;


-- 2. View all products
SELECT *
FROM products;


-- 3. View all orders
SELECT *
FROM orders;


-- 4. Count total customers
SELECT COUNT(*) AS total_customers
FROM customers;


-- 5. Count total products
SELECT COUNT(*) AS total_products
FROM products;


-- 6. Count total orders
SELECT COUNT(*) AS total_orders
FROM orders;


-- 7. Calculate total revenue
SELECT
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id;


-- 8. Calculate revenue by product
SELECT
    p.product_id,
    p.product_name,
    SUM(o.quantity) AS total_quantity_sold,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY
    p.product_id,
    p.product_name
ORDER BY total_revenue DESC;


-- 9. Find top-selling products
SELECT
    p.product_name,
    SUM(o.quantity) AS total_quantity_sold
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC;


-- 10. Customer-wise order analysis
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.quantity * p.price) AS total_spending
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
JOIN products p
    ON o.product_id = p.product_id
GROUP BY
    c.customer_id,
    c.customer_name
ORDER BY total_spending DESC;


-- 11. Revenue by category
SELECT
    p.category,
    SUM(o.quantity * p.price) AS category_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY category_revenue DESC;


-- 12. Average order value
SELECT
    AVG(o.quantity * p.price) AS average_order_value
FROM orders o
JOIN products p
    ON o.product_id = p.product_id;


-- 13. Orders by customer state
SELECT
    c.state,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.state
ORDER BY total_orders DESC;


-- 14. Monthly revenue
SELECT
    EXTRACT(YEAR FROM o.order_date) AS order_year,
    EXTRACT(MONTH FROM o.order_date) AS order_month,
    SUM(o.quantity * p.price) AS monthly_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY
    EXTRACT(YEAR FROM o.order_date),
    EXTRACT(MONTH FROM o.order_date)
ORDER BY order_year, order_month;
```
