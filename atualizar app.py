from flask import Flask, render_template, request, jsonify
import csv
import os

app = Flask(__name__)

CSV_FILE = 'pratos.csv'

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
    app.run(debug=True)
