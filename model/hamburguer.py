from database.conexao import conectar



def recuperar_hamburguers():
    conexao,cursor = conectar()

     
    cursor.execute('''SELECT hamburguers.codigo,hamburguers.produto,hamburguers.descricao,hamburguers.preco,hamburguers.destaque,hamburguers.foto,hamburguers.disponibilidade 
                   FROM hamburguers
                   WHERE hamburguers.disponibilidade = 1;''')

    hamburguers=cursor.fetchall()


    conexao.close()

    return hamburguers

def recuperar_hamburguers_destaques():
    conexao,cursor = conectar()

     
    cursor.execute('''SELECT hamburguers.codigo,hamburguers.produto,hamburguers.descricao,hamburguers.preco,hamburguers.destaque,hamburguers.foto,hamburguers.disponibilidade 
                   FROM hamburguers
                   WHERE hamburguers.destaque = 1 and hamburguers.disponibilidade = 1 
                   ;''')

    hamburguers=cursor.fetchall()


    conexao.close()
    return hamburguers

def recuperar_produto(codigo: int):
    conexao,cursor = conectar()

     
    cursor.execute('''SELECT hamburguers.codigo,hamburguers.produto,hamburguers.descricao,hamburguers.preco,hamburguers.destaque,hamburguers.foto,hamburguers.disponibilidade 
        FROM hamburguers
        WHERE hamburguers.codigo = %s; 
                   ;''',(codigo, ))

    hamburguers=cursor.fetchone()


    conexao.close()
    return hamburguers

def cadastrar(nome, senha):
    conexao,cursor = conectar()

     
    cursor.execute('''INSERT INTO Devburguer.usuarios (nome,senha)
    VALUES
    (%s,%s);''',(nome, senha))

    conexao.commit()


    conexao.close()
    