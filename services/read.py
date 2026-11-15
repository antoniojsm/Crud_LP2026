import sqlite3
def read():    
    #caminho banco de dados
    conect = sqlite3.connect("./db/database.db")
    cursor = conect.cursor()
    # consulta sql para exibir todos os produtos
    cursor.execute("SELECT * FROM produtos")
    produtos = cursor.fetchall()

    conect.close()
    
    return produtos