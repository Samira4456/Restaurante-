import fornecedor
import funcionario
import produto
import ementa 
import prato


FICHEIRO_FORNECEDORES= "fornecedores.txt"
FICHEIRO_PRODUTOS = "produtos.txt"
FICHEIRO = "funcionários.txt"
FICHEIRO_PRATOS = "pratos.txt"


# MENU PRINCIPAL
def menu_principal():
    produtos = produto.carregar_produtos(FICHEIRO_PRODUTOS)
    fornecedores = fornecedor.carregar_fornecedores(FICHEIRO_FORNECEDORES)
    funcionarios = funcionario.carregar_funcionarios(FICHEIRO)
    ementa = Ementa()  # Inicialize a classe Ementa aqui
    ementa.pratos = ementa.carregar_pratos()  # Carregue os pratos aqui
    while True:
        print("-*" * 40)
        print("                 MENU PRINCIPAL                     ")
        print("-*" * 40)
        print("1- Gerenciar Fornecedores")
        print("2- Gerenciar Produtos")
        print("3- Gerenciar Funcionário")
        print("4- Gerenciar Ementa")
        print("s- SAIR")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            fornecedor.menu_fornecedores(fornecedores, produtos)

        elif opcao == "2":
            produto.menu_produtos(produtos, fornecedores, produto.quantidade_produtos)

        elif opcao == "3":
            funcionario.menu_funcionario()
            funcionario.atualizar_funcionario()

        elif opcao == "4":
            ementa = Ementa()
            ementa.pratos = ementa.carregar_pratos()
            ementa.menu_ementa()


        elif opcao == "s":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente!")





if __name__ == "__main__":
    menu_principal()



