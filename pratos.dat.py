import csv

class Prato:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Descrição: {self.descricao}, Preço: {self.preco}"

class Ementa:
    def __init__(self):
        self.pratos = Ementa.carregar_pratos()

    @staticmethod
    def carregar_pratos():
        print("Carregando pratos...")
        try:
            with open('pratos.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)  # Pula a linha de cabeçalho
                pratos = []
                for row in reader:
                    prato = Prato(int(row[0]), row[1], row[2], float(row[3]))
                    pratos.append(prato)
                print("Pratos carregados!")
                return pratos
        except FileNotFoundError:
            print("Arquivo de pratos não encontrado!")
            return []

    @staticmethod
    def salvar_pratos(pratos):
        print("Salvando pratos...")
        with open('pratos.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["id", "nome", "descricao", "preco"])
            for prato in pratos:
                writer.writerow([prato.id, prato.nome, prato.descricao, prato.preco])
        print("Pratos salvos!")

    def adicionar_prato(self, prato):
        self.pratos.append(prato)
        Ementa.salvar_pratos(self.pratos)

    def get_pratos(self):
        return self.pratos

if __name__ == "__main__":
    main()
