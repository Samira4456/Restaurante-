class Prato:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def is_valid(self):
        erros = []
        if not isinstance(self.id, int) or self.id <= 0:
            erros.append("ID deve ser um número inteiro positivo")
        if not self.nome or not isinstance(self.nome, str):
            erros.append("Nome não pode ser vazio e deve ser uma string")
        if not self.descricao or not isinstance(self.descricao, str):
            erros.append("Descrição não pode ser vazio e deve ser uma string")
        if not isinstance(self.preco, (int, float)) or self.preco <= 0:
            erros.append("Preço não pode ser zero ou negativo")
        if erros:
            print("Erro(s) encontrado(s):")
            for erro in erros:
                print(f"- {erro}")
            return False
        return True

