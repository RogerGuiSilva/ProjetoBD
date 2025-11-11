from flask import Flask, request
from tarefa import buscar_tarefas, buscar_tarefa

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
    tarefa = buscar_tarefa()
    return tarefa

@app.route ('/api/tarefa/<int:todo_id', methods=['POST'])
def create_tarefa();
    corpo = request.get_json()
    tarefa_name = corpo.get('name')
    tarefa_description = corpo.get('description')
    criar_tarefa(tarefa_name, tarefa_description)
    return {
        'message': 'Tarefa cadastrada'
    }

if __name__ == '__main__':
    app.run(debug=True)
