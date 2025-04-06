from flask import Flask, request, jsonify, render_template
from Links.funcionario import carregar_funcionarios, Funcionario, gravar_funcionario
from Links.fornecedor import carregar_fornecedores
from Links.ementa import carregar_pratos
app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello_world():
    return 'Hello World Maurília'

FICHEIRO_FORNECEDORES= "fornecedores.txt"
FICHEIRO_PRODUTOS = "produtos.txt"
FICHEIRO = "funcionários.txt"
FICHEIRO_PRATOS = "pratos.txt"


lista_funcionarios = []
lista_fornecedores = []
lista_pratos = []

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
        # Obter os dados enviados no corpo do pedido em formato JSON
        data = request.get_json()

        # Verificar se os campos necessários estão presentes
        nif = data.get('NIF')
        nome = data.get('nome')
        idade = data.get('idade')
        cargo= data.get('cargo')
        salario = data.get('salario')

        if not nif or not nome or not idade or not cargo or not salario :
            return jsonify({'error': 'Faltam informações obrigatórias'}), 400

        # Criar um novo cliente
        novo_funcionario = Funcionario(nif, nome, idade,cargo, salario)
        if novo_funcionario.is_valid() :
            lista_funcionarios.append(novo_funcionario)
            gravar_funcionario(FICHEIRO, lista_funcionarios)

        # Retornar uma resposta de sucesso
        return jsonify({'message': 'Funcionário adicionado com sucesso!'}), 201

    except Exception as e:
        return jsonify({'error': f'Ocorreu um erro: {str(e)}'}), 500



@app.route('/funcionarios4/')
def funcionarios():
    lista_funcionarios = carregar_funcionarios(FICHEIRO)
    return render_template('funcionarios4.html', funcionarios=lista_funcionarios)

@app.route('/fornecedores/')
def fornecedor():
    lista_fornecedores= carregar_fornecedores(FICHEIRO_FORNECEDORES)
    return render_template('fornecedores.html', fornecedores=lista_fornecedores)

@app.route('/pratos/')
def pratos():
    lista_pratos = carregar_pratos()
    return render_template('pratos.html', pratos=lista_pratos)


# main driver functionx\
if __name__ == '__main__':
    app.run()
