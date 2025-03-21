from prato import Prato
import csv

class Ementa:
    def __init__(self):
        self.pratos = self.carregar_pratos()

    def carregar_pratos(self):
        try:
            with open('pratos.csv', 'r') as arquivo:
                reader = csv.reader(arquivo)
                next(reader)  # Pula a linha de cabeçalho
                pratos = []
                for row in reader:
                    prato = Prato(int(row[0]), row[1], row[2], float(row[3]))
                    pratos.append(prato)
                return pratos
        except FileNotFoundError:
            return []

    def salvar_pratos(self):
        with open('pratos.csv', 'w', newline='') as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["id", "nome", "descricao", "preco"])
            for prato in self.pratos:
                writer.writerow([prato.id, prato.nome, prato.descricao, prato.preco])

    def listar_pratos(self):
        if not self.pratos:
            print("Não há pratos cadastrados.")
        else:
            for prato in self.pratos:
                print(f"ID: {prato.id}")
                print(f"Nome: {prato.nome}")
                print(f"Descrição: {prato.descricao}")
                print(f"Preço: {prato.preco}")
                print("------------------------")

    def menu_ementa(self):
        while True:
            print(" MENU DE PRATOS ")
            print("1- Listar pratos")
            print("2- Adicionar prato à ementa")
            print("3- Remover prato")
            print("4- Atualizar prato")
            print("s- SAIR")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.listar_pratos()
            elif opcao == "2":
                self.adicionar_prato_interativo()
            elif opcao == "3":
                self.remover_prato_interativo()
            elif opcao == "4":
                self.atualizar_prato_interativo()
            elif opcao == "s":
                print("Saindo do menu de ementa...")
                break
            else:
                print("Opção inválida. Tente novamente!")

    def adicionar_prato_interativo(self):
        id_prato = int(input("Digite o ID do novo prato: "))
        nome_prato = input("Digite o nome do novo prato: ")
        descricao_prato = input("Digite a descrição do novo prato: ")
        preco_prato = float(input("Digite o preço do novo prato: "))
        novo_prato = Prato(id_prato, nome_prato, descricao_prato, preco_prato)
        self.pratos.append(novo_prato)
        self.salvar_pratos()
        print("Prato adicionado com sucesso!")

    def remover_prato_interativo(self):
        id_prato = int(input("Digite o ID do prato que deseja remover: "))
        for prato in self.pratos:
            if prato.id == id_prato:
                self.pratos.remove(prato)
                self.salvar_pratos()
                print("Prato removido com sucesso!")
                return
        print("Prato não encontrado.")

# implementação do método
    def atualizar_prato_interativo(self):
        id_prato = int(input("Digite o ID do prato que deseja atualizar: "))
        for prato in self.pratos:
            if prato.id == id_prato:
                print("Prato encontrado!")
                print("1- Atualizar nome")
                print("2- Atualizar descrição")
                print("3- Atualizar preço")
                opcao = input("Escolha uma opção: ")
                if opcao == "1":
                    novo_nome = input("Digite o novo nome do prato: ")
                    prato.nome = novo_nome
                elif opcao == "2":
                    nova_descricao = input("Digite a nova descrição do prato: ")
                    prato.descricao = nova_descricao
                elif opcao == "3":
                    novo_preco = float(input("Digite o novo preço do prato: "))
                    prato.preco = novo_preco
                self.salvar_pratos()
                print("Prato atualizado com sucesso!")
                return
        print("Prato não encontrado.")
