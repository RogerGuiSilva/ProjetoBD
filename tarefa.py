from conexao import get_conexao
from psycopg2.extras import RealDictCursor
from flask import jsonify

def buscar_tarefas():
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT id, nome, descricao FROM tarefas;")
    tarefas = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(tarefas)


def create(name, description):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tarefas (name, description) VALUES (%s, %s)",
        (name, description)
    )
    conn.commit()
    cursor.close()
    conn.close()


def apagar_tarefa(tarefa_id):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tarefas WHERE id = %s;",
        (tarefa_id,)
    )
    conn.commit()
    cursor.close()
    conn.close()
    def atualizar_tarefa(tarefa_id,name, description):
     conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute(
        "UPTADE todos SET name = %s, description =%s, WHERE id =%s",
        (name, description, tarefa_id)
    )

    conn.commit()
    cursor.close()
    conn.close()
