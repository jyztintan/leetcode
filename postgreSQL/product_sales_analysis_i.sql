SELECT p.product_name, s.year, s.price
FROM sales s, product p
WHERE s.product_id = p.product_id