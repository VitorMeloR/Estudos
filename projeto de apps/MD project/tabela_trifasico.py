import sqlite3

# Conectar ao banco de dados (isso cria um arquivo exemplo.db se não existir)
conn = sqlite3.connect('trifasico.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Executar um comando SQL para criar a tabela 'motores'
cursor.execute('''
    CREATE TABLE IF NOT EXISTS motores (
        id INTEGER PRIMARY KEY,
        cod_busca TEXT,
        marca_motor TEXT,
        potencia TEXT,
        modelo TEXT,
        voltagem TEXT,
        amperagem TEXT,
        rotacao TEXT,
        pacote TEXT,
        bobina_grupo TEXT,
        grupo_fase TEXT,
        camada TEXT,
        passe TEXT,
        espiras TEXT,
        fio TEXT,
        ligacao TEXT
    )
''')

# Commit para aplicar as alterações e fechar a conexão
conn.commit()
conn.close()