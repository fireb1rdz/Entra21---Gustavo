SELECT * FROM funcionarios
ORDER BY id ASC;

UPDATE funcionarios SET nome = 'Pedro Álvares' WHERE id = 18;
UPDATE funcionarios SET nome = 'Anderson Silva' WHERE id = 26;
UPDATE funcionarios SET nome = 'Gustavo Paganelli' WHERE id = 64;
UPDATE funcionarios SET nome = 'Nelson Paganelli' WHERE id = 45;
UPDATE funcionarios SET nome = 'Marcia Arendt' WHERE id = 39;

SELECT * FROM ajudas_custo
ORDER BY id ASC;

UPDATE ajudas_custo SET valor_base = 200 WHERE id = 1;
UPDATE ajudas_custo SET valor_base = 121 WHERE id = 3;
UPDATE ajudas_custo SET valor_base = 1500 WHERE id = 5;
UPDATE ajudas_custo SET valor_base = 98 WHERE id = 4;
UPDATE ajudas_custo SET valor_base = 10 WHERE id = 10;