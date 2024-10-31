import sqlite3

def create_db():
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ponto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            setor TEXT,
            tipo_funcionario TEXT,
            nome_funcionario TEXT,
            hora_entrada TEXT,
            hora_saida TEXT,
            observacao TEXT
        )
    ''')
    conn.commit()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department TEXT,
            user TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    
    conn.close()

def create_register(data, setor, tipo_funcionario, nome_funcionario, hora_entrada, hora_saida, observacao):
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO ponto (data, setor, tipo_funcionario, nome_funcionario, hora_entrada, hora_saida, observacao)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (data, setor, tipo_funcionario, nome_funcionario, hora_entrada, hora_saida, observacao))

    conn.commit()
    conn.close()

def read_registers():
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ponto')
    rows = cursor.fetchall()

    conn.close()
    return rows

def update_register(id, data, setor, tipo_funcionario, nome_funcionario, hora_entrada, hora_saida, observacao):
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE ponto
        SET data = ?, setor = ?, tipo_funcionario = ?, nome_funcionario = ?, hora_entrada = ?, hora_saida = ?, observacao = ?
        WHERE id = ?
    ''', (data, setor, tipo_funcionario, nome_funcionario, hora_entrada, hora_saida, observacao, id))

    conn.commit()
    conn.close()

def delete_register(id):
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM ponto WHERE id = ?', (id,))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_db()