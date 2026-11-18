import sqlite3

def update(id:int, info:dict):
    connect = sqlite3.connect("./db/database.db")
    cursor = connect.cursor()

    sql_update = f"""
        UPDATE produtos
        SET nome = '{info["nome"]}', fabricante = '{info["fabricante"]}', estoque = {info["estoque"]}, valor = {info["valor"]}
    """
    cursor.execute(sql_update)

    connect.commit()
    connect.close()