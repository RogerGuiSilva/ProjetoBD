from flask import Flask, request
from tarefa import buscar_tarefas, create, apagar_tarefa, atualizar_tarefa


app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return {
        'message': 'Bem-vindo à API!'
    }


@app.route("/api", methods=['GET'])
def index():

    return {
        'message': 'API rodando'
    }
    
@app.route('/api/tarefas', methods=['GET'])
def get_tarefas():
    tarefas = buscar_tarefas()
    return tarefas



@app.route('/api/tarefa', methods=['GET'])
def get_tarefa():
    tarefa = buscar_tarefas()
    return tarefa

@app.route ('/api/tarefas', methods=['POST'])
def create_tarefa():
    corpo = request.get_json()
    tarefa_name = corpo.get('name')
    tarefa_description = corpo.get('description')
    create(tarefa_name, tarefa_description)
    return {
        'message': 'Tarefa cadastrada'
    }

@app.route ('/api/tarefas/<int:tarefa_id>', methods=['DELETE'])
def delete_tarefa(tarefa_id):
    apagar_tarefa(tarefa_id)
    return {
        'message': 'Tarefa apagada com sucesso'
    }
@app.route ('/api/tarefas/<int:tarefa_id>', methods=['PUT'])
def uptade_tarefa(tarefa_id)
 corpo = request.get_json()
 tarefa_name = corpo.get('name')
 tarefa_description = corpo.get('description')
atualizar_tarefa(tarefa_id,)




if __name__ == '__main__':
    app.run(debug=True)
