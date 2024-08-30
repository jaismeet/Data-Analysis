-- Task: Retrieve products that are either in the 'Electronics' category or have a price less than 70,000.
use ecommerce;
SELECT * FROM Product
WHERE category = 'Electronics' OR price < 70000;


