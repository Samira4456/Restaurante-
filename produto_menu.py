from produto_csv import (
    adicionar_produto,
    listar_produtos,
    atualizar_produto,
    remover_produto,
    carregar_produtos
)

def menu_produtos():
    produtos = carregar_produtos()
    while True:
        print("\n" + "-=" * 25)
        print("               MENU DE PRODUTOS")
        print("-=" * 25)
        print("1 - Adicionar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar produto")
        print("4 - Remover produto")
        print("s - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(produtos)
        elif opcao == "2":
            listar_produtos(produtos)
        elif opcao == "3":
            atualizar_produto(produtos)
        elif opcao == "4":
            remover_produto(produtos)
        elif opcao.lower() == "s":
            break
        else:
            print("Opção inválida. Tente novamente.")
