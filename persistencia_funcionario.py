
from funcionario import Funcionario


def gravar_funcionarios(ficheiro, lista_funcionarios):
    with open(ficheiro, "w") as f:
        for funcionario in lista_funcionarios:
            f.write(str(funcionario) + "\n")
    print(f"Funcionários gravados em {ficheiro} com sucesso !")


def carregar_funcionarios(ficheiro):
    funcionarios = []
    try:
        with open(ficheiro, "r") as f:
            for linha in f:
                funcionario = Funcionario.from_string (linha)
                funcionarios.append(funcionario)
        print(f" Funcionários carregados com sucesso de {ficheiro} !")
    except FileNotFoundError:
        print(f"O ficheiro {ficheiro} não foi encontrado ")
        return funcionarios
