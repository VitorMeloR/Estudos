from flask import Flask, render_template, request, redirect, url_for

import sqlite3

app = Flask(__name__, template_folder='templates')


# Função para buscar dados no banco de dados
def criar_tabela_monofasico():
    conn = sqlite3.connect('monofasico.db')
    cursor = conn.cursor()

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
            passe_campo TEXT,
            espiras_campo TEXT,
            fio_campo TEXT,
            passe_auxiliar TEXT,
            espiras_auxiliar TEXT,
            fio_auxiliar TEXT,
            ligacao TEXT
            
        )
    ''')

    conn.commit()
    conn.close()


def criar_tabela_trifasico():
    conn = sqlite3.connect('trifasico.db')
    cursor = conn.cursor()

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

    conn.commit()
    conn.close()


# Rota para exibir a pagina principal
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/monofasico')
def monof():
    return render_template('monofasico.html')


@app.route('/trifasico')
def trif():
    return render_template('trifasico.html')


# Rota para lidar com o envio do formulário
@app.route('/buscar_monof', methods=['POST'])
def buscar_monof():
    marca_motor = request.form['marca_motor']
    potencia = request.form['potencia']
    modelo = request.form['modelo']
    voltagem = request.form['voltagem']
    amperagem = request.form['amperagem']
    rotacao = request.form['rotacao']
    pacote = request.form['pacote']
    cod_busca = str(marca_motor[0:3] + potencia + modelo.strip() + voltagem[0:3] + amperagem[0:3] + voltagem[4:] +
                    amperagem[4:] + rotacao + pacote)
    print(cod_busca)

    dados_motor = buscar_dados_motor_monof(cod_busca, marca_motor, potencia, modelo, voltagem, amperagem, rotacao,
                                           pacote)

    if dados_motor:
        return render_template('dados_motor.html', dados_motor=dados_motor)
    else:
        return render_template('dados_monof.html', dados=request.form)


# Função para buscar dados no banco de dados
def buscar_dados_motor_monof(cod_busca,  marca_motor, potencia, modelo, voltagem, amperagem, rotacao, pacote):
    conn = sqlite3.connect('monofasico.db')
    cursor = conn.cursor()

    # Buscar dados na tabela motores usando uma consulta parametrizada
    cursor.execute('''
        SELECT * FROM motores
        WHERE cod_busca = ? OR
              marca_motor = ? OR
              potencia = ? OR
              modelo = ? OR
              voltagem = ? OR
              amperagem = ? OR
              rotacao = ? OR
              pacote = ? OR
              passe_campo = ? OR
              espiras_campo = ? OR
              fio_campo = ? OR
              passe_auxiliar = ? OR
              espiras_auxiliar = ? OR
              fio_auxiliar = ? OR
              ligacao = ?
    ''', (cod_busca, '', '', '', '', '', '', '', '', '', '', '', '', '', ''))

    dados_motor = cursor.fetchall()

    conn.close()

    return dados_motor


@app.route('/adicionar', methods=['POST'])
def adicionar_monof():
    marca_motor = request.form['marca_motor']
    potencia = request.form['potencia']
    modelo = request.form['modelo']
    voltagem = request.form['voltagem']
    amperagem = request.form['amperagem']
    rotacao = request.form['rotacao']
    pacote = request.form['pacote']
    passe_campo = request.form['passe_campo']
    espiras_campo = request.form['espiras_campo']
    fio_campo = request.form['fio_campo']
    passe_auxiliar = request.form['passe_auxiliar']
    espiras_auxiliar = request.form['espiras_auxiliar']
    fio_auxiliar = request.form['fio_auxiliar']
    ligacao = request.form['ligacao']
    cod_busca = str(marca_motor[0:3] + potencia + modelo.strip() + voltagem[0:3] + amperagem[0:3] + voltagem[4:] +
                    amperagem[4:] + rotacao + pacote)

    conn = sqlite3.connect('monofasico.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO motores (cod_busca, marca_motor, potencia, modelo, voltagem, amperagem, rotacao, pacote, passe_campo, espiras_campo, 
        fio_campo, passe_auxiliar, espiras_auxiliar, fio_auxiliar, ligacao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (cod_busca, marca_motor, potencia, modelo, voltagem, amperagem, rotacao, pacote, passe_campo, espiras_campo, fio_campo,
          passe_auxiliar, espiras_auxiliar, fio_auxiliar, ligacao))

    conn.commit()
    conn.close()

    return redirect('/')


@app.route('/dados_encontrados')
def dados_encontrados_monofasico():
    marca_motor = request.args.get('marca_motor')
    potencia = request.args.get('potencia')
    modelo = request.args.get('modelo')
    voltagem = request.args.get('voltagem')
    amperagem = request.args.get('amperagem')
    rotacao = request.args.get('rotacao')
    pacote = request.args.get('pacote')
    passe_campo = request.args.get('passe_campo')
    espiras_campo = request.args.get('espiras_campo')
    fio_campo = request.args.get('fio_campo')
    passe_auxiliar = request.args.get('passe_auxiliar')
    espiras_auxiliar = request.args.get('espiras_auxiliar')
    fio_auxiliar = request.args.get('fio_auxiliar')
    ligacao = request.args.get('ligacao')

    dados_motor = buscar_dados_motor_monof(marca_motor, potencia, modelo, voltagem, amperagem, rotacao, pacote)

    return render_template('dados_encontrados.html', dados_motor=dados_motor)


@app.route('/buscar_trif', methods=['POST'])
def buscar_trif():
    marca_motor = request.form['marca_motor']
    potencia = request.form['potencia']
    modelo = request.form['modelo']
    voltagem = request.form['voltagem']
    amperagem = request.form['amperagem']
    rotacao = request.form['rotacao']
    pacote = request.form['pacote']
    cod_busca = str(marca_motor[0:3] + potencia + modelo.strip() + voltagem[0:3] + amperagem[0:3] + voltagem[4:] +
                    amperagem[4:] + rotacao + pacote)
    print(cod_busca)

    dados_motor_trif = buscar_dados_motor_trif(cod_busca, marca_motor, potencia, modelo, voltagem, amperagem, rotacao,
                                           pacote)

    if dados_motor_trif:
        return render_template('dados_motor_tri.html', dados_motor_trif=dados_motor_trif)
    else:
        return render_template('dados_trif.html', dados=request.form)


def buscar_dados_motor_trif(cod_busca,  marca_motor, potencia, modelo, voltagem, amperagem, rotacao, pacote):
    conn = sqlite3.connect('trifasico.db')
    cursor = conn.cursor()

    # Buscar dados na tabela motores usando uma consulta parametrizada
    cursor.execute('''
        SELECT * FROM motores
        WHERE cod_busca = ? OR
              marca_motor = ? OR
              potencia = ? OR
              modelo = ? OR
              voltagem = ? OR
              amperagem = ? OR
              rotacao = ? OR
              pacote = ? OR
              bobina_grupo = ? OR
              grupo_fase = ? OR
              camada = ? OR
              passe = ? OR
              espiras = ? OR
              fio = ? OR
              ligacao = ?
    ''', (cod_busca, '', '', '', '', '', '', '', '', '', '', '', '', '', ''))

    dados_motor_trif = cursor.fetchall()

    conn.close()

    return dados_motor_trif


@app.route('/adicionar_trif', methods=['POST'])
def adicionar_trif():
    marca_motor = request.form['marca_motor']
    potencia = request.form['potencia']
    modelo = request.form['modelo']
    voltagem = request.form['voltagem']
    amperagem = request.form['amperagem']
    rotacao = request.form['rotacao']
    pacote = request.form['pacote']
    bobina_grupo = request.form['bobina_grupo']
    grupo_fase = request.form['grupo_fase']
    camada = request.form['camada']
    passe = request.form['passe']
    espiras = request.form['espiras']
    fio = request.form['fio']
    ligacao = request.form['ligacao']
    cod_busca = str(marca_motor[0:3] + potencia + modelo.strip() + voltagem[0:3] + amperagem[0:3] + voltagem[4:] +
                    amperagem[4:] + rotacao + pacote)

    conn = sqlite3.connect('trifasico.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO motores (cod_busca, marca_motor, potencia, modelo, voltagem, amperagem, rotacao, pacote, bobina_grupo, grupo_fase, 
        camada, passe, espiras, fio, ligacao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (cod_busca, marca_motor, potencia, modelo, voltagem, amperagem, rotacao, pacote, bobina_grupo, grupo_fase, camada,
          passe, espiras, fio, ligacao))

    conn.commit()
    conn.close()

    return redirect('/')


@app.route('/dados_encontrados_trifasico')
def dados_encontrados_trifasico():
    marca_motor = request.args.get('marca_motor')
    potencia = request.args.get('potencia')
    modelo = request.args.get('modelo')
    voltagem = request.args.get('voltagem')
    amperagem = request.args.get('amperagem')
    rotacao = request.args.get('rotacao')
    pacote = request.args.get('pacote')
    bobina_grupo = request.args.get('bobina_grupo')
    grupo_fase = request.args.get('grupo_fase')
    camada = request.args.get('camada')
    passe = request.args.get('passe')
    espiras = request.args.get('espiras')
    fio = request.args.get('fio')
    ligacao = request.args.get('ligacao')

    dados_motor_trif = buscar_dados_motor_trif(marca_motor, potencia, modelo, voltagem, amperagem, rotacao, pacote)

    return render_template('dados_encontrados_trif.html', dados_motor_trif=dados_motor_trif)


@app.route('/verifficar_tabela')
def verificar_tabela():
    criar_tabela_monofasico()
    criar_tabela_trifasico()
    return 'Tabela criada com sucesso!'


if __name__ == '__main__':
    app.run(debug=True)
