# tarefa.py
from conexao import get_conexao
from psycopg2.extras import RealDictCursor

def buscar_tarefas():
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT id, name, description FROM tarefas;")
    tarefas = cursor.fetchall()
    cursor.close()
    conn.close()
    return tarefas

def buscar_tarefa(tarefa_id):
    conn = get_conexao()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, name, description FROM tarefas WHERE id = %s;",
        (tarefa_id,)
    )
    tarefa = cursor.fetchone()
    cursor.close()
    conn.close()
    return tarefa

def criar_tarefa(name, description):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tarefas (name, description) VALUES (%s, %s) RETURNING id;",
        (name, description)
    )
    inserted_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return inserted_id

def apagar_tarefa(tarefa_id):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tarefas WHERE id = %s;",
        (tarefa_id,)
    )
    affected = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return affected > 0

def atualizar_tarefa(tarefa_id, name, description):
    conn = get_conexao()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tarefas SET name = %s, description = %s WHERE id = %s;",
        (name, description, tarefa_id)
    )
    affected = cursor.rowcount
    conn.commit()
    cursor.close()
    conn.close()
    return affected > 0
