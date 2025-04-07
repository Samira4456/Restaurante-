from flask import jsonify
import csv
import os

class Prato:
    def __init__(self, id, nome, descricao, preco):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    @staticmethod
    def is_valid(prato):
        return (
            isinstance(prato.nome, str) and prato.nome.strip() and
            isinstance(prato.descricao, str) and prato.descricao.strip() and
            isinstance(prato.preco, (int, float)) and prato.preco > 0
        )

class Ementa:
    def __init__(self):
        self.pratos = self.carregar_pratos()

    def carregar_pratos(self):
        pratos = []
        if not os.path.exists('pratos.csv'):
            return pratos
        with open('pratos.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 4:
                    prato = Prato(int(row[0]), row[1], row[2], float(row[3]))
                    pratos.append(prato)
        return pratos

    def salvar_pratos(self):
        with open('pratos.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for prato in self.pratos:
                writer.writerow([prato.id, prato.nome, prato.descricao, prato.preco])

    def adicionar_prato(self, nome, descricao, preco):
        novo_id = max([prato.id for prato in self.pratos], default=0) + 1
        novo_prato = Prato(novo_id, nome, descricao, preco)
        if Prato.is_valid(novo_prato):
            self.pratos.append(novo_prato)
            self.salvar_pratos()
            return jsonify({'message': 'Prato adicionado com sucesso!'}), 201
        return jsonify({'error': 'Dados inválidos'}), 400

    def remover_prato_por_id(self, id_prato):
        pratos_filtrados = [p for p in self.pratos if p.id != id_prato]
        if len(pratos_filtrados) == len(self.pratos):
            return jsonify({'error': 'Prato não encontrado!'}), 404
        self.pratos = pratos_filtrados
        self.salvar_pratos()
        return jsonify({'message': 'Prato removido com sucesso!'}), 200
