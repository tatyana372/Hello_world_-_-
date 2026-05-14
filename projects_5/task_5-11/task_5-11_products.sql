SELECT * FROM products WHERE category = 'Электроника';
SELECT * FROM products WHERE category = 'Одежда' AND name ILIKE '%женские%';
SELECT * FROM products WHERE category IN ('Продукты', 'Книги');
SELECT * FROM products WHERE category <> 'Бытовая техника';
SELECT * FROM products WHERE category IN ('Электроника', 'Одежда', 'Книги');
SELECT * FROM products WHERE (category = 'Электроника' AND name ILIKE '%Samsung%') OR category = 'Бытовая техника';
SELECT * FROM products WHERE (category IN ('Электроника', 'Одежда', 'Бытовая техника') AND id BETWEEN 1 AND 15 AND name NOT ILIKE '%Samsung%') OR category = 'Книги';