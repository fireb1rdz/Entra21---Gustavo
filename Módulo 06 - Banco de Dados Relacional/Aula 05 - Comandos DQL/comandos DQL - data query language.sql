-- Selecionando colunas em especifico
SELECT name, age FROM employees;

-- Definindo um limite para a consulta
SELECT * FROM employees LIMIT 5;

-- Definindo um início para a consulta
SELECT * FROM employees OFFSET 3;

-- Selecionando os dados com condições
SELECT * FROM employees WHERE age > 30;

-- Between - Intervalo de valores
SELECT * FROM employees WHERE age BETWEEN 20 and 25;

-- Casting -> Conversão de tipo de dado
SELECT * FROM employees WHERE salary BETWEEN 'RS 3000' AND 'R$ 7000';

SELECT * FROM employees WHERE CAST(salary AS numeric) BETWEEN 3000 AND 7000;

SELECT * FROM employees WHERE salary::numeric BETWEEN 3000 and 7000;

-- Operador IN
SELECT * FROM employees WHERE age in (27, 29, 41)

--  Operador LIKE
SELECT * FROM employees WHERE name LIKE '%Ig%' -- Case-sensitive, considera um ou mais caracteres antes e depois
SELECT * FROM employees WHERE name ILIKE '%Ig%' -- Não é case-sensitive, considera um ou mais caracteres antes e depois
SELECT * FROM employees WHERE name LIKE 'Ig__' -- Case sensitive, considera a quantidade de caracteres igual a quantidade de _

-- INNER JOIN

SELECT employees.name, departments.name
FROM employees
INNER JOIN departments
ON employees.department_id = departments.id;

-- Definindo apelidos para as colunas

SELECT employees.name "Nome do funcionário", departments.name "Nome do departamento"
FROM employees
INNER JOIN departments
ON employees.department_id = departments.id;

-- Definindo apelidos para as tabelas

SELECT e.name "Nome do funcionário", d.name "Nome do departamento"
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id;

-- LEFT JOIN

SELECT e.name funcionário, d.name departamento
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id;

--  RIGHT JOIN

SELECT e.name funcionário, d.name departamento
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.id;

-- FULL JOIN

SELECT e.name funcionário, d.name departamento
FROM employees e
FULL JOIN departments d
ON e.department_id = d.id;

-- Funções agregadoras
-- COUNT - Conta as ocorrências
SELECT COUNT (*) FROM employees;

SELECT COUNT (*) FROM employees WHERE salary::numeric > 3000;

--  MAX - Maior valor
SELECT MAX(salary) FROM employees

--  MIN - Menor valor
SELECT MAX(salary) FROM employees

-- SUM - Soma dos valores
SELECT SUM(salary) FROM employees

-- AVG - Soma dos valores
SELECT AVG(salary::numeric) FROM employees

-- ROUND - Arredondar casas decimais
SELECT ROUND(AVG(salary::numeric),2) FROM employees

--  GROUP BY - Agrupar colunas
SELECT department_id "ID do departamento", COUNT(*) "Quantidade de funcionários"
FROM employees
GROUP BY 1;

-- COALESCE - Verifica se a coluna possui valor, caso não possuir, mostra um valor padrão
--  GROUP BY - Agrupar colunas
SELECT 
	COALESCE(department_id::text, 'Funcionarios sem departamento') "ID do departamento", 
	COUNT(*) "Quantidade de funcionários"
FROM employees
GROUP BY 1;

-- Com LEFT JOIN
-- COALESCE - Verifica se a coluna possui valor, caso não possuir, mostra um valor padrão
--  GROUP BY - Agrupar colunas
SELECT 
	COALESCE(d.name, 'Funcionarios sem departamento') "ID do departamento", 
	COUNT(*) "Quantidade de funcionários"
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.id
GROUP BY 1;

--  DISTINCT -> Remover as duplicatas da consulta
SELECT DISTINCT(age) FROM employees;

-- ORDER BY - Ordenar uma ou mais colunas (ASC | DESC)
SELECT DISTINCT(age) FROM employees ORDER BY 1;

-- HAVING - Filtrar por uma função agregadora
SELECT
	department_id "ID do departamento",
	COUNT(*) "Quantidade de funcionários"
FROM employees
GROUP BY 1
HAVING COUNT (*) > 3;

-- HAVING usando INNER JOIN
SELECT
	d.name "Departamento",
	COUNT(*) "Quantidade de funcionários"
FROM employees e
INNER JOIN departments d
ON e.department_id = d.id
GROUP BY 1
HAVING COUNT(department_id) > 3;

	