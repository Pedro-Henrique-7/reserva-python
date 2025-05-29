import mysql.connector
from datetime import date

def conectar():
    return mysql.connector.connect(
        host="34.66.199.250", #banco de dados provisionado em nuvem googlcloud a fins de teste
        user="pedro", 
        password="123",
        database="reserva_recursos"
    )

def listar_recursos(data):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    query = '''
        SELECT r.id, r.nome, r.descricao,
        CASE
            WHEN EXISTS (
                SELECT 1 FROM reservas res
                WHERE res.recurso_id = r.id AND res.data = %s
            ) THEN 'Reservado'
            ELSE 'Disponível'
        END AS status
        FROM recursos r;            

    '''
    cursor.execute(query,(data,))
    recursos = cursor.fetchall()
    conn.close()
    return recursos

def adicionar_recursos(nome, descricao):
    conn = conectar()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("INSERT INTO recursos (nome, descricao) VALUES (%s, %s)", (nome, descricao))
    conn.commit()
    conn.close()

def reservar_recurso(recurso_id, usuario_nome, data, hora_inicio, hora_fim):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservas (recurso_id, usuario_nome, data, hora_inicio, hora_fim)
        VALUES (%s, %s, %s, %s, %s)
    """, (recurso_id, usuario_nome, data, hora_inicio, hora_fim))
    conn.commit()
    conn.close()
