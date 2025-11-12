from conexao import get_conexao
from psycopg2.extras import RealDictCursor
from flask import jsonify

def buscar_tarefas():
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT id, name, description FROM tarefas;")
    tarefas = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(tarefas)

def create(name, description):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tarefas (nome, descricao) VALUES (%s, %s)",
        (name, description)
    )
    conn.commit()
    cursor.close()
    conn.close()
