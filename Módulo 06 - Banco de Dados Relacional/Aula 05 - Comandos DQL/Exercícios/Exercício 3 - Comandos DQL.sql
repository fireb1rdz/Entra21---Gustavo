-- Exercício 3
-- A)
SELECT
	e.name "Colaborador",
	e.role "Cargo",
	d.name "Departamento"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;

-- B)
SELECT
	e.name "Colaborador",
	e.role "Cargo",
	e.salary "Salário"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE d.name = 'Vendas';

-- C)
SELECT
	e.name "Colaborador",
	e.role "Cargo",
	e.salary "Salário"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
WHERE salary::numeric > 3500 AND d.name = 'Vendas';

-- D)
SELECT
	e.name "Colaborador",
	e.role "Cargo",
	e.salary "Salário",
	STRING_AGG(p.name, ', ') Projetos
FROM employees e
INNER JOIN departments d 
ON e.department_id = d.id
INNER JOIN projects p
ON p.department_id = d.id
GROUP BY e.id;

-- E)
SELECT 
	SUM(salary) "Gasto total com salários"
FROM employees;

-- F)
SELECT
	d.name "Departamento",
	SUM(e.salary) "Soma dos salários"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.name;

-- G)
SELECT
	d.name "Departamento",
	MAX(e.salary) "Maior salário"
FROM employees e
INNER JOIN departments d ON e.department_id = d.id
GROUP BY d.name;



