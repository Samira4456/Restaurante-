from flask import Flask, render_template, request, jsonify
from ementa import Ementa

app = Flask(__name__)

@app.route("/")
def index():
    ementa = Ementa()
    lista_pratos = ementa.carregar_pratos()
    return render_template("pratos4.html", pratos=lista_pratos)

@app.route("/adicionar_novo_prato", methods=["POST"])
def adicionar_novo_prato():
    data = request.get_json()
    nome = data.get("nome")
    descricao = data.get("descricao")
    try:
        preco = float(data.get("preco"))
    except (ValueError, TypeError):
        return jsonify({"error": "Preço inválido"}), 400

    ementa = Ementa()
    return ementa.adicionar_prato(nome, descricao, preco)

@app.route("/remover_prato/<int:id_prato>", methods=["DELETE"])
def remover_prato(id_prato):
    ementa = Ementa()
    return ementa.remover_prato_por_id(id_prato)

if __name__ == "__main__":
    app.run(debug=True)
