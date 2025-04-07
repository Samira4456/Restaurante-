from flask import Flask, request, jsonify, render_template
from funcionario import carregar_funcionarios, Funcionario, gravar_funcionario, validar_dados
from fornecedor import Fornecedor,carregar_fornecedores,gravar_fornecedor
import csv
import os

app = Flask(__name__, template_folder='templates')

CSV_FILE = 'pratos.csv'

@app.route('/')
def hello_world():
    return 'Hello World'

lista_funcionarios = []
lista_fornecedores = []

FICHEIRO_FORNECEDORES= "fornecedores.txt"
FICHEIRO = "funcionários.txt"


# Funções HTML do Funcionário
@app.route('/remove_funcionario', methods=['DELETE'])
def remove_funcionario():
    try:
        # Obter o NIF enviado pelo frontend
        data = request.get_json()
        NIF = data.get('NIF')

        if not NIF:
            return jsonify({'error': 'NIF não fornecido'}), 400

        # Procurar e remover o cliente da lista
        lista_funcionarios = carregar_funcionarios(FICHEIRO)
        lista_funcionarios = [f for f in lista_funcionarios if f.NIF!= NIF ]
        gravar_funcionario(FICHEIRO, lista_funcionarios)
    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro: {str(e)}'}), 500

    return jsonify({'message': 'Funcionário removido com sucesso!'}), 200



@app.route('/new_funcionario', methods=['POST'])
def new_funcionario():
    try:
        data = request.get_json()
        nome = data.get('nome')
        idade = data.get('idade')
        salario = data.get('salario')
        cargo = data.get('cargo')
        NIF = data.get('NIF')

        if not nome or not idade or not salario or not cargo or not NIF:
            return jsonify({'error': 'Faltam informações obrigatórias'}), 400

        lista_funcionarios = carregar_funcionarios(FICHEIRO)
        try:
            salario = float(salario)
        except ValueError:
            return jsonify({'error': 'Salário inválido'}), 400

        novo_funcionario  = Funcionario( nome, int(idade), salario, cargo, NIF)

        if validar_dados(nome, int(idade), NIF):
            lista_funcionarios.append(novo_funcionario)
            gravar_funcionario(FICHEIRO, lista_funcionarios)

        return jsonify({'message': 'Funcionário adicionado com sucesso!'}), 201

    except Exception as e:
        print(f"Erro: {str(e)}")
        return jsonify({'error': f'Ocorreu um erro: {str(e)}'}), 500

@app.route('/funcionarios4/')
def funcionarios():
    lista_funcionarios = carregar_funcionarios(FICHEIRO)
    return render_template('funcionarios4.html', funcionarios=lista_funcionarios)

@app.route('/fornecedor/')
def fornecedor():
    lista_fornecedores = carregar_fornecedores(FICHEIRO_FORNECEDORES)
    return render_template('Fornecedor4.html', fornecedores=lista_fornecedores)



#FUNÇÕES HTML DO FORNECEDOR
@app.route('/new_fornecedor', methods=['POST'])
def new_fornecedor():
    try:
        data = request.get_json()
        NIF = data.get('NIF')
        nome = data.get('nome')
        telefone = data.get('telefone')
        email = data.get('email')
        tipo_de_produto = data.get('tipo_de_produto')

        if not NIF or not nome or not telefone or not email or not tipo_de_produto:
            return jsonify({'error': 'Faltam informações obrigatórias'}), 400

        lista_fornecedores = carregar_fornecedores(FICHEIRO_FORNECEDORES)

        novo_fornecedor  = Fornecedor(nome, NIF, telefone, email, tipo_de_produto,[])

        if novo_fornecedor.is_valid():
            lista_fornecedores.append(novo_fornecedor)
            gravar_fornecedor(FICHEIRO_FORNECEDORES, lista_fornecedores)

        return jsonify({'message': 'Fornecedor adicionado com sucesso!'}), 201

    except Exception as e:
        print(f"Erro: {str(e)}")
        return jsonify({'error': f'Ocorreu um erro: {str(e)}'}), 500


@app.route('/remove_fornecedor', methods=['DELETE'])
def remove_fornecedor():
    try:

        data = request.get_json()

        NIF = data.get('NIF')

        if not NIF:
            return jsonify({'error': 'NIF não fornecido'}), 400

        lista_fornecedores = carregar_fornecedores(FICHEIRO_FORNECEDORES)


        lista_fornecedores = [f for f in lista_fornecedores if f.NIF != NIF]
        gravar_fornecedor(FICHEIRO_FORNECEDORES, lista_fornecedores)

        return jsonify({'message': 'Fornecedor removido com sucesso!'}), 200

    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro: {str(e)}'}), 500

@app.route('/')
def index():
    lista_fornecedores = carregar_fornecedores(FICHEIRO_FORNECEDORES)
    return render_template('Fornecedor4.html', fornecedores=lista_fornecedores)




#FUNÇÕES HTML PRATOS
class Prato:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

def carregar_pratos():
    pratos = []
    if not os.path.exists(CSV_FILE):
        return pratos
    with open(CSV_FILE, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            pratos.append(Prato(int(row['id']), row['nome'], row['descricao'], float(row['preco'])))
    return pratos

def salvar_pratos(pratos):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'nome', 'descricao', 'preco'])
        for prato in pratos:
            writer.writerow([prato.id, prato.nome, prato.descricao, prato.preco])

@app.route('/')
def index():
    pratos = carregar_pratos()
    return render_template('pratos4.html', pratos=pratos)

@app.route('/adicionar_novo_prato', methods=['POST'])
def adicionar_prato():
    data = request.get_json()
    pratos = carregar_pratos()
    novo_id = max([p.id for p in pratos], default=0) + 1
    novo_prato = Prato(novo_id, data['nome'], data['descricao'], float(data['preco']))
    pratos.append(novo_prato)
    salvar_pratos(pratos)
    return jsonify({"message": "Prato adicionado com sucesso!"})

@app.route('/remover_prato/<int:id>', methods=['DELETE'])
def remover_prato(id):
    pratos = carregar_pratos()
    pratos = [p for p in pratos if p.id != id]
    salvar_pratos(pratos)
    return jsonify({"message": "Prato removido com sucesso!"})


if __name__ == '__main__':
    app.run()
