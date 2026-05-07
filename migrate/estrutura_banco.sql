CREATE DATABASE IF NOT EXISTS Devburguer;

USE Devburguer;


CREATE TABLE IF NOT EXISTS hamburguers (
 codigo INTEGER(30) auto_increment PRIMARY KEY,
 produto VARCHAR(100),
 descricao VARCHAR(1000),
 preco DOUBLE,
 destaque BOOLEAN,
 foto VARCHAR(1000),
 disponibilidade BOOLEAN
);

create table if not exists usuarios (
	usuario VARCHAR(30) NOT NULL PRIMARY KEY,
	senha VARCHAR(200) NOT NULL,    
    nome VARCHAR (100) default "ANONIMO"
);


create table if not exists carrinhos (
	cod_carrinho int auto_increment primary key,
    usuario varchar(30),
    date datetime default current_timestamp(),
    finalizado bool,
    CONSTRAINT fk_carrinho_usuario FOREIGN KEY (usuario) references usuarios(usuario)
    
);

create table if not exists itens_carrinho (
    cod_item_carrinho int auto_increment primary key, 
    cod_carrinho int,
    cod_produto int,
    quantidade int default 1,
    CONSTRAINT fk_itenscarrinho_carrinhos foreign key (cod_carrinho) references carrinhos(cod_carrinho),
    constraint fk_itenscarinho_itens foreign key (cod_produto) references hamburguers(codigo)
);

SELECT carrinhos.cod_carrinho,
       carrinhos.usuario,
       carrinhos.date,
       carrinhos.finalizado,
       hamburguers.produto,
       itens_carrinho.quantidade,
       hamburguers.preco,
       hamburguers.foto
        FROM carrinhos
        INNER JOIN itens_carrinho ON carrinhos.cod_carrinho = itens_carrinho.cod_carrinho
        INNER JOIN hamburguers ON hamburguers.codigo = itens_carrinho.cod_produto
        WHERE carrinhos.usuario = "pablorei";
        



INSERT INTO DevBurguer.hamburguers(produto,descricao,preco,destaque,foto,disponibilidade)
VALUES
("Classic Dev","Pão brioche, carne suculenta e queijo derretido.",25.00,1,"https://images.pexels.com/photos/1639557/pexels-photo-1639557.jpeg?auto=compress&cs=tinysrgb&w=600",1),
("Double Stack","Dois hambúrgueres, bacon crocante e molho especial.",38.00,1,"https://images.pexels.com/photos/2983101/pexels-photo-2983101.jpeg?auto=compress&cs=tinysrgb&w=600",0),
("Veggie Script","Hambúrguer de grão de bico com salada fresca.",30.00,1,"https://images.pexels.com/photos/3219483/pexels-photo-3219483.jpeg?auto=compress&cs=tinysrgb&w=600",1),
("Java Chicken","Frango empanado crocante com alface e maionese.",28.00,1,"https://images.pexels.com/photos/12034622/pexels-photo-12034622.jpeg",1),
("Python Onion","Anéis de cebola, barbecue e queijo cheddar.",33.00,1,"https://images.pexels.com/photos/70497/pexels-photo-70497.jpeg?auto=compress&cs=tinysrgb&w=600",1),
("React Salad","Uma opção leve e reativa para o seu almoço.",27.00,1,"https://images.pexels.com/photos/1199957/pexels-photo-1199957.jpeg?auto=compress&cs=tinysrgb&w=600",1);

INSERT INTO Devburguer.usuarios (usuario,senha)
VALUES
("pablorei","melmelmelsahur");

INSERT INTO carrinhos (usuario, finalizado) 
VALUES ('pablorei', false);
INSERT INTO itens_carrinho (cod_carrinho, cod_produto, quantidade)
VALUES 
(1, 1, 2), -- 2 Classic Devs no carrinho 1
(1, 5, 1); -- 1 Python Onion no carrinho 1

select * from itens_carrinho


