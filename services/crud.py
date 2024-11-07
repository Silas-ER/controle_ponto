import sqlite3, os

# CRUD Setor
def create_setor(setor):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execução da query SQL
    try:
        cursor.execute('INSERT INTO setor (setor) VALUES (?)', (setor,))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Erro ao inserir setor: {e}")
    finally:
        conn.close()
    
def read_setors():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM setor')
        rows = cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(f"Erro ao ler setors: {e}")
    finally:
         conn.close()

    return rows

def delete_setor(id_setor):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execução da query SQL
    try:
        cursor.execute('DELETE FROM setor WHERE id = ?', (id_setor,))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Erro ao deletar setor: {e}")
    finally:
        conn.close()

def get_setor_name(setor_id):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT setor FROM setor WHERE id = ?', (setor_id,))
        setor_nome = cursor.fetchone()
        if setor_nome:
            setor_nome = setor_nome[0]
        else:
            setor_nome = None
    except sqlite3.OperationalError as e:
        print(f"Erro ao ler setor: {e}")
        setor_nome = None
    finally:
        conn.close()

    return setor_nome
 
 
# CRUD Contrato
def read_contratos():
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
        cursor.execute('SELECT contrato FROM contrato WHERE id = ?', (contrato_id,))
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
        cursor.execute('INSERT INTO funcionario (nome, contrato, setor) VALUES (?, ?, ?)', (funcionario, id_contrato, id_setor))
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
def create_register(data, id_setor, id_contrato, id_funcionario, entrada, saida, observacao):
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO ponto (data, setor, contrato, funcionario, entrada, saida, observacao)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (data, id_setor, id_contrato, id_funcionario, entrada, saida, observacao))

    conn.commit()
    conn.close()

def read_registers():
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM ponto')
    rows = cursor.fetchall()

    conn.close()
    return rows

def update_register(id, data, id_setor, id_contrato, id_funcionario, entrada, saida, observacao):
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE ponto
        SET data = ?, setor = ?, contrato = ?, nome_funcionario = ?, entrada = ?, saida = ?, observacao = ?
        WHERE id = ?
    ''', (data, id_setor, id_contrato, id_funcionario, entrada, saida, observacao, id))

    conn.commit()
    conn.close()

def delete_register(id):
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM ponto WHERE id = ?', (id,))

    conn.commit()
    conn.close()
