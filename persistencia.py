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