import csv
 

ARQUIVO_CSV = "produtos.csv"

class Produto:
    def __init__(self, id, nome, preco, quantidade, tipo):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo

    def __str__(self):
        return f"{self.id} | {self.nome} | R${self.preco:.2f} | Quant: {self.quantidade} | Tipo: {self.tipo}"

from produto import Produto

ARQUIVO_CSV = "produtos.csv"

def salvar_produtos(produtos):
    with open(ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nome', 'preco', 'quantidade', 'tipo'])
        for produto in produtos:
            writer.writerow([produto.id, produto.nome, produto.preco, produto.quantidade, produto.tipo])
 main

def carregar_produtos():
    produtos = []
    try:
        with open(ARQUIVO_CSV, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for linha in reader:
                p = Produto(
                    int(linha['id']),
                    linha['nome'],
                    float(linha['preco']),
                    int(linha['quantidade']),
                    linha['tipo']
                )
                produtos.append(p)
    except FileNotFoundError:
        pass
    return produtos


def salvar_produtos(produtos):
    with open(ARQUIVO_CSV, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nome', 'preco', 'quantidade', 'tipo'])
        for produto in produtos:
            writer.writerow([produto.id, produto.nome, produto.preco, produto.quantidade, produto.tipo])

def gerar_novo_id(produtos):
    if not produtos:
        return 1
    return max(p.id for p in produtos) + 1

def adicionar_produto(produtos):
    try:

def adicionar_produto(produtos):
    try:
        if produtos:
            ultimo_id = max(p.id for p in produtos)
        else:
            ultimo_id = 0
        novo_id = ultimo_id + 1

 main
        nome = input("Nome: "))
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        tipo = input("Tipo (frescos, congelados, embalados, enlatados): ")
 Sprint-3
        novo_id = gerar_novo_id(produtos)
        novo = Produto(novo_id, nome, preco, quantidade, tipo)
        produtos.append(novo)
        salvar_produtos(produtos)
        print("Produto adicionado com sucesso!")

        novo = Produto(novo_id, nome,preco, quantidade, tipo)
        produtos.append(novo)
        salvar_produtos(produtos)
        print(f"Produto adicionado com sucesso com ID {novo_id}!")
 main
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
        print("1 - Nome\n2 - Preço\n4 - Quantidade\n5 - Tipo")
        opcao = input("Escolha: ")
        if opcao == "1":
            produto.nome = input("Novo nome: ")
       elif opcao == "2":
            produto.preco = float(input("Novo preço: "))
        elif opcao == "3":
            produto.quantidade = int(input("Nova quantidade: "))
        elif opcao == "4":
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

def atualizar_produto(produtos):
    try:
        id = int(input("Digite o ID do produto a ser atualizado: "))
        produto = next((p for p in produtos if p.id == id), None)
        if not produto:
            print("Produto não encontrado.")
            return
        print("Produto encontrado. O que deseja atualizar?")
        print("1 - Nome\n2 - Preço\n4 - Quantidade\n5 - Tipo")
        opcao = input("Escolha: ")
        if opcao == "1":
 Sprint-3
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

            produto.nome = input("Novo nome: ")
        elif opcao == "2":
            produto.preco = float(input("Novo preço: "))
        elif opcao == "3":
            produto.quantidade = int(input("Nova quantidade: "))
        elif opcao == "4":
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

class Produto:
    def __init__(self, id, nome,preco, quantidade, tipo):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo
        self.fornecedores = []

    def __str__(self):
        fornecedores_str = ', '.join([f.nome for f in self.fornecedores]) if self.fornecedores else "Nenhum"
        return f"{self.id},{self.nome},{self.preco},{self.quantidade},{self.tipo} | Fornecedores: {fornecedores_str}"
 main
