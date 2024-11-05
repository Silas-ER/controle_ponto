import sqlite3, os

def create_db():
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()
    
    # tabela de ponto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ponto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            departament TEXT,
            tipo_funcionario TEXT,
            nome_funcionario TEXT,
            hora_entrada TEXT,
            hora_saida TEXT,
            observacao TEXT
        )
    ''')
    conn.commit()

    # tabela de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            department TEXT,
            user TEXT,
            password TEXT
        )
    ''')
    conn.commit()

    # tabela de tipos de contrato
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contrato (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contract TEXT
        )
    ''')
    conn.commit()
    
    # insert de tipos de contrato
    cursor.execute("INSERT INTO contrato (contract) VALUES ('AVULSO')")
    cursor.execute("INSERT INTO contrato (contract) VALUES ('CTPS')")
    conn.commit()

    # tabela de tipos de setores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            departamento TEXT
        )
    ''')
    conn.commit()

    # tabela de funcionarios cadastrados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            contrato INTEGER,
            departamento INTEGER,
            FOREIGN KEY (contrato) REFERENCES contrato(id),
            FOREIGN KEY (departamento) REFERENCES departamento(id)
        )
    ''')
    conn.commit()

    conn.close()

if __name__ == '__main__':
    create_db()