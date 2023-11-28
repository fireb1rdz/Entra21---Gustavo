-- Exercícios 2
-- A)
SELECT SUM(quantity_in_stock) "Quantidade total em estoque"
FROM products;

-- B)
SELECT ROUND(AVG(price::numeric), 2)
FROM products;

-- C)
SELECT product "Produto", price "Preço"
FROM products
ORDER BY 2 DESC
LIMIT 1;

-- D)
SELECT product "Produto", price "Preço"
FROM products
ORDER BY 2
LIMIT 1;

-- E)
SELECT product "Produto", price * quantity_in_stock "Valor total do estoque" 
FROM products;

-- F)
SELECT SUM(contagem) "Soma total"
FROM (
	SELECT COUNT(*) "contagem"
	FROM products
	GROUP BY quantity_in_stock
	HAVING quantity_in_stock < 20
);

-- G)
SELECT product "Produto", price * quantity_in_stock "Valor total do estoque"
FROM products
ORDER BY 2 DESC
LIMIT 1;