-- 3 Usuario(s)
-- 3 Materia(s)
-- 7 Prova(s) -> 3 Questao(s)
-- 18 Questao(s) -> 4 Alternativa(s)

USE Escola;

INSERT INTO Configuracao(
	ocultar_questoes_outros_usuario,
	exibe_material_inativa,
    exibe_alternativa
)
VALUES
	(false, true, true),
	(true, true, true),
	(false, false, true)
;

INSERT INTO Usuario(
	id_config,
    email,
    nome_completo,
    senha,
    administrador
)
VALUES
	(1, "artur@gmail.com", "Artur Regadas", "1234", true),
	(2, "davi@gmail.com", "Davi Ribeiro", false),
	(3, "gabriel@gmail.com", "Gabriel Nascimento",false)
;

INSERT INTO Prova(
		id_usuario,
        descricao,
        tema
)
VALUES
	(1, "Uma prova muito complicada", "Diversidade"),
    (1, "Uma prova sobre Dinheiro", "Economia"),
    (3, "Uma prova facil", "Banco de dados"),
    (2, "Uma prova da Claeudete", "Artes"),
    (2, "Uma prova de numeros", "Matematica"),
    (3, "Uma prova sem nocao", "Web"),
    (2, "Uma prova", "Amazonia")
;
    
    
