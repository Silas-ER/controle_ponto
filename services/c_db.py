import sqlite3, os

def create_db():
    conn = sqlite3.connect('../ponto.db')
    cursor = conn.cursor()
    
    cursor.execute('''
                   DROP TABLE IF EXISTS ponto
                     ''')
    conn.commit()
    
    # tabela de ponto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ponto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT,
            setor INTEGER,
            contrato INTEGER,
            funcionario INTEGER,
            entrada1 TEXT,
            saida1 TEXT,
            entrada2 TEXT,
            saida2 TEXT,
            observacao TEXT,
            FOREIGN KEY (funcionario) REFERENCES funcionario(id),
            FOREIGN KEY (contrato) REFERENCES contrato(id),
            FOREIGN KEY (setor) REFERENCES setor(id)
        )
    ''')
    conn.commit()

    # tabela de usuarios
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            setor TEXT,
            user TEXT,
            password TEXT
        )
    ''')
    conn.commit()

    # tabela de tipos de contrato
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contrato (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contrato TEXT
        )
    ''')
    conn.commit()
    
    """
    # insert de tipos de contrato
    cursor.execute("INSERT INTO contrato (contrato) VALUES ('AVULSO')")
    cursor.execute("INSERT INTO contrato (contrato) VALUES ('CTPS')")
    conn.commit()
    """
    
    # tabela de tipos de setores
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS setor (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            setor TEXT
        )
    ''')
    conn.commit()

    # tabela de funcionarios cadastrados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS funcionario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            contrato INTEGER,
            setor INTEGER,
            FOREIGN KEY (contrato) REFERENCES contrato(id),
            FOREIGN KEY (setor) REFERENCES setor(id)
        )
    ''')
    conn.commit()

    conn.close()

if __name__ == '__main__':
    create_db()