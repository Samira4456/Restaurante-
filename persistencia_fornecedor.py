
from fornecedor import Fornecedor


def gravar_fornecedores(ficheiro,lista_fornecedores) :
     with open (ficheiro,"w") as f:
         for fornecedor in lista_fornecedores :
             f.write(str(fornecedor) + "\n" ) #Grava cada fornecedor como linha

     print(f"Fornecedor gravado em {ficheiro}com sucesso!")

def carregar_fornecedores(ficheiro):
    fornecedores =[]
    try:
        with open (ficheiro,"r") as f :
            for linha in f:
                fornecedor = Fornecedor.from_string(linha)  #De linha para instancia
                fornecedores.append(fornecedor)
        print(f"Fornecedores carregados de {ficheiro}com sucesso!")
    except FileNotFoundError:
        print (f"O ficheiro {ficheiro} não foi encontrado.")
    return fornecedores
