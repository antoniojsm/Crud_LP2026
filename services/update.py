import sqlite3

def update(id:int, info:dict):
    connect = sqlite3.connect("./db/database.db")
    cursor = connect.cursor()

    # usa if ternario para adicionar no comando caso exista algo inserido no campo
    sql_nome = f"'{info["nome"]}'" if info['nome'] != "" else "nome"
    sql_fabri = f"'{info['fabricante']}'" if info["fabricante"] != "" else "fabricante"
    sql_estoque = f"'{info['estoque']}'" if info["estoque"] != "" else "estoque"
    sql_valor = f"'{info['valor']}'" if info["valor"] != "" else "valor"

    sql_update = f"""
        UPDATE produtos
        SET nome = {sql_nome}, fabricante = {sql_fabri}, estoque = {sql_estoque}, valor = {sql_valor}
        WHERE id = {id}
    """
    cursor.execute(sql_update)

    connect.commit()
    connect.close()