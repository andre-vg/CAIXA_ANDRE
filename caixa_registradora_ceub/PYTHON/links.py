import sql
import mysql.connector
from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
    global usuario
    usuario = request.form.get('username', '')
    senha = request.form.get('password', '')
    print(usuario)
    print(senha)

    cnx = mysql.connector.connect(user='qZAqwXH0Wi', password='O387pnW1tb',
                                  host='remotemysql.com',
                                  database='qZAqwXH0Wi')

    print("Conectado=", cnx.is_connected())

    cs = cnx.cursor(buffered=True)

    sql = "SELECT nme_funcionario, username, senha FROM tb_funcionario where" \
          " username = %s and senha = %s; "

    cs.execute(sql, (usuario, senha))

    dados = cs.fetchone()

    cs.close()
    cnx.close()

    if dados is not None:
        global nome_funcionario
        nome_funcionario = dados[0]
        return render_template('index.html', nome_funcionario=nome_funcionario)
    else:
        return render_template('naoencontrado.html')


@app.route('/')
def principal():
    data = str(datetime.now())

    return render_template('formlogin.html', data=data)


@app.route('/incluir', methods=['POST'])
def incluir():
    print('I got clicked!')
    nme = request.form['nme']
    end = request.form['end']
    token = request.form['token']
    cpf = request.form['cpf']

    # Incluindo pessoa no SGBD
    mysql = sql.SQL("qZAqwXH0Wi", "O387pnW1tb", "qZAqwXH0Wi")
    comando = "INSERT INTO tb_cliente(nme_cliente, endereco_cliente, qtd_token, CPF) VALUES (%s, %s, %s, %s);"
    if mysql.executar(comando, [nme, end, token, cpf]):
        msg = "Cliente " + nme + " cadastrada com sucesso!"
    else:
        msg = "Falha na inclusão de pessoa."

    return msg

@app.route('/pagar', methods=['POST'])
def pagar():
    data = str(datetime.now())

    
    espresso=request.form['qtd_espresso']
    torta=request.form['qtd_torta']
    agua=request.form['qtd_agua']
    vlr_espresso=int(espresso) * 2.00
    vlr_torta=int(torta) * 5.00
    vlr_agua=int(agua) * 1.00

    

    return render_template('pagar.html', nome_funcionario=nome_funcionario, data=data,
                           espresso=espresso, torta=torta, agua=agua, vlr_torta=vlr_torta, vlr_espresso=vlr_espresso,
                           vlr_agua=vlr_agua)


@app.route('/buscar', methods=['POST'])
def buscar():

  # Recuperando dados vindos do Ajax
  parte = request.form['parte']

  # Incluindo pessoa no SGBD
  mysql = sql.SQL("qZAqwXH0Wi", "O387pnW1tb", "qZAqwXH0Wi")
  comando = "SELECT * FROM tb_cliente WHERE CPF LIKE CONCAT('%', %s, '%') ORDER BY CPF;"
  cs=mysql.consultar(comando, [parte])
  print(cs)
  dados = cs.fetchone()
  if dados == None:
      saida = ""
  else:
      saida = str(dados[0]) + ',' + dados[1] + ',' + dados[2] + ',' + str(dados[3]) + ',' + dados[4]

  return saida


app.run(debug=True)
