from database.conexao import conectar

def recuperar_carrinho(usuario:str)->list:
    conexao,cursor = conectar()
    cursor.execute(""" 
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
        WHERE carrinhos.usuario = %s;
""",(usuario,))
    
    resultado = cursor.fetchall()
    conexao.close()
    return resultado

def inserir_item(usuario,cod_item,quantidade=1):
    conexao, cursor = conectar()
    cursor.execute("""
                    SELECT cod_carrinho from carrinhos
                    WHERE usuario = %s
                    AND finalizado = 0
                    limit 1;
                   """,[usuario])
    
    resultado_carrinho = cursor.fetchone()

    if resultado_carrinho:
        codigo_carrinho = resultado_carrinho["cod_carrinho"]
    else:
        cursor.execute("""
                    INSERT INTO carrinhos (usuario)
                    VALUES (%s);
                   """,[usuario])
        
        codigo_carrinho = cursor.lastrowid()

    conexao.close()