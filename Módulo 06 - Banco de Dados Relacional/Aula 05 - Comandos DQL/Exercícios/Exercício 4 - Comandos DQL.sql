-- Exercício 4
-- A)
SELECT 
	f.name,
	c.name
FROM foods f
INNER JOIN categories c
ON f.category_id = c.id

-- B)
SELECT
	c.name,
	SUM(n.calories)
FROM foods f
INNER JOIN categories c
ON f.category_id = c.id
INNER JOIN nutritional_information n
ON n.food_id = f.id
GROUP BY c.name

-- C)
SELECT 
	d.name "Dietas"
FROM foods f
INNER JOIN diets_foods df
ON f.id = df.food_id
INNER JOIN nutritional_information n
ON f.id = n.food_id
INNER JOIN diets d
ON df.diet_id = d.id
WHERE n.calories > 500

-- D)
SELECT
	c.name,
	ROUND(AVG(n.calories),2)
FROM nutritional_information n
INNER JOIN foods f
ON f.id = n.food_id
INNER JOIN categories c
ON f.category_id = c.id
GROUP BY 1;

-- E)
SELECT 
	f.name,
	n.fats
FROM foods f
INNER JOIN nutritional_information n
ON f.id = n.food_id
WHERE n.fats > (
	SELECT AVG(fats)
	FROM nutritional_information
)

