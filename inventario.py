import csv
from produto import Produto

ARQUIVO_CSV = "produtos.csv"

def salvar_produtos(produtos):
    with open(ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nome', 'descricao', 'preco', 'quantidade', 'tipo'])
        for produto in produtos:
            writer.writerow([produto.id, produto.nome, produto.descricao, produto.preco, produto.quantidade, produto.tipo])

def carregar_produtos():
    produtos = []
    try:
        with open(ARQUIVO_CSV, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for linha in reader:
                p = Produto(
                    int(linha['id']),
                    linha['nome'],
                    linha['descricao'],
                    float(linha['preco']),
                    int(linha['quantidade']),
                    linha['tipo']
                )
                produtos.append(p)
    except FileNotFoundError:
        pass
    return produtos

def adicionar_produto(produtos):
    try:
        id = int(input("ID do produto: "))
        nome = input("Nome: ")
        descricao = input("Descrição: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        tipo = input("Tipo (frescos, congelados, embalados, enlatados): ")
        novo = Produto(id, nome, descricao, preco, quantidade, tipo)
        produtos.append(novo)
        salvar_produtos(produtos)
        print("Produto adicionado com sucesso!")
    except ValueError:
        print("Erro ao inserir os dados. Tente novamente.")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto encontrado.")
        return
    for p in produtos:
        print(p)

def atualizar_produto(produtos):
    try:
        id = int(input("Digite o ID do produto a ser atualizado: "))
        produto = next((p for p in produtos if p.id == id), None)
        if not produto:
            print("Produto não encontrado.")
            return
        print("Produto encontrado. O que deseja atualizar?")
        print("1 - Nome\n2 - Descrição\n3 - Preço\n4 - Quantidade\n5 - Tipo")
        opcao = input("Escolha: ")
        if opcao == "1":
            produto.nome = input("Novo nome: ")
        elif opcao == "2":
            produto.descricao = input("Nova descrição: ")
        elif opcao == "3":
            produto.preco = float(input("Novo preço: "))
        elif opcao == "4":
            produto.quantidade = int(input("Nova quantidade: "))
        elif opcao == "5":
            produto.tipo = input("Novo tipo (frescos, congelados, embalados, enlatados): ")
        else:
            print("Opção inválida.")
            return
        salvar_produtos(produtos)
        print("Produto atualizado com sucesso!")
    except ValueError:
        print("Erro de entrada. Tente novamente.")

def remover_produto(produtos):
    try:
        id = int(input("Digite o ID do produto a remover: "))
        produto = next((p for p in produtos if p.id == id), None)
        if produto:
            produtos.remove(produto)
            salvar_produtos(produtos)
            print("Produto removido com sucesso!")
        else:
            print("Produto não encontrado.")
    except ValueError:
        print("ID inválido.")
