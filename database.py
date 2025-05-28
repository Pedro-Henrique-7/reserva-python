import sqlite3  # Importa o módulo para trabalhar com banco SQLite

def criar_banco():
    # Abre conexão com o banco de dados (se o arquivo não existir, ele cria)
    conn = sqlite3.connect('reserva_recursos.db')
    cursor = conn.cursor()  # Cria um cursor para executar comandos SQL

    # Cria a tabela 'recursos' caso não exista
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recursos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  # ID automático e único para cada recurso
            nome TEXT NOT NULL,                    # Nome do recurso (ex: Sala 1)
            descricao TEXT                        # Descrição opcional do recurso
        )
    ''')

    # Cria a tabela 'reservas' caso não exista
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,  # ID automático para cada reserva
            recurso_id INTEGER NOT NULL,             # ID do recurso reservado (chave estrangeira)
            usuario_nome TEXT NOT NULL,              # Nome do usuário que fez a reserva
            data TEXT NOT NULL,                      # Data da reserva (formato string para simplicidade)
            hora_inicio TEXT NOT NULL,               # Hora de início da reserva
            hora_fim TEXT NOT NULL,                  # Hora de fim da reserva
            status TEXT NOT NULL,                    # Status da reserva (ex: Confirmado)
            FOREIGN KEY (recurso_id) REFERENCES recursos(id)  # Define relação com a tabela recursos
        )
    ''')

    conn.commit()  # Salva as alterações feitas no banco
    conn.close()   # Fecha a conexão com o banco


def listar_recursos():
    conn = sqlite3.connect('reserva_recursos.db')
    cursor = conn.cursor()


    cursor.execute('SELECT id, nome, descricao FROM recursos')
    recursos = cursor.fetchall()

    conn.close()
    return recursos


def adicionar_recursos(nome, descricao):
    conn = sqlite3.connect('reserva_recursos.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO recursos (nome, descricao) VALUES (?, ?)', (nome, descricao))
    conn.commit()
    conn.close()

def reservar_recurso(recurso_id, usuario_nome, data):
    conn = sqlite3.connect('reserva_recursos.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO reservas (recurso_id, usuario_nome, data)
        VALUES (?, ?, ?)
    ''', (recurso_id, usuario_nome, data))

    conn.commit()
    conn.close()


if __name__ == '__main__':
    criar_banco()  # Executa a função que cria o banco e tabelas quando o script é rodado direto
    print("Banco e tabelas criados com sucesso!")
