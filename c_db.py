import sqlite3

# Criação ou recriação do db caso necessário!
def create_db():
    conn = sqlite3.connect('ponto.db')
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

# CRUD
def create_register():
    pass

def read_register():
    pass 

def update_register():
    pass

def delete_register():
    pass
