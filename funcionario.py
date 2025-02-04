import json  # Para salvar e carregar dados do arquivo

FICHEIRO = "funcionarios.txt"

# Classe Funcionario para armazenar os dados de cada funcionário
class Funcionario:
    def __init__(self, nome, idade, cargo, salario, NIF):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario
        self.NIF = NIF

    def _str_(self):
        return f"{self.nome},{self.idade},{self.cargo},{self.salario},{self.NIF}"


    def from_string(data_str):
        partes = data_str.strip().split(",")
        if len(partes) != 5:
            print("Erro ao carregar fornecedor. Formato inválido.")
            return None
        nome, idade, cargo, salario, NIF = partes
        return Funcionario(nome.strip(), idade.strip(), cargo.strip(), salario.strip(), NIF.strip ())


    # Validação de dados
def validar_dados(nome, idade, NIF):
    if not nome.replace(" ", "").isalpha() or not isinstance(nome, str):
        print("ERRO! O nome é obrigatório e deve ser uma string válida.")
        return False
    if not idade.isdigit() or int(idade) < 18:
        print("ERRO! O funcionário deve ser maior de idade (mínimo 18 anos).")
        return False
    if not NIF.isdigit() or len(NIF) != 9:
        print("ERRO! O NIF deve conter exatamente 9 dígitos numéricos.")
        return False
    return True


# Função para gravar funcionários em um arquivo
def gravar_funcionarios(ficheiro, lista_funcionarios):
 with open(ficheiro, "w") as f:
         for funcionario in lista_funcionarios:
             f.write(str(funcionario) + "\n")
 print(f"Funcionários gravados em {ficheiro} com sucesso!")


# Função para carregar funcionários de um arquivo
def carregar_funcionarios(ficheiro):
    try:
        with open(ficheiro, "r") as f:
            funcionarios = json.load(f)  # Carrega JSON do arquivo
            return [Funcionario.from_dict(f) for f in funcionarios]
    except FileNotFoundError:
        print(f"O ficheiro {ficheiro} não foi encontrado.")
        return []
    except json.JSONDecodeError:
        print("Erro ao carregar os funcionários. O ficheiro pode estar corrompido.")
    return []
