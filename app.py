from flask import Flask, jsonify, request, abort
from flask_httpauth import HTTPBasicAuth
import json

app = Flask(__name__)
auth = HTTPBasicAuth()

with open('veiculos.json', 'r') as file:
    veiculos = json.load(file)

users = {
    "admin": "MSX123"
}

@auth.verify_password
def verify_password(username, password):
    if username in users and users[username] == password:
        return username

@app.route('/veiculos', methods=['GET'])
@auth.login_required
def get_veiculos():
    return jsonify(veiculos)

@app.route('/veiculos', methods=['POST'])
@auth.login_required
def create_veiculo():
    if not request.json or 'placa' not in request.json:
        abort(400)
    novo_veiculo = {
        'placa': request.json['placa'],
        'marca': request.json.get('marca', ""),
        'fabricante': request.json.get('fabricante', ""),
        'cor': request.json.get('cor', ""),
        'tipo': request.json.get('tipo', ""),
        'combustivel': request.json.get('combustivel', ""),
        'status': "DESCONECTADO"
    }
    veiculos.append(novo_veiculo)
    return jsonify(novo_veiculo), 201

@app.route('/veiculos/<placa>', methods=['GET'])
@auth.login_required
def get_veiculo(placa):
    veiculo = next((v for v in veiculos if v['placa'] == placa), None)
    if veiculo is None:
        abort(404)
    return jsonify(veiculo)

@app.route('/veiculos/<placa>', methods=['PUT'])
@auth.login_required
def update_veiculo_status(placa):
    veiculo = next((v for v in veiculos if v['placa'] == placa), None)
    if veiculo is None:
        abort(404)
    if not request.json or 'status' not in request.json:
        abort(400)
    if request.json['status'] not in ["CONNECTADO", "DESCONECTADO"]:
        abort(400)
    veiculo['status'] = request.json['status']
    return jsonify(veiculo)

@app.route('/veiculos/<placa>', methods=['DELETE'])
@auth.login_required
def delete_veiculo(placa):
    global veiculos
    veiculos = [v for v in veiculos if v['placa'] != placa]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)