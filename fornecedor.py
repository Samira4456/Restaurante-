import re

class Fornecedor :
    def __init__(self,nome,telefone,email,tipo_de_produto,produtos):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.tipo_de_produto = tipo_de_produto
        self.produtos = []


    def __str__(self):
        produtos_str = ', '.join([produto.nome for produto in self.produtos]) if self.produtos else "Nenhum"
        return f"{self.nome},{self.telefone},{self.email},{self.tipo_de_produto}, Produtos: {produtos_str}"

    def from_string(data_str):
     nome,telefone,email,tipo_de_produto,produtos= data_str.strip().split(",")
     return Fornecedor(nome,telefone,email,tipo_de_produto,produtos )

    # Associar Produto ao fornecedor

    def associar_produto(self, produto):
        if produto not in self.produtos:
            self.produtos.append(produto)
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
                self.is_valid_telefone() and
                self.is_valid_email() and
                self.is_valid_tipo_de_produto())

