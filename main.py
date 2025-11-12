
from flask import Flask, request, jsonify
from tarefa import buscar_tarefas, buscar_tarefa, criar_tarefa, apagar_tarefa, atualizar_tarefa

app = Flask(__name__)

@app.route("/", methods=['GET'])
def home():
    return jsonify({'message': 'Bem-vindo à API!'})

@app.route("/api", methods=['GET'])
def index():
    return jsonify({'message': 'API rodando'})

@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = buscar_tarefas()
    return jsonify(tarefas), 200

@app.route('/api/tarefas/<int:tarefa_id>', methods=['GET'])
def get_tarefa(tarefa_id):
    tarefa = buscar_tarefa(tarefa_id)
    if tarefa:
        return jsonify(tarefa), 200
    return jsonify({'message': 'Tarefa não encontrada'}), 404

@app.route('/api/tarefas', methods=['POST'])
def create_tarefa():
    corpo = request.get_json() or {}
    tarefa_name = corpo.get('name')
    tarefa_description = corpo.get('description')

    if not tarefa_name:
        return jsonify({'message': 'O campo name é obrigatório.'}), 400

    new_id = criar_tarefa(tarefa_name, tarefa_description)
    return jsonify({'message': 'Tarefa cadastrada', 'id': new_id}), 201

@app.route('/api/tarefas/<int:tarefa_id>', methods=['DELETE'])
def delete_tarefa(tarefa_id):
    ok = apagar_tarefa(tarefa_id)
    if ok:
        return jsonify({'message': 'Tarefa apagada com sucesso'}), 200
    return jsonify({'message': 'Tarefa não encontrada'}), 404

@app.route('/api/tarefas/<int:tarefa_id>', methods=['PUT'])
def update_tarefa(tarefa_id):
    corpo = request.get_json() or {}
    tarefa_name = corpo.get('name')
    tarefa_description = corpo.get('description')

    if not tarefa_name:
        return jsonify({'message': 'O campo name é obrigatório.'}), 400

    ok = atualizar_tarefa(tarefa_id, tarefa_name, tarefa_description)
    if ok:
        return jsonify({'message': 'Tarefa atualizada com sucesso'}), 200
    return jsonify({'message': 'Tarefa não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
