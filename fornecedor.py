import re

FICHEIRO_FORNECEDORES = "fornecedores.txt"

class Fornecedor:
    def __init__(self, nome,NIF, telefone, email, tipo_de_produto, produtos):
        self.nome = nome
        self.NIF = NIF
        self.telefone = telefone
        self.email = email
        self.tipo_de_produto = tipo_de_produto
        self.produtos = []

    def __str__(self):
        produtos_str = ', '.join([produto.nome for produto in self.produtos]) if self.produtos else "Nenhum"
        return f"{self.nome},{self.NIF},{self.telefone},{self.email},{self.tipo_de_produto}, Produtos: {produtos_str}"

    def from_string(data_str):
        partes = data_str.strip().split(",")
        nome,NIF, telefone, email, tipo_de_produto = partes[:5]
        produtos = partes[5].split(";") if len(partes) > 5 and partes[5] else []
        return Fornecedor(nome,NIF, telefone, email, tipo_de_produto, produtos)

    # Associar Produto ao fornecedor

    def associar_produto(self, produto, fornecedores):
        if produto not in self.produtos:
            self.produtos.append(produto)
            gravar_fornecedor(FICHEIRO_FORNECEDORES, fornecedores)
            print(f"Produto {produto.nome} associado ao fornecedor {self.nome} com sucesso!")
        else:
            print("Este produto já está associado a este fornecedor.")

    # Listar Produtos associados
    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto associado a este fornecedor.")
        else:
            print(f"Produtos fornecidos por {self.nome}:")
            for produto in self.produtos:
                print(f"- {produto.nome} , Preço: {produto.preco}, Quantidade: {produto.quantidade})")

    # Erros/Validação de dados

    # validação do nome
    def is_valid_nome(self):
        if not all(c.isalpha() or c.isspace() for c in
                   self.nome):  # verifica se é composto apenas por letras e tbm permite espaços
            print("ERRO! O nome deve conter apenas letras")
            return False
        return True

    #validação NIF
    def is_valid_NIF(self):
        if not str(self.NIF).isdigit():  # verifica se o telefone tem apenas numeros
            print("ERRO! O NIF só pode conter números")
            return False

        if not len(self.NIF) == 9:  # verifica se o telefone tem 9 numeros
            print("ERRO! O NIF deve conter apenas 9 dígitos")
            return False
        return True


    # validação Telefone

    def is_valid_telefone(self):

        if not str(self.telefone).isdigit():  # verifica se o telefone tem apenas numeros
            print("ERRO! O telerfone só pode conter números")
            return False

        if not len(self.telefone) == 9:  # verifica se o telefone tem 9 numeros
            print("ERRO! O telefone deve conter apenas 9 dígitos")
            return False
        return True

    # Validação email

    def is_valid_email(self):
        email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not re.match(email_regex, self.email):
            print("ERRO! Email inválido.Tente novamente!")
            return False
        return True

    # Validação Tipo de Produto

    def is_valid_tipo_de_produto(self):
        lista_tipos = ["frescos", "congelados", "embalados", "enlatados"]
        if self.tipo_de_produto in lista_tipos:
            return True
        else:
            print("ERRO!Tipo de produto inválido.Tente novamente!")
            return False



    def is_valid(self):
        return (self.is_valid_nome() and
                self.is_valid_NIF() and
                self.is_valid_telefone() and
                self.is_valid_email() and
                self.is_valid_tipo_de_produto())


# Menu de fornecedores
def menu_fornecedores(fornecedores, produtos):
    while True:
        print("-*" * 25)
        print("                  MENU DE FORNECEDORES               ")
        print("-*" * 25)
        print("1- Adicionar fornecedor")
        print("2- Ver Lista de fornecedores")
        print("3- Atualizar fornecedor")
        print("4- Remover fornecedor")
        print("5- Associar produto a um fornecedor")
        print("6- Listar produtos associados")
        print("s- Voltar ao menu principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                print("Preencha os seguintes dados:")
                nome = input("Nome do fornecedor: ")
                NIF = input("NIF: ")
                telefone = input("Contato telefônico: ")
                email = input("Email: ")
                tipo_de_produto = input("Tipo de produtos que fornece:(frescos,congelados,embalados,enlatados)")

                forn = Fornecedor(nome, NIF, telefone, email, tipo_de_produto, produtos)
                if forn.is_valid():
                    fornecedores.append(forn)
                    gravar_fornecedor(FICHEIRO_FORNECEDORES, fornecedores)

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
                    print(f"NIF: {fornecedor.NIF}")
                    print(f"Telefone: {fornecedor.telefone}")
                    print(f"Email: {fornecedor.email}")
                    print(f"Tipo de Produto: {fornecedor.tipo_de_produto}")
                    print("-" * 40)

        elif opcao== "3":
            atualizar_fornecedor(fornecedores)


        elif opcao == "4":
            remover_fornecedor(fornecedores, produtos, FICHEIRO_FORNECEDORES)

        elif opcao == "5":
            nome_fornecedor = input("Nome do fornecedor: ")
            fornecedor = next((f for f in fornecedores if f.nome == nome_fornecedor), None)
            if fornecedor:
                nome_produto = input("Nome do produto: ")
                produto = next((p for p in produtos if p.nome == nome_produto), None)
                if produto:
                    fornecedor.associar_produto(produto, fornecedores)

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


# Persistencia
def gravar_fornecedor(ficheiro, lista_fornecedores):
    with open(ficheiro, "w") as f:
        for fornecedor in lista_fornecedores:
            produtos_str = ";".join([p.nome for p in fornecedor.produtos])
            f.write(str(fornecedor) + "\n")



def carregar_fornecedores(ficheiro):
    fornecedores = []
    try:
        with open(ficheiro, "r") as f:
            for linha in f:
                fornecedor = Fornecedor.from_string(linha)  # De linha para instancia
                fornecedores.append(fornecedor)
        print(f"Fornecedores carregados de {ficheiro}com sucesso!")
    except FileNotFoundError:
        print(f"O ficheiro {ficheiro} não foi encontrado.")
    return fornecedores


# Função para remover fornecedor
def remover_fornecedor(fornecedores, produtos, ficheiro):

    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
        return

    print("\nLista de Fornecedores:")
    for fornecedor in fornecedores:
        print(f"- Nome: {fornecedor.nome} | NIF: {fornecedor.NIF}")

    nif_fornecedor = input("\nDigite o NIF do fornecedor a remover: ")
    fornecedor = next((f for f in fornecedores if f.NIF == nif_fornecedor), None)


    if not fornecedor:
        print("Fornecedor não encontrado!")
        return

    confirmacao = input(f"Deseja mesmo eliminar o fornecedor '{fornecedor.nome}'(NIF: {nif_fornecedor})? (s/n): ")
    if confirmacao != 's':
        print("Operação cancelada.")
        return
    else:
        fornecedores.remove(fornecedor)
        gravar_fornecedor(ficheiro, fornecedores)
        print(f"Fornecedor '{fornecedor.nome}'  removido com sucesso!")



#Função para atualizar dados
def atualizar_fornecedor(fornecedores):
    if not fornecedores:
        print("Nenhum fornecedor cadastrado.")
        return

    print("\nLista de Fornecedores:")
    for fornecedor in fornecedores:
        print(f"- Nome: {fornecedor.nome} | NIF: {fornecedor.NIF}")


    nif_fornecedor = input("\nDigite o NIF do fornecedor que deseja atualizar: ")
    fornecedor = next((f for f in fornecedores if f.NIF == nif_fornecedor), None)


    if not fornecedor:
        print("Fornecedor não encontrado!")
        return

    print(f"\nAtualizando os dados do fornecedor {fornecedor.nome}:")
    novo_nome = input(f"Nome (atualmente: {fornecedor.nome}): ")
    novo_nif = input(f"NIF (atualmente: {fornecedor.NIF}): ")
    novo_telefone = input(f"Telefone (atualmente: {fornecedor.telefone}): ")
    novo_email = input(f"Email (atualmente: {fornecedor.email}): ")
    novo_tipo_de_produto = input(f"Tipo de produto (atualmente: {fornecedor.tipo_de_produto}): ")

    confirmacao = input("\nDeseja mesmo mudar os dados? (s/n)")
    if confirmacao != 's':
        print("Atualização cancelada.")
        return

    fornecedor.nome = novo_nome if novo_nome else fornecedor.nome
    fornecedor.NIF = novo_nif if novo_nif else fornecedor.NIF
    fornecedor.telefone = novo_telefone if novo_telefone else fornecedor.telefone
    fornecedor.email = novo_email if novo_email else fornecedor.email
    fornecedor.tipo_de_produto = novo_tipo_de_produto if novo_tipo_de_produto else fornecedor.tipo_de_produto


    if fornecedor.is_valid():
        gravar_fornecedor(FICHEIRO_FORNECEDORES, fornecedores)
        print(f"Fornecedor {fornecedor.nome} atualizado com sucesso!")
    else:
        print("Dados inválidos. A atualização foi cancelada.")

   

