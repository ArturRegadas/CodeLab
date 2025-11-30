DROP DATABASE IF EXISTS Escola;

CREATE DATABASE IF NOT EXISTS Escola 
	CHARACTER SET utf8mb4
    COLLATE utf8mb4_general_ci
    ENCRYPTION = 'N'
;

USE Escola;

CREATE TABLE IF NOT EXISTS Configuracao(
	id_configuracao INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    paginacao INT NOT NULL DEFAULT 1,
    ocultar_questoes_outros_usuario BOOL NOT NULL DEFAULT FALSE,
    exibe_material_inativa BOOL NOT NULL DEFAULT TRUE,
    exibe_alternativa BOOL NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS Usuario(
	id_usuario INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_configuracao INT NOT NULL REFERENCES Configuracao(id_configuracao), -- FOREIGN KEY
	email VARCHAR(100) NOT NULL,
    nome_completo VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    administrador BOOL NOT NULL DEFAULT FALSE,
    foto BLOB
);

CREATE TABLE IF NOT EXISTS Materia(
	id_materia INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255) NOT NULL,
    sigla CHAR(5) NOT NULL,
    curso VARCHAR(100) NOT NULL,
    inativa BOOL NOT NULL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS Prova(
	id_prova INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_materia INT NOT NULL REFERENCES Materia(id_materia),
    id_usuario INT NOT NULL REFERENCES Usuario(id_usuario),
    descricao VARCHAR(255),
    tema VARCHAR(255),
    data_prova DATETIME
);


CREATE TABLE IF NOT EXISTS Questao(
	id_questao INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_usuario INT REFERENCES Usuario(id_usuario),
    enunciado TEXT NOT NULL,
    verificada BOOL NOT NULL DEFAULT FALSE,
    imagem BLOB,
    comentarios TEXT,
    assunto VARCHAR(100),
    ano YEAR,
    banca VARCHAR(100),
    orgao VARCHAR(100),
    prova VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS Alternativa(
	id_alternativa INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    id_questao INT NOT NULL REFERENCES Questao(id_questao),
    texto VARCHAR(255) NOT NULL,
    certa BOOL NOT NULL,
    imagem BLOB
);

CREATE TABLE IF NOT EXISTS ProvaQuestao(
	id_prova INT NOT NULL REFERENCES Prova(id_prova),
	id_questao INT NOT NULL REFERENCES Questao(id_questao),
    PRIMARY KEY(id_prova, id_questao)
);

