--
-- File generated with SQLiteStudio v3.3.3 on seg out 4 11:42:29 2021
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: empresa
CREATE TABLE empresa (
    id              INTEGER       PRIMARY KEY AUTOINCREMENT,
    nome            VARCHAR (255) NOT NULL,
    cnpj            INTEGER (14)  NOT NULL,
    nome_imunizante VARCHAR (100) NOT NULL
);


-- Table: imunizante
CREATE TABLE imunizante (
    id         INTEGER      PRIMARY KEY AUTOINCREMENT,
    lote       INTEGER (20) NOT NULL,
    id_estado  INTEGER (11) NOT NULL
                            REFERENCES uf (id),
    id_empresa INTEGER (11) NOT NULL
                            REFERENCES empresa (id) 
);


-- Table: pessoa
CREATE TABLE pessoa (
    id            INTEGER       NOT NULL
                                PRIMARY KEY AUTOINCREMENT,
    nome          VARCHAR (100) NOT NULL,
    cpf           VARCHAR (11)  NOT NULL,
    doses         INTERGER (1),
    id_imunizante VARCHAR (11)  REFERENCES imunizante (id) 
);


-- Table: uf
CREATE TABLE uf (
    id   INTEGER      NOT NULL
                      PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR (75) DEFAULT NULL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
