from database.conexao import conectar

def recuperar_carrinho(usuario:str)->list:
    conexao,cursor = conectar()
    cursor.execute(""" 
    SELECT * from itens_carrinho
""")
    
    resultado = cursor.fetchall()
    conexao.close()
    return resultado