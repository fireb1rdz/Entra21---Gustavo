CREATE TABLE IF NOT EXISTS public.departamentos (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(256) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS public.cargos (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(256) NOT NULL,
	departamento_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.funcionarios (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(256) NOT NULL,
	cpf VARCHAR(11) NOT NULL UNIQUE,
	data_nascimento DATE NOT NULL,
	data_inicio DATE NOT NULL,
	cargo_id INT NOT NULL,
	departamento_id INT NOT NULL,
	plano_saude_id INT,
	fundo_pensao_id INT, 
	ajuda_custo_id INT,
	vale_refeicao_id INT
);

CREATE TABLE IF NOT EXISTS public.candidatos (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(256) NOT NULL,
	educacao TEXT,
	vaga_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.candidaturas (
	id SERIAL PRIMARY KEY,
	status VARCHAR(30) NOT NULL,
	vaga_id INT NOT NULL,
	candidato_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.entrevistas (
	id SERIAL PRIMARY KEY,
	data TIMESTAMP NOT NULL,
	anotacoes TEXT NOT NULL,
	candidatura_id INT NOT NULL,
	entrevistador_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.vagas (
	id SERIAL PRIMARY KEY,
	status VARCHAR(50) NOT NULL,
	cargo_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.enderecos (
	id SERIAL PRIMARY KEY,
	cidade VARCHAR(256) NOT NULL,
	bairro VARCHAR(256) NOT NULL,
	rua VARCHAR(256) NOT NULL,
	numero VARCHAR(8),
	funcionario_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.historicos (
	id SERIAL PRIMARY KEY,
	empresa VARCHAR(256),
	cargo VARCHAR(256),
	departamento VARCHAR(256),
	funcionario_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.ausencias (
	id SERIAL PRIMARY KEY,
	tipo_ausencia TEXT NOT NULL,
	data_inicio TIMESTAMP NOT NULL,
	data_termino TIMESTAMP,
	funcionario_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.folhas_pagamento (
	id SERIAL PRIMARY KEY,
	mes_ano_vigente TIMESTAMP NOT NULL,
	salario_base NUMERIC NOT NULL,
	horas_trabalhadas REAL NOT NULL,
	bonus REAL NOT NULL,
	deducoes_fiscais REAL NOT NULL,
	contr_previdenciarias REAL NOT NULL,
	status VARCHAR(30) NOT NULL,
	funcionario_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.pagamentos (
	id SERIAL PRIMARY KEY,
	data_pagamento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	valor_pagamento NUMERIC NOT NULL,
	folha_pagamento_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.objetivos_planos (
	id SERIAL PRIMARY KEY,
	data_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	objetivo_carreira TEXT,
	plano_desenvolvimento TEXT,
	funcionario_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.pdi (
	id SERIAL PRIMARY KEY,
	requisitos TEXT NOT NULL,
	plano_desenvolvimento_id TEXT
);

CREATE TABLE IF NOT EXISTS public.avaliacoes_desempenho (
	id SERIAL PRIMARY KEY,
	data_avaliacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	valor_avaliacao NUMERIC NOT NULL,
	feedback_supervisor TEXT,
	funcionario_id INT NOT NULL,
	supervisor_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.planos_saude (
	id SERIAL PRIMARY KEY,
	valor_base NUMERIC NOT NULL,
	funcionario_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.fundos_pensao (
	id SERIAL PRIMARY KEY,
	valor_base NUMERIC NOT NULL,
	funcionario_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.ajudas_custo (
	id SERIAL PRIMARY KEY,
	valor_base NUMERIC NOT NULL,
	funcionario_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.vales_refeicao (
	id SERIAL PRIMARY KEY,
	valor_base NUMERIC NOT NULL,
	funcionario_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.cursos (
	id SERIAL PRIMARY KEY,
	nome_curso VARCHAR(256) NOT NULL,
	disponivel BOOLEAN NOT NULL
);

CREATE TABLE IF NOT EXISTS public.inscricoes (
	id SERIAL PRIMARY KEY,
	data_inscricao TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	funcionario_id INT NOT NULL,
	curso_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.cursos_pdis (
	curso_id INT,
	pdi_id INT,
	PRIMARY KEY (curso_id, pdi_id)
);

CREATE TABLE IF NOT EXISTS public.entrevistas_funcionarios (
	entrevistador_id INT,
	funcionario_id INT,
	PRIMARY KEY (entrevistador_id, funcionario_id)
);

-- Adicionando as chaves-estrangeiras

ALTER TABLE IF EXISTS public.cargos
ADD FOREIGN KEY (departamento_id)
REFERENCES public.departamentos (id)
ON UPDATE RESTRICT
ON DELETE RESTRICT;

ALTER TABLE IF EXISTS public.planos_saude
ADD FOREIGN KEY (funcionario_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.funcionarios
ADD FOREIGN KEY (cargo_id)
REFERENCES public.cargos (id)
ON UPDATE CASCADE
ON DELETE SET NULL;

ALTER TABLE IF EXISTS public.funcionarios
ADD FOREIGN KEY (departamento_id)
REFERENCES public.departamentos (id)
ON UPDATE CASCADE
ON DELETE SET NULL;

ALTER TABLE IF EXISTS public.funcionarios
ADD FOREIGN KEY (fundo_pensao_id)
REFERENCES public.fundos_pensao (id)
ON UPDATE CASCADE
ON DELETE SET NULL;

ALTER TABLE IF EXISTS public.funcionarios
ADD FOREIGN KEY (ajuda_custo_id)
REFERENCES public.ajudas_custo (id)
ON UPDATE CASCADE
ON DELETE SET NULL;

ALTER TABLE IF EXISTS public.funcionarios
ADD FOREIGN KEY (vale_refeicao_id)
REFERENCES public.vales_refeicao (id)
ON UPDATE CASCADE
ON DELETE SET NULL;

ALTER TABLE IF EXISTS public.funcionarios
ADD FOREIGN KEY (plano_saude_id)
REFERENCES public.planos_saude (id)
ON UPDATE CASCADE
ON DELETE SET NULL;

ALTER TABLE IF EXISTS public.candidatos
ADD FOREIGN KEY (vaga_id)
REFERENCES public.vagas (id)
ON UPDATE CASCADE
ON DELETE SET NULL;

ALTER TABLE IF EXISTS public.vagas
ADD FOREIGN KEY (cargo_id)
REFERENCES public.cargos (id)
ON UPDATE CASCADE
ON DELETE RESTRICT;

ALTER TABLE IF EXISTS public.enderecos
ADD FOREIGN KEY (funcionario_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE SET NULL;

ALTER TABLE IF EXISTS public.historicos
ADD FOREIGN KEY (funcionario_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.folhas_pagamento
ADD FOREIGN KEY (funcionario_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.objetivos_planos
ADD FOREIGN KEY (funcionario_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.fundos_pensao
ADD FOREIGN KEY (funcionario_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.ajudas_custo
ADD FOREIGN KEY (funcionario_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.vales_refeicao
ADD FOREIGN KEY (funcionario_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.ausencias
ADD FOREIGN KEY (funcionario_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.avaliacoes_desempenho
ADD FOREIGN KEY (funcionario_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.avaliacoes_desempenho
ADD FOREIGN KEY (supervisor_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.candidaturas
ADD FOREIGN KEY (vaga_id)
REFERENCES public.vagas (id)
ON UPDATE CASCADE
ON DELETE RESTRICT;

ALTER TABLE IF EXISTS public.candidaturas
ADD FOREIGN KEY (candidato_id)
REFERENCES public.candidatos (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.pagamentos
ADD FOREIGN KEY (folha_pagamento_id)
REFERENCES public.folhas_pagamento (id)
ON UPDATE CASCADE
ON DELETE RESTRICT;

ALTER TABLE IF EXISTS public.pdi
ADD FOREIGN KEY (plano_desenvolvimento_id)
REFERENCES public.objetivos_planos (plano_desenvolvimento)
ON UPDATE NO ACTION
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.entrevistas
ADD FOREIGN KEY (candidatura_id)
REFERENCES public.candidaturas (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.entrevistas
ADD FOREIGN KEY (entrevistador_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE RESTRICT;

ALTER TABLE IF EXISTS public.inscricoes
ADD FOREIGN KEY (funcionario_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.inscricoes
ADD FOREIGN KEY (curso_id)
REFERENCES public.cursos (id)
ON UPDATE CASCADE
ON DELETE RESTRICT;

ALTER TABLE IF EXISTS public.cursos_pdis
ADD FOREIGN KEY (curso_id)
REFERENCES public.cursos (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.cursos_pdis
ADD FOREIGN KEY (pdi_id)
REFERENCES public.pdi (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.entrevistas_funcionarios
ADD FOREIGN KEY (entrevista_id)
REFERENCES public.entrevistas (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.entrevistas_funcionarios
ADD FOREIGN KEY (entrevistador_id)
REFERENCES public.funcionarios (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;
