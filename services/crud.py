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

def get_setor_id(nome_setor):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id FROM setor WHERE setor = ?", (nome_setor,))
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.OperationalError as e:
        print(f"Erro ao buscar setor: {e}")
        return None
    finally:
         conn.close()
          
##########################################################################################################################################
 
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

def get_contrato_id(nome_contrato):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id FROM contrato WHERE contrato = ?", (nome_contrato,))
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.OperationalError as e:
        print(f"Erro ao buscar contrato: {e}")
        return None
    finally:
         conn.close()
         
##########################################################################################################################################

# CRUD Genero
def read_generos():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT * FROM genero')
        rows = cursor.fetchall()
    except sqlite3.OperationalError as e:
        print(f"Erro ao ler tipos de genero: {e}")
    finally:
         conn.close()

    return rows

def get_genero_name(genero_id):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    try:
        cursor.execute('SELECT genero FROM genero WHERE id = ?', (genero_id,))
        genero_nome = cursor.fetchone()
        if genero_nome:
            genero_nome = genero_nome[0]
        else:
            genero_nome = None
    except sqlite3.OperationalError as e:
        print(f"Erro ao ler genero: {e}")
        genero_nome = None
    finally:
        conn.close()

    return genero_nome

def get_genero_id(nome_genero):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id FROM genero WHERE genero = ?", (nome_genero,))
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.OperationalError as e:
        print(f"Erro ao buscar genero: {e}")
        return None
    finally:
         conn.close()
         
##########################################################################################################################################

# CRUD Funcionário
def create_funcionario(funcionario, id_genero, id_contrato, id_setor):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execução da query SQL
    try:
        cursor.execute('INSERT INTO funcionario (nome, genero, contrato, setor) VALUES (?, ?, ?, ?)', (funcionario, id_genero, id_contrato, id_setor))
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
               
def get_funcionario_id(nome_funcionario):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT id FROM funcionario WHERE nome = ?", (nome_funcionario,))
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.OperationalError as e:
        print(f"Erro ao buscar funcionario: {e}")
        return None
    finally:
         conn.close()
      
def get_funcionario_name(id_funcionario):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT nome FROM funcionario WHERE id = ?", (id_funcionario,))
        result = cursor.fetchone()
        return result[0] if result else None
    except sqlite3.OperationalError as e:
        print(f"Erro ao buscar nome do funcionário: {e}")
        return None
    finally:
         conn.close()         

##########################################################################################################################################
               
# CRUD Ponto
def create_register(data, id_setor, id_contrato, id_funcionario, id_genero, entrada1, saida1, entrada2, saida2, observacao):
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Execução da query SQL
    try:
        cursor.execute('''
        INSERT INTO ponto (data, setor, contrato, funcionario, genero, entrada1, saida1, entrada2, saida2, observacao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                       ''', (data, id_setor, id_contrato, id_funcionario, id_genero, entrada1, saida1, entrada2, saida2, observacao))
        conn.commit()
    except sqlite3.OperationalError as e:
        print(f"Erro ao inserir setor: {e}")
    finally:
        conn.close()

def read_registers():
    # Caminho do banco de dados
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, '../ponto.db')

    # Conexão ao banco de dados com row_factory
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Para acessar colunas por nome
    cursor = conn.cursor()

    try: 
        cursor.execute('SELECT * FROM ponto')
        rows = cursor.fetchall()
        
        # Convertendo para lista de dicionários para uso no DataFrame
        data = [dict(row) for row in rows]
    except sqlite3.OperationalError as e:
        print(f"Erro ao ler dados de ponto: {e}")
        data = []
    finally:
        conn.close()
         
    return data

def update_register(id, data, id_setor, id_contrato, id_funcionario, entrada1, saida1, entrada2, saida2, observacao):
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE ponto
        SET data = ?, setor = ?, contrato = ?, nome_funcionario = ?, entrada1 = ?, saida1 = ?, entrada2 = ?, saida2 = ? observacao = ?
        WHERE id = ?
    ''', (data, id_setor, id_contrato, id_funcionario, entrada1, saida1, entrada2, saida2, observacao, id))

    conn.commit()
    conn.close()

def delete_register(id):
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM ponto WHERE id = ?', (id,))

    conn.commit()
    conn.close()
