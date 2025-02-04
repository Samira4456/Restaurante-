class Prato:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f"{self.id},{self.nome},{self.descricao},{self.preco}"

    @staticmethod
    def from_string(data_str):
        try:
            partes = data_str.strip().split(",")
            if len(partes) != 4:
                raise ValueError("Formato da string inválido. Esperado: id,nome,descricao,preco")
            id = int(partes[0])
            nome = partes[1]
            descricao = partes[2]
            preco = float(partes[3])
            return Prato(id, nome, descricao, preco)
        except ValueError as e:
            print(f"Erro ao converter dados: {e}")
            return None
