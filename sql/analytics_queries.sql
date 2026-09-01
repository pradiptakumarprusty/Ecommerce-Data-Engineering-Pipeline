-- ============================================================
-- E-COMMERCE ANALYTICS QUERIES
-- ============================================================


-- 1. TOTAL NUMBER OF CUSTOMERS
SELECT COUNT(*) AS total_customers
FROM customers;


-- 2. TOTAL NUMBER OF PRODUCTS
SELECT COUNT(*) AS total_products
FROM products;


-- 3. TOTAL NUMBER OF ORDERS
SELECT COUNT(*) AS total_orders
FROM orders;


-- 4. TOTAL PRODUCTS SOLD
SELECT SUM(quantity) AS total_products_sold
FROM orders;


-- 5. TOTAL REVENUE
SELECT
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id;


-- 6. AVERAGE ORDER VALUE
SELECT
    AVG(o.quantity * p.price) AS average_order_value
FROM orders o
JOIN products p
    ON o.product_id = p.product_id;


-- 7. TOP-SELLING PRODUCTS BY QUANTITY
SELECT
    p.product_name,
    SUM(o.quantity) AS total_quantity_sold
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_quantity_sold DESC;


-- 8. REVENUE BY PRODUCT
SELECT
    p.product_name,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_revenue DESC;


-- 9. REVENUE BY CATEGORY
SELECT
    p.category,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;


-- 10. TOP CUSTOMERS BY SPENDING
SELECT
    c.customer_name,
    SUM(o.quantity * p.price) AS total_spending
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN products p
    ON o.product_id = p.product_id
GROUP BY c.customer_name
ORDER BY total_spending DESC;


-- 11. ORDERS BY CITY
SELECT
    c.city,
    COUNT(o.order_id) AS total_orders
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
GROUP BY c.city
ORDER BY total_orders DESC;


-- 12. DAILY REVENUE
SELECT
    o.order_date,
    SUM(o.quantity * p.price) AS daily_revenue
FROM orders o
JOIN products p
    ON o.product_id = p.product_id
GROUP BY o.order_date
ORDER BY o.order_date;


-- 13. SALES BY STATE
SELECT
    c.state,
    SUM(o.quantity * p.price) AS total_revenue
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN products p
    ON o.product_id = p.product_id
GROUP BY c.state
ORDER BY total_revenue DESC;