from db.database import initDatabase
from services.create import cadastrar
from services.read import displayProd
from services.delete import delete 
from services.update import update

# Exibição de menu no terminal
def menu():
    titulo = "Controle de Estoque"
    center = int((50-len(titulo))/2)

    print(f"{"="*50}\n{" "*center}{titulo}\n{"="*50}")
    print(f"\n[1] Cadastrar\n[2] Atualizar produto\n[3] Exibir produto\n[4] Excluir produto\n[5] Encerrar")

initDatabase() #inicialização do banco de dados

while True:
    menu() #chamada do menu

    #validação do input do usuario
    while True:
        opc = int(input("\nInsira uma opção > "))

        if 1 <= opc <= 5:
            break
        else:
            print("[ERRO] Insira uma opção valida!")

    match(opc):
        case 1: # cadastrar
            produto = {"nome": str, "fabricante": str, "estoque": int, "valor": float}

            # passa pelos itens para realizar o input com tipo correto
            for chave, tipo in produto.items():
                if tipo is float:
                    entrada = input("Insira o valor: ")
                    produto[chave] = float(entrada.replace(",", "."))
                elif tipo is int:
                    produto[chave] = int(input("Quant. Estoque > "))
                else:
                    produto[chave] = input(f"Insira o {chave} > ")

            cadastrar(produto)       

        case 2: # Atualizar produto
            displayProd() # mostra lista de itens cadastrados

            update_id = int(input("\nQual produto deseja alterar > "))

            #dicionario que recebe os dados
            prod_info = {"nome": "", "fabricante": "", "estoque": "", "valor": ""}

            print("\nAlterar Registro\n>> Caso não deseje alterar algum valor\n já registrado deixe o campo [VAZIO]\n")
            #solicita infomações que desejam ser alterada ao dicionario
            prod_info["nome"] = input("Nome > ")
            prod_info["fabricante"] = input("Fabricante > ")

            while True:
                prod_info["estoque"] = input("Estoque > ")
                try:
                    prod_info["estoque"] = int(prod_info["estoque"])
                    break
                except ValueError:
                    print("[ERRO] Insira um número inteiro!")

            #Se estiver vazio o valor se mantém o valor antigo

        case 3: # Exibir produto
            displayProd() # mostra lista de itens cadastrados

            while True:
                continuar = input("\nDigite [s] para continuar > ")

                if continuar.lower() == "s":
                    break

        case 4: # Excluir produto
            displayProd() # mostra lista de itens cadastrados

            prod_id = int(input("\nInsira o ID do produto a ser excluido > "))
            delete(prod_id) #Chama a função delete() para excluir o produto com o ID informado
            
        case 5:
            print(">> Programa encerrado!")
            break