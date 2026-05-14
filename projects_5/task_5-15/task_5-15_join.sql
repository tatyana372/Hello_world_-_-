SELECT * FROM products WHERE category IN ('Продукты', 'Книги');
SELECT category, COUNT(*) AS product_count FROM products GROUP BY category ORDER BY product_count DESC;
UPDATE prices 
SET price = price * 1.05 
WHERE product_id <= 5 AND price < 10000;
SELECT name AS "Название товара", category AS "Категория" FROM products;