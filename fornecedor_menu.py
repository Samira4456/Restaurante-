from fornecedor import Fornecedor, carregar_fornecedores_csv, gravar_fornecedores_csv, remover_fornecedor
from produto_csv import carregar_produtos

def adicionar_fornecedor(fornecedores):
    nome = input("Nome: ")
    telefone = input("Telefone (9 dígitos): ")
    email = input("Email: ")
    tipo = input("Tipo de produto (frescos, congelados, embalados, enlatados): ")

    novo = Fornecedor(nome, telefone, email, tipo)
    if novo.is_valid():
        fornecedores.append(novo)
        gravar_fornecedores_csv(fornecedores)
        print("Fornecedor adicionado com sucesso!")
    else:
        print("Dados inválidos. Verifique e tente novamente.")

def listar_fornecedores(fornecedores):
    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
        return
    for f in fornecedores:
        print(f)

def atualizar_fornecedor(fornecedores):
    nome = input("Digite o nome do fornecedor a atualizar: ")
    fornecedor = next((f for f in fornecedores if f.nome.lower() == nome.lower()), None)
    if not fornecedor:
        print("Fornecedor não encontrado.")
        return

    print("1 - Nome\n2 - Telefone\n3 - Email\n4 - Tipo de Produto")
    opcao = input("O que deseja atualizar? ")

    if opcao == "1":
        fornecedor.nome = input("Novo nome: ")
    elif opcao == "2":
        fornecedor.telefone = input("Novo telefone: ")
    elif opcao == "3":
        fornecedor.email = input("Novo email: ")
    elif opcao == "4":
        fornecedor.tipo_de_produto = input("Novo tipo: ")
    else:
        print("Opção inválida.")
        return

    if fornecedor.is_valid():
        gravar_fornecedores_csv(fornecedores)
        print("Fornecedor atualizado com sucesso!")
    else:
        print("Dados inválidos. Atualização não salva.")

def associar_produto_a_fornecedor(fornecedores):
    produtos = carregar_produtos()
    if not produtos:
        print("Nenhum produto disponível.")
        return

    nome_forn = input("Digite o nome do fornecedor: ")
    fornecedor = next((f for f in fornecedores if f.nome.lower() == nome_forn.lower()), None)
    if not fornecedor:
        print("Fornecedor não encontrado.")
        return

    print("Produtos disponíveis:")
    for i, p in enumerate(produtos):
        print(f"{i + 1} - {p.nome}")

    try:
        escolha = int(input("Escolha o número do produto para associar: "))
        if 1 <= escolha <= len(produtos):
            produto_escolhido = produtos[escolha - 1]
            fornecedor.associar_produto(produto_escolhido, fornecedores)
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")

def menu_fornecedores():
    fornecedores = carregar_fornecedores_csv()

    while True:
        print("\n" + "-=" * 25)
        print("              MENU DE FORNECEDORES")
        print("-=" * 25)
        print("1 - Adicionar fornecedor")
        print("2 - Listar fornecedores")
        print("3 - Atualizar fornecedor")
        print("4 - Remover fornecedor")
        print("5 - Associar produto a fornecedor")
        print("s - Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_fornecedor(fornecedores)
        elif opcao == "2":
            listar_fornecedores(fornecedores)
        elif opcao == "3":
            atualizar_fornecedor(fornecedores)
        elif opcao == "4":
            nome = input("Nome do fornecedor a remover: ")
            remover_fornecedor(fornecedores, nome)
        elif opcao == "5":
            associar_produto_a_fornecedor(fornecedores)
        elif opcao.lower() == "s":
            break
        else:
            print("Opção inválida. Tente novamente.")
