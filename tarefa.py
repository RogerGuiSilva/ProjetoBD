from flask import jsonify

def buscar_tarefas():
    tarefas = [
        {
            'id': 1,
            'nome': 'Aprender digitação',
            'descricao': 'Vamos aumentar o zoom para não errar a digitação',
            'status': 'Pendente'
        },
        {
            'id': 2,
            'nome': 'Aprender Python',
            'descricao': 'Aprender python para programar apis',
            'status': 'Pendente'
        }
    ]

    return jsonify(tarefas)

def buscar_tarefa():
    tarefa = {
        'id': 1,
        'nome': 'Aprender digitação',
        'descricao': 'Vamos aumentar o zoom para não errar a digitação',
        'status': 'Pendente'
    }
    return jsonify(tarefa)