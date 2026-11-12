def menu():
    titulo = "Controle de Estoque"
    center = int((50-len(titulo))/2)

    print(f"{"="*50}\n{" "*center}{titulo}\n{"="*50}")
    print(f"\n[1] Cadastrar\n[2] Atualizar produto\n[3] Exibir produto\n[4] Excluir produto")

menu()
while True:
    opc = int(input("\nInsira uma opção: > "))

    if 1 <= opc <= 4:
        break
    else:
        print("[ERRO] Insira uma opção valida!")