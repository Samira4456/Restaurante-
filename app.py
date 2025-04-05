from flask import Flask, request, jsonify, render_template

from ementa import carregar_pratos
from fornecedor import Fornecedor,carregar_fornecedores,gravar_fornecedor
from funcionario import carregar_funcionarios

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello_world():
    return 'Hello World'

lista_funcionarios = []
lista_pratos = []
lista_fornecedores = []

FICHEIRO_FORNECEDORES= "fornecedores.txt"
FICHEIRO_PRODUTOS = "produtos.txt"
FICHEIRO = "funcionários.txt"
FICHEIRO_PRATOS = "pratos.txt"

@app.route('/funcionar6ios/')
def funcionarios():
    lista_funcionarios = carregar_funcionarios(FICHEIRO)
    return render_template('funcionarios.html', funcionarios=lista_funcionarios)

@app.route('/ementa/')
def ementa():
    lista_pratos  = carregar_pratos(FICHEIRO_PRATOS)
    return render_template('ementa.html', pratos=lista_pratos)

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

if __name__ == '__main__':
    app.run()
