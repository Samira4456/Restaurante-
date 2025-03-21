FICHEIRO_PRODUTOS = "produtos.txt"

quantidade_produtos = 0

class Produto:
    def __init__(self, nome, preco, quantidade, tipo, fornecedor):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo
        self.fornecedores = []

    def __str__(self):
        fornecedores_str = ', '.join(
            [fornecedor.nome for fornecedor in self.fornecedores]) if self.fornecedores else "Nenhum"
        return f"{self.nome},{self.preco},{self.quantidade},{self.tipo}, Fornecedores: {fornecedores_str}"

    def from_string(data_str):
        nome, preco, quantidade, tipo, fornecedores = data_str.strip().split(",")
        return Produto(nome, float(preco), quantidade, tipo, fornecedores)

    # Associar e listar fornecedores

    def associar_fornecedor(self, fornecedor):
        if fornecedor not in self.fornecedores:
            self.fornecedores.append(fornecedor)
            print(f"Fornecedor {fornecedor.nome} associado ao produto {self.nome} com sucesso!")
        else:
            print("Este fornecedor já está associado a este produto.")

    def listar_fornecedores(self):
        if not self.fornecedores:
            print("Nenhum fornecedor associado a este produto.")
        else:
            print(f"Fornecedores do produto {self.nome}:")
            for fornecedor in self.fornecedores:
                print(f"- {fornecedor.nome} ({fornecedor.telefone}, {fornecedor.email})")

#ErrosValidações

    def is_valid_tipo(self):
        lista_tipos = ["frescos", "congelados", "embalados", "enlatados"]
        if self.tipo in lista_tipos:
            return True
        print("ERRO! Tipo de produto inválido. Tente novamente!")
        return False

    def is_valid_preco(self):
        if not isinstance(self.preco, (int, float)):
            print("ERRO! O preço deve ser um número.")
            return False
        return True

    def is_valid(self):
        return self.is_valid_tipo() and self.is_valid_preco()


# MENU DE PRODUTOS
def menu_produtos(produtos,fornecedores, quantidade_produtos):
    while True:
        print("-*" * 25)
        print("                  MENU DE PRODUTOS                   ")
        print("-*" * 25)
        print("1- Adicionar produto")
        print("2- Listar produtos")
        print("3- Remover Produto")
        print("4- Carregar produtos")
        print("5- Associar fornecedor a produto")
        print("6- Listar fornecedores de um produto")
        print("7- Mostrar quantidade de produtos")
        print("s- Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                print("Preencha os seguintes dados:")
                nome = input("Nome do produto: ")
                quantidade_produtos += 1
                preco = input("Preço: ")
                while True:
                    try:
                        preco = float(preco)
                        break
                    except ValueError:
                        print("Preço tem de ser um número")
                        preco = input("Preço: ")
                quantidade = input("Quantidade: ")
                tipo = input("Tipo de produto:(frescos,congelados,embalados,enlatados)- ")

                produto = Produto(nome, preco, quantidade, tipo, fornecedores)
                if produto.is_valid():
                    produtos.append(produto)
                    gravar_produto(FICHEIRO_PRODUTOS, produtos)
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
            remover_produto(produtos, fornecedores, FICHEIRO_PRODUTOS)

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

        elif opcao == "7":
            print("Produtos adicionados :", quantidade_produtos)


        elif opcao == "s":
            break
        else:
            print("Opção inválida. Tente novamente!")


#Persistencia

def gravar_produto(ficheiro, lista_produtos):
    with open(ficheiro, "w") as f:
        for produto in lista_produtos:
            f.write(str(produto) + "\n")

    print(f"Produtos gravados em {ficheiro} com sucesso!")


def carregar_produtos(ficheiro):
    produtos = []
    try:
        with open(ficheiro, "r") as f:
            for linha in f:
                produto = Produto.from_string(linha)
                if produto:
                    produtos.append(produto)
        print(f"Produtos carregados de {ficheiro} com sucesso!")
    except FileNotFoundError:

        print(f"O ficheiro {ficheiro} não foi encontrado.")
    return produtos


#Função para remover

def remover_produto(produtos, fornecedores, ficheiro):
    nome_produto = input("Nome do produto a remover: ")
    produto = next((p for p in produtos if p.nome == nome_produto), None)

    if not produto:
        print("Produto não encontrado!")
        return

    confirmacao = input(f"Deseja mesmo eliminar o produto '{nome_produto}'? (s/n): ")
    if confirmacao != 's':
        print("Operação cancelada.")
        return
    else:
        produtos.remove(produto)
        gravar_produto(ficheiro, produtos)
        print(f"Produto '{nome_produto}' removido com sucesso!")

           
   
