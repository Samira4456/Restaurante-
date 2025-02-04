from produto import Produto

def gravar_produtos(ficheiro, lista_produtos):
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
