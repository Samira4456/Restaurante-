from persistencia import Persistencia
from prato import Prato
from fornecedor import Fornecedor
from persistencia_fornecedores import gravar_fornecedores, carregar_fornecedores
from produto import Produto
from persistencia_produto import gravar_produtos, carregar_produtos
from funcionario import Funcionario, carregar_funcionarios, validar_dados
from persistencia_funcionario import gravar_funcionarios, carregar_funcionarios

FICHEIRO_FORNECEDORES = "fornecedores.txt"
FICHEIRO_PRODUTOS = "produtos.txt"
FICHEIRO = "funcionario.txt"
FICHEIRO_PRATOS = "pratos.txt"

# MENU PRINCIPAL
def menu_principal():
    produtos = carregar_produtos(FICHEIRO_PRODUTOS)
    fornecedores = carregar_fornecedores(FICHEIRO_FORNECEDORES)

    while True:
        print("-*" * 40)
        print("                 MENU PRINCIPAL                     ")
        print("-*" * 40)
        print("1- Gerenciar Fornecedores")
        print("2- Gerenciar Produtos")
        print("3- Gerenciar Funcionário")
        print("4- Listar pratos")
        print("s- SAIR")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_fornecedores(fornecedores, produtos)
        elif opcao == "2":
            menu_produtos(produtos, fornecedores)

        elif opcao == "3":
            menu_funcionario()
        elif opcao== "4":
            menu_pratos()

        elif opcao == "s":
            print("A sair...")
            break
        else:
            print("Opção inválida. Tente novamente!")

# MENU DE FORNECEDORES
def menu_fornecedores(fornecedores,produtos):
    while True:
        print("-*" * 25)
        print("                  MENU DE FORNECEDORES               ")
        print("-*" * 25)
        print("1- Adicionar fornecedor")
        print("2- Listar fornecedores")
        print("3- Gravar fornecedor")
        print("4- Carregar fornecedores")
        print("5- Associar produto a um fornecedor")
        print("6- Listar produtos associados")
        print("s- Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                print("Preencha os seguintes dados:")
                nome = input("Nome do fornecedor: ")
                telefone = input("Contato telefônico: ")
                email = input("Email: ")
                tipo_de_produto = input("Tipo de produtos que fornece:(frescos,congelados,embalados,enlatados)")

                forn = Fornecedor(nome, telefone, email, tipo_de_produto, produtos)
                if forn.is_valid():
                    fornecedores.append(forn)
                    print("Fornecedor adicionado com sucesso!")
                    break
                else:
                    print("Fornecedor inválido. Verifique os dados e tente novamente.")

        elif opcao == "2":
            if not fornecedores:
                print("Nenhum fornecedor cadastrado.")
            else:
                for fornecedor in fornecedores:

                    print("-" * 40)
                    print(f"Nome: {fornecedor.nome}")
                    print(f"Telefone: {fornecedor.telefone}")
                    print(f"Email: {fornecedor.email}")
                    print(f"Tipo de Produto: {fornecedor.tipo_de_produto}")
                    print("-" * 40)

        elif opcao == "3":
            gravar_fornecedores(FICHEIRO_FORNECEDORES, fornecedores)
            print("Fornecedores gravados com sucesso!")

        elif opcao == "4":
            fornecedores.extend(carregar_fornecedores(FICHEIRO_FORNECEDORES))
            print("Fornecedores carregados com sucesso!")

        elif opcao == "5":
            nome_fornecedor = input("Nome do fornecedor: ")
            fornecedor = next((f for f in fornecedores if f.nome == nome_fornecedor), None)
            if fornecedor:
                nome_produto = input("Nome do produto: ")
                produto = next((p for p in produtos if p.nome == nome_produto), None)
                if produto:
                    fornecedor.associar_produto(produto)
                else:
                    print("Produto não encontrado.")
            else:
                print("Fornecedor não encontrado.")

        elif opcao == "6":
            nome_fornecedor = input("Nome do fornecedor: ")
            fornecedor = next((f for f in fornecedores if f.nome == nome_fornecedor), None)
            if fornecedor:
                fornecedor.listar_produtos()
            else:
                print("Fornecedor não encontrado.")

        elif opcao == "s":
            break
        else:
            print("Opção inválida. Tente novamente!")



# MENU DE PRODUTOS
def menu_produtos(produtos, fornecedores):
    while True:
        print("-*" * 25)
        print("                  MENU DE PRODUTOS                   ")
        print("-*" * 25)
        print("1- Adicionar produto")
        print("2- Listar produtos")
        print("3- Gravar produtos")
        print("4- Carregar produtos")
        print("5- Associar fornecedor a produto")
        print("6- Listar fornecedores de um produto")
        print("s- Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                print("Preencha os seguintes dados:")
                nome = input("Nome do produto: ")
                preco = float( input("Preço: "))
                quantidade = input("Quantidade: ")
                tipo = input("Tipo de produto:(frescos,congelados,embalados,enlatados)- ")

                produto = Produto(nome, preco, quantidade, tipo,fornecedores)
                if produto.is_valid():
                    produtos.append(produto)
                    print("Produto adicionado com sucesso!")
                    break
                else:
                    print("Produto inválido. Verifique os dados e tente novamente.")



        elif opcao == "2":
            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                for produto in produtos:

                    print("-" * 40)
                    print(f"Nome: {produto.nome}")
                    print(f"preço: {produto.preco}")
                    print(f"quantidade: {produto.quantidade}")
                    print(f"Tipo : {produto.tipo}")
                    print("-" * 40)

        elif opcao == "3":
            gravar_produtos(FICHEIRO_PRODUTOS, produtos)
            print("Produtos gravados com sucesso!")

        elif opcao == "4":
            produtos.extend(carregar_produtos(FICHEIRO_PRODUTOS))
            print("Produtos carregados com sucesso!")

        elif opcao == "5":
            nome_produto = input("Nome do produto: ")
            produto = next((p for p in produtos if p.nome == nome_produto), None)
            if produto:
                nome_fornecedor = input("Nome do fornecedor: ")
                fornecedor = next((f for f in fornecedores if f.nome == nome_fornecedor), None)
                if fornecedor:
                    produto.associar_fornecedor(fornecedor)
                else:
                    print("Fornecedor não encontrado.")
            else:
                print("Produto não encontrado.")

        elif opcao == "6":
            nome_produto = input("Nome do produto: ")
            produto = next((p for p in produtos if p.nome == nome_produto), None)
            if produto:
                produto.listar_fornecedores()
            else:
                print("Produto não encontrado.")

        elif opcao == "s":
            break
        else:
            print("Opção inválida. Tente novamente!")


# MENU DE FUNCIONÁRIOS
lista_funcionario = []

def menu_funcionario():
    funcionarios = []

    while True:
        print("-*" * 25)
        print("                  MENU DE OPÇÕES                     ")
        print("-*" * 25)
        print("1- Cadastrar o funcionário")
        print("2- Listar funcionários")
        print("3- Gravar funcionários")
        print("4- Carregar funcionários")
        print("5- SAIR")

        escolha = input("Faça uma escolha: ")

        if escolha == "1":
            print("\nPreencha as seguintes informações abaixo :")
            nome = str(input("Nome Completo: "))
            idade = input("Idade: ")
            cargo = input("Cargo: ")
            salario = input("Salário: ")
            NIF = input("NIF: ")

            if validar_dados(nome, idade, NIF):
                novo_funcionario = Funcionario(str(nome), int(idade), cargo, salario,NIF)
                funcionarios.append(novo_funcionario)
                print("\nFuncionário adicionado com sucesso!")
            else:
                print("Erro ao cadastrar funcionário. Verifique os dados e tente novamente!")

        elif escolha == "2":
            if not funcionarios:
                print("\nNenhum funcionário cadastrado.")
            else:
                print("\nLista de funcionários:")
                for func in funcionarios:
                    print("-" * 40)
                    print(f"Nome: {func.nome}")
                    print(f"Idade: {func.idade}")
                    print(f"Cargo: {func.cargo}")
                    print(f"Salário: {func.salario}")
                    print(f"NIF: {func.NIF}")
                    print("-" * 40)

        elif escolha == "3":
            gravar_funcionarios(FICHEIRO, funcionarios)

        elif escolha == "4":
            funcionarios_carregados = carregar_funcionarios(FICHEIRO)
            if funcionarios_carregados:
                funcionarios.extend(funcionarios_carregados)
                print("\nFuncionários carregados com sucesso!")

        elif escolha == "5":
            print("Saindo do programa...")

            break

        else:
            print("Opção inválida. Tente novamente!")


# MENU PRATOS
def menu_pratos():
    print("-*" * 40)
    print(" MENU DE PRATOS ")
    print("-*" * 40)
    print("1- Listar pratos")
    print("s- SAIR")
    pratos_opcao = input("Escolha uma opção: ")
    if pratos_opcao == "1":
        # Código para listar pratos
        pratos = [
            Prato(1, "Bacalhau à Brás", "Bacalhau desfiado com batata, cebola e ovos", 18.50),
            Prato(2, "Caldeirada", "Sopa de peixe com batata, cebola e especiarias", 15.00),
            Prato(3, "Feijoada à Transmontana", "Feijoada cozida com carne de porco e especiarias", 19.00),
            Prato(4, "Leitão à Bairrada", "Leitão assado com batata e especiarias", 22.00),
        ]
        print("\nLista de pratos:")
        for prato in pratos:
            print("-" * 40)
            print(f"ID: {prato.id}")
            print(f"Nome: {prato.nome}")
            print(f"Descrição: {prato.descricao}")
            print(f"Preço: {prato.preco}")
            print("-" * 40)
    elif pratos_opcao == "s":
        print("A sair...")
    else:
        print("Opção inválida. Tente novamente!")


if __name__ == "__main__":
    menu_principal()
