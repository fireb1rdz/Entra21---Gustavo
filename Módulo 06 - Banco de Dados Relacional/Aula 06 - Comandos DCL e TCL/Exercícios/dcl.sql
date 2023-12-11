-- 1)
CREATE ROLE aluno WITH PASSWORD '123456'

-- 2)
GRANT SELECT ON ausencias TO aluno;

-- 3)
REVOKE SELECT ON ausencias FROM aluno;

-- 4)
GRANT INSERT, UPDATE ON ALL TABLES IN SCHEMA public;

-- 5)
DROP ROLE aluno;

-- 6)
CREATE ROLE deletar;
GRANT DELETE ON ajudas_custo TO deletar;

-- 7)
CREATE VIEW deletar_view AS
SELECT id, valor_base
FROM ajudas_custo;

GRANT SELECT ON deletar_view TO deletar;

-- 8)
GRANT SELECT ON ajudas_custo TO dba WITH GRANT OPTION;