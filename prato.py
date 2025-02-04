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

    def is_valid(self):
        if self.preco < 0:
            return False
        if not self.nome:
            return False
        if len(self.nome) > 50:
            return False
        if not self.descricao:
            return False
        return True


# persistencia.py

from prato import Prato

class Persistencia:
    FICHEIRO = "pratos.txt"

    def ler_pratos(self):
        try:
            with open(self.FICHEIRO, "r") as f:
                pratos = [Prato.from_string(linha) for linha in f]
                return pratos
        except FileNotFoundError:
            return []
        except Exception as e:
            print(f"Ocorreu um erro ao ler os pratos: {e}")
            return []

    def gravar_prato(self, prato):
        with open(self.FICHEIRO, "a") as f:
            f.write(str(prato) + "\n")