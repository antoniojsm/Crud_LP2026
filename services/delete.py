import sqlite3

def delete(prod_id:int):
    # conexão com o banco de dados
    conect = sqlite3.connect("./db/database.db")
    cursor = conect.cursor()

    # comando sql para deletar registro
    sql = f"""
        DELETE FROM produtos WHERE id = {prod_id}
    """
    cursor.execute(sql)

    # salva e fecha conexão
    conect.commit()
    conect.close()