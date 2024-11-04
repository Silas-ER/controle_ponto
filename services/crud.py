import sqlite3, os

# CR Departamento
def create_department(departamento):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conecta ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Executa a query SQL
    try:
        cursor.execute('INSERT INTO departamento (departamento) VALUES (?)', (departamento,))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Erro ao inserir departamento: {e}")
    finally:
        conn.close()
    
def read_departments():
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM departamento')
    rows = cursor.fetchall()

    conn.close()
    return rows

# CRUD Ponto
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
