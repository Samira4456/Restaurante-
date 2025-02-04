class Prato:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f'{self.id},{self.nome},{self.descricao},{self.preco}'

    @staticmethod
    def from_string(data_str):
        id, nome, descricao, preco = data_str.strip().split(",")
        return Prato(int(id), nome, descricao, int(preco))

    def is_valid(self):
        if self.preco < 0:
            return False
        if not self.nome:
            return False
        if len(self.nome) > 50:
            return False
        return True
