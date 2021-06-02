import flask
import mysql.connector
from flask import Flask, render_template, request
from datetime import datetime


app = Flask(__name__)


@app.route('/login', methods=['POST'])
def login():
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
        nome = dados[0]
        return render_template('index.html', nome_funcionario=nome)
    else:
        return render_template('naoencontrado.html')


@app.route('/')
def principal():
    data = str(datetime.now())

    return render_template('formlogin.html', data=data)


@app.route('/incluir/', methods=['POST'])
def incluir():
    print('I got clicked!')
    nome_cliente = request.form.get('nome_cliente')
    endereco_cliente = request.form.get('endereco_cliente')
    numero_cliente = request.form.get('numero_cliente')
    cpf_cliente = request.form.get('cpf_cliente')

    print(nome_cliente)

    cnx = mysql.connector.connect(user='qZAqwXH0Wi', password='O387pnW1tb',
                                  host='remotemysql.com',
                                  database='qZAqwXH0Wi')

    print("Conectado=", cnx.is_connected())

    cs = cnx.cursor()

    sql = "INSERT INTO tb_cliente (nme_cliente, endereco_cliente, numero_cliente, CPF) " \
          "VALUES (%s, %s, %s, %s);"
    cs.execute(sql, (nome_cliente, endereco_cliente, numero_cliente, cpf_cliente))
    cnx.commit()
    cs.close()
    cnx.close()

    return render_template('incluir.html', nome_cliente=nome_cliente, endereco_cliente=endereco_cliente,
                           numero_cliente=numero_cliente, cpf_cliente=cpf_cliente)

@app.route('/pagar')
def pagar():
    data = str(datetime.now())

    return render_template('pagar.html', data=data)


app.run(debug=True)
