FICHEIRO = "funcionários.txt"
class Funcionario:
    def __init__(self,nome,idade,salario , cargo, NIF):
        self.nome = nome
        self.idade = idade
        self.salario= salario
        self.cargo = cargo
        self.NIF = NIF

    def __str__(self):
        return f"{self.nome},{self.idade},{self.salario},{self.cargo}, {self.NIF}"

    def from_string(data_str):
        data = data_str.strip().split(",")

        if len(data) != 5:
            print(f"Erro: Dados incompletos ou mal formatados na linha: {data_str}")
            return None
        nome, idade, salario, cargo, NIF = data
        return Funcionario(nome, idade, salario, cargo, NIF)


# Função para atualizar o funcionario
def atualizar_funcionarios (funcionario) :
    print(" O que  gostaria de atualizar ?")
    print(" 1- Nome ")
    print(" 2- Idade ")
    print(" 3- Cargo ")
    print(" 4- Salário ")
    print(" 5- NIF ")
    print(" 6- Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        novo_nome = input("Digite o novo nome: ")
        while not validar_nome(novo_nome) :
            novo_nome = input("Digite o novo nome: ")
        funcionario.nome = novo_nome
        print(f"Nome atualizado para: {funcionario.nome}")
    elif opcao == 2:
        nova_idade = input("Digite a nova idade: ")
        while True:
            try:
                nova_idade = int(nova_idade)
                if validar_novosdados(nova_idade, funcionario.NIF):
                    funcionario.idade = nova_idade
                    print(f"Idade atualizada para: {funcionario.idade}")
                    break
                else:
                    nova_idade = input("Digite uma idade válida (maior que 18): ")
            except ValueError:
                print("Erro! A idade tem de apresentar um valor inteiro!")
                nova_idade = input("Digite a nova idade: ")
    elif opcao == 3:
        novo_cargo = input("Digite o novo cargo: ")
        funcionario.cargo = novo_cargo
        print(f"Cargo atualizado para: {funcionario.cargo}")
    elif opcao == 4 :
        novo_salario = input("Digite o novo salário")
        funcionario.salario = novo_salario
        print(f"Salário atualizado para: {funcionario.salario}")
    elif opcao == 5:
        novo_NIF = input("Digite o novo NIF: ")
        while True:
            if len(novo_NIF) == 9 and novo_NIF.isdigit():
                funcionario.NIF = novo_NIF
                print(f"NIF atualizado para: {funcionario.NIF}")
                break
            else:
                print("ERRO! O NIF deve conter 9 dígitos numéricos e deve ser um número válido.Tente novamente")
                novo_NIF = input("Digite o novo NIF: ")
    elif opcao == 6:
        print("Saindo...")


    else:
        print("Opção inválida!")


# MENU DE FUNCIONÁRIOS
lista_funcionario = []

def menu_funcionario():
    funcionarios = []

    while True:
        print("-*" * 25)
        print("                  MENU DE OPÇÕES                     ")
        print("-*" * 25)
        print("1- Cadastrar o funcionário")
        print("2- Listar funcionários")
        print("3- Carregar funcionários")
        print("4- Atualizar funcionário")
        print("5- Deletar um funcionário")
        print("6- SAIR")

        escolha = input("Faça uma escolha: ")

        if escolha == "1":
            print("\nPreencha as seguintes informações abaixo :")
            nome = str(input("Nome : "))
            while not validar_nome(nome) :
                nome = str(input("Nome : "))
            idade = input("Idade: ")
            while True :
                try :
                    idade=int(idade)
                    break
                except ValueError :
                    print("A idade tem de apresentar um valor inteiro! Tente novamente.")
                    idade = input("Idade: ")
            salario = input("Salário: ")
            cargo = input("Cargo: ")

            NIF = input("NIF: ")
            while True:
                if len(NIF) != 9 or not NIF.isdigit():
                    print("O NIF deve conter 9 dígitos numéricos e deve apresentar um valor inteiro. Tente novamente.")
                    NIF = input("NIF: ")
                else:
                    break


            funcionario=Funcionario(nome,idade,salario,cargo,NIF)
            if validar_dados(nome, idade, NIF):
                novo_funcionario = Funcionario(str(nome), int(idade), salario, cargo,NIF)
                funcionarios.append(novo_funcionario)
                gravar_funcionario(FICHEIRO, funcionarios)
                print("\nFuncionário adicionado com sucesso!")
            else:
                print("Erro ao cadastrar funcionário. Verifique os dados e tente novamente!")

        elif escolha == "2":
            funcionarios = carregar_funcionarios(FICHEIRO)
            if not funcionarios:
                print("\nNenhum funcionário cadastrado.")
            else:
                print("\nLista de funcionários:")
                for func in funcionarios:
                    print("-" * 40)
                    print(f"Nome: {func.nome}")
                    print(f"Idade: {func.idade}")
                    print(f"Salário: {func.salario}")
                    print(f"Cargo: {func.cargo}")
                    print(f"NIF: {func.NIF}")
                    print("-" * 40)


        elif escolha == "3":
            funcionarios_carregados = carregar_funcionarios(FICHEIRO)
            if funcionarios_carregados:
                funcionarios.extend(funcionarios_carregados)
                print("\nFuncionários carregados com sucesso!")

        elif escolha == "4":
            if not funcionarios:
                print("Nenhum funcionário cadastrado para atualizar.")
            else:
                print("\nLista de funcionários disponíveis para atualização:")
                for i, func in enumerate(funcionarios):
                    print(f"{i + 1}. {func.nome}")

                try:
                    opcao = int(input("\nEscolha o número do funcionário que deseja atualizar: "))
                    if 1 <= opcao <= len(funcionarios):
                        funcionario = funcionarios[opcao - 1]
                        atualizar_funcionarios(funcionario)
                    else:
                        print("Opção inválida. Escolha um número válido.")
                except ValueError:
                    print("Digite um número válido.")
        elif escolha == "5" :
            if not funcionarios:
                print("Não há nenhum funcionário cadastrado para eliminar.")
            else:
                print("\nLista de funcionários disponíveis para eliminar:")
                for i, func in enumerate(funcionarios):
                    print(f"{i + 1}. {func.nome}")
                try:
                    opcao = int(input("\nEscolha o número do funcionário que deseja eliminar: "))
                    if 1 <= opcao <= len(funcionarios):
                        funcionario = funcionarios[opcao - 1]
                        funcionarios.clear()
                        print("Funcionário eliminado com sucesso!")
                    else:
                        print("Opção inválida. Escolha um número válido.")
                except ValueError:
                    print("Digite um número válido.")
        elif escolha == "6":
            print("Saindo do programa...")
            break


        else:
            print("Opção inválida. Tente novamente!")

def validar_nome(nome):
    if nome.isalpha() and nome.strip() != "" :
        return True
    else:
        print("ERRO! O nome  é obrigatório e deve conter apenas letras.")
        return False


def validar_dados(nome, idade, NIF):
    if not nome or not isinstance(nome, str):
        print(" ERRO! O nome é obrigatório e deve ser uma string válida. ")
    if idade < 18:
        print("ERRO ! O funcionário deve ser maior de idade. ")
        if len(NIF) != 9 or not NIF.isdigit():
         print("ERRO! O NIF é obrigatório e deve conter 9 dígitos numéricos.")
        return False
    return True

def validar_novosdados (nova_idade, novo_NIF) :
    if nova_idade < 18 :
        print("A idade tem de apresentar um valor válido")
        if len(novo_NIF) != 9 or not novo_NIF.isdigit():
            print("ERRO! O NIF deve conter 9 dígitos numéricos.")
        return False
    return True


def add_funcionario(nome, idade, salario, cargo, NIF):
    novo_funcionario = {"Nome": nome, "Idade": idade, "Salário": salario, "Cargo": cargo,  "NIF": NIF}
    Funcionario.append(novo_funcionario)


def gravar_funcionario(FICHEIRO, lista_funcionarios):
    with open(FICHEIRO, "w") as f:
        for funcionario in lista_funcionarios:
            f.write(str(funcionario) + "\n")
    print(f"Funcionários gravados em {FICHEIRO} com sucesso !")

def carregar_funcionarios(FICHEIRO):
    funcionarios = []
    try:
        with open(FICHEIRO, "r") as f:
            for linha in f:
                funcionario = Funcionario.from_string (linha)
                funcionarios.append(funcionario)
        print(f" Funcionários carregados com sucesso de {FICHEIRO} !")
    except FileNotFoundError:
        print(f"O ficheiro {FICHEIRO} não foi encontrado ")
    return funcionarios


       

                 
   
