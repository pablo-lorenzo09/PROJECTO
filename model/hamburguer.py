from database.conexao import conectar



def recuperar_hamburguers():
    conexao,cursor = conectar()

     
    cursor.execute('''SELECT hamburguers.codigo,hamburguers.produto,hamburguers.descricao,hamburguers.preco,hamburguers.destaque,hamburguers.foto,hamburguers.disponibilidade 
                   FROM hamburguers;''')

    hamburguers=cursor.fetchall()


    conexao.close()

    return hamburguers