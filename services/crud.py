import sqlite3, os

# CRUD Departamento
def create_department(departamento):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execução da query SQL
    try:
        cursor.execute('INSERT INTO departamento (departamento) VALUES (?)', (departamento,))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Erro ao inserir departamento: {e}")
    finally:
        conn.close()
    
def read_departments():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM departamento')
        rows = cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(f"Erro ao ler departamentos: {e}")
    finally:
         conn.close()

    return rows

def delete_department(id_departamento):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execução da query SQL
    try:
        cursor.execute('DELETE FROM departamento WHERE id = ?', (id_departamento,))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Erro ao deletar departamento: {e}")
    finally:
        conn.close()

def get_department_name(department_id):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT departamento FROM departamento WHERE id = ?', (department_id,))
        departamento_nome = cursor.fetchone()
        if departamento_nome:
            departamento_nome = departamento_nome[0]
        else:
            departamento_nome = None
    except sqlite3.OperationalError as e:
        print(f"Erro ao ler departamento: {e}")
        departamento_nome = None
    finally:
        conn.close()

    return departamento_nome
 
 
# CRUD Contrato
def read_contrato():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM contrato')
        rows = cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(f"Erro ao ler tipos de contrato: {e}")
    finally:
         conn.close()

    return rows

def get_contrato_name(contrato_id):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT contract FROM contrato WHERE id = ?', (contrato_id,))
        contrato_nome = cursor.fetchone()
        if contrato_nome:
            contrato_nome = contrato_nome[0]
        else:
            contrato_nome = None
    except sqlite3.OperationalError as e:
        print(f"Erro ao ler contrato: {e}")
        contrato_nome = None
    finally:
        conn.close()

    return contrato_nome


# CRUD Funcionário
def create_funcionario(funcionario, id_setor, id_contrato):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execução da query SQL
    try:
        cursor.execute('INSERT INTO funcionario (nome, contrato, departamento) VALUES (?, ?, ?)', (funcionario, id_contrato, id_setor))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Erro ao inserir funcionário: {e}")
    finally:
        conn.close()     

def read_funcionarios():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM funcionario')
        rows = cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(f"Erro ao ler funcionários: {e}")
    finally:
         conn.close()

    return rows

def delete_funcionario(id_funcionario):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execução da query SQL
    try:
        cursor.execute('DELETE FROM funcionario WHERE id = ?', (id_funcionario,))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Erro ao inserir funcionário: {e}")
    finally:
        conn.close()    
        

    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT id, nome, contrato, departamento FROM funcionario WHERE id = ?', (id_funcionario,))
        id_funcionario = cursor.fetchone()[0]
    except sqlite3.OperationalError as e:
        print(f"Erro ao ler funcionário: {e}")
    finally:
         conn.close()

    return id_funcionario, nome_funcionario, id_contrato, id_setor
               
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
