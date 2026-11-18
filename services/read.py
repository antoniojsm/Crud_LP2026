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

def displayProd():
    produtos = read() #Chama a funçao read() para exibir os produtos cadastrados na pasta serviç
    
    if not produtos:
        #verifica se a lista de produtos está vazia, caso esteja exibe a mensagem
        print("Nenhum produto cadastrado!")
    else:
        #caso a lista de produtos não esteja vazia, exibe os produtos cadastrados
        for produto in produtos:
            print(f"ID: {produto[0]} | Nome: {produto[1]} | Fabricante: {produto[2]} | Estoque: {produto[3]} | Valor: R${produto[4]:.2f}")