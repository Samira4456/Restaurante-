class Produto:
    def __init__(self, id, nome, descricao, preco, quantidade, tipo):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade = quantidade
        self.tipo = tipo
        self.fornecedores = []

    def __str__(self):
        fornecedores_str = ', '.join([f.nome for f in self.fornecedores]) if self.fornecedores else "Nenhum"
        return f"{self.id},{self.nome},{self.preco},{self.quantidade},{self.tipo} | Fornecedores: {fornecedores_str}"
