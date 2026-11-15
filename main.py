from db.database import initDatabase
from services.create import cadastrar

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
        opc = int(input("\nInsira uma opção: > "))

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
                    entrada = input("Insira o valor > ")
                    produto[chave] = float(entrada.replace(",", "."))
                elif tipo is int:
                    produto[chave] = int(input("Quant. Estoque > "))
                else:
                    produto[chave] = input(f"Insira o {chave} > ")

            cadastrar(produto)       

        case 2: # Atualizar produto
            pass
        case 3: # Exibir produto
            pass
        case 4: # Excluir produto
            pass
        case 5:
            print(">> Programa encerrado!")
            break