import sqlite3

def createTables():
    conn = sqlite3.connect('db/database.db') # Conecta com a base de dados
    cursor = conn.cursor()

    # cursor excuta os comando sql, se não houver tabela ele a cria
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome VARCHAR(50) NOT NULL,
            fabricante VARCHAR(25) NOT NULL,
            estoque INTEGER NOT NULL,
            valor DECIMAL(10, 2) NOT NULL
            )
        ''')

    # Salva e fecha a conexão
    conn.commit()
    conn.close()

def initDatabase():
    try:
        # busca o arquivo da base de dados, se não existir será criado
        db = open("db/database.db", "x")
        db.close()

        createTables()

        print("[Base de dados Criada no primeiro acesso!]")
    except FileExistsError:

        #Se o arquivo existe ele cria as tabelas
        print(">> Arquivo existe!")
        createTables()


        
