CREATE DATABASE IF NOT EXISTS Devburguer;

USE Devburguer;

CREATE TABLE IF NOT EXISTS hamburguers (
 codigo VARCHAR(30) auto_increment PRIMARY KEY,
 produto VARCHAR(100),
 descricao VARCHAR(1000),
 preco DOUBLE,
 destaque BOOLEAN,
 foto VARCHAR(1000),
 disponibilidade BOOLEAN
);


