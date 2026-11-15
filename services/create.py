import sqlite3

def cadastrar(prod:dict):
    # conexão com o banco de dados
    conect = sqlite3.connect("./db/database.db")
    cursor = conect.cursor()

    # comando sql novo registro
    # nome, fabricante, estoque, valor
    sql = f"""
        INSERT INTO produtos (nome, fabricante, estoque, valor) VALUES ('{prod["nome"]}', '{prod["fabricante"]}', {prod["estoque"]}, {prod["valor"]})
    """
    cursor.execute(sql)

    # salva e fecha conexão
    conect.commit()
    conect.close()