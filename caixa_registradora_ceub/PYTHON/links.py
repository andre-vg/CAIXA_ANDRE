import sql
import mysql.connector
from flask import Flask, render_template, request
from datetime import datetime
import webbrowser

app = Flask(__name__)

url = 'http://localhost:5000/'
webbrowser.register('chrome',
                    None,
                    webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome').open(url)


@app.route('/login', methods=['POST'])
def login():
    global usuario
    global senha
    usuario = request.form.get('username', '')
    senha = request.form.get('password', '')
    print(usuario)
    print(senha)

    cnx = mysql.connector.connect(user='qZAqwXH0Wi', password='O387pnW1tb',
                                  host='remotemysql.com',
                                  database='qZAqwXH0Wi')

    print("Conectado=", cnx.is_connected())

    cs = cnx.cursor(buffered=True)

    sql = "SELECT idt_funcionario, nme_funcionario, username, senha FROM tb_funcionario where" \
          " username = %s and senha = md5(%s); "

    cs.execute(sql, (usuario, senha))

    dados = cs.fetchone()

    cs.close()
    cnx.close()

    if dados is not None:
        global idt_funcionario
        idt_funcionario = dados[0]
        global nome_funcionario
        nome_funcionario = dados[1]
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
        msg = "Cliente " + nme + " cadastrado(a) com sucesso!"
    else:
        msg = "Falha na inclusão do cliente."

    return msg


@app.route('/pagar', methods=['POST'])
def pagar():
    data = str(datetime.now())

    global espresso, vlr_espresso
    global torta, vlr_torta
    global agua, vlr_agua
    global cookie, vlr_cookie

    espresso = request.form['qtd_espresso']
    torta = request.form['qtd_torta']
    agua = request.form['qtd_agua']
    cookie = request.form['qtd_cookie']
    vlr_espresso = int(espresso) * 2.00
    vlr_torta = int(torta) * 5.00
    vlr_agua = int(agua) * 1.00
    vlr_cookie = int(cookie) * 3.50
    vlr_total = vlr_espresso + vlr_torta + vlr_agua + vlr_cookie
    if round((int(vlr_total) / 15) * 3) == 0:
        vlr_token = 1
    else:
        vlr_token = round((int(vlr_total) / 15) * 3)

    return render_template('pagar.html', nome_funcionario=nome_funcionario, data=data,
                           espresso=espresso, torta=torta, agua=agua, cookie=cookie, vlr_torta=vlr_torta,
                           vlr_espresso=vlr_espresso,
                           vlr_agua=vlr_agua, vlr_total=vlr_total, vlr_token=vlr_token, vlr_cookie=vlr_cookie)


@app.route('/buscar', methods=['POST'])
def buscar():
    # Recuperando dados vindos do Ajax
    parte = request.form['parte']

    # Incluindo pessoa no SGBD
    mysql = sql.SQL("qZAqwXH0Wi", "O387pnW1tb", "qZAqwXH0Wi")
    comando = "SELECT * FROM tb_cliente WHERE CPF LIKE CONCAT('%', %s, '%') ORDER BY CPF;"
    cs = mysql.consultar(comando, [parte])
    print(cs)
    global dados
    dados = cs.fetchone()
    if dados == None:
        saida = ""
    else:
        saida = str(dados[0]) + ',' + dados[1] + ',' + dados[2] + ',' + str(dados[3]) + ',' + dados[4]

    return saida


@app.route('/sucesso')
def teste():
    data = str(datetime.now())
    idt_cliente = dados[0]
    nme = dados[1]
    end = dados[2]
    token = dados[3]
    cpf = dados[4]

    print(nme, end, token, cpf)
    print(espresso, vlr_espresso, torta, vlr_torta)
    vlr_total = vlr_espresso + vlr_torta + vlr_agua + vlr_cookie
    vlr_token = round((int(vlr_total) / 15) * 3)
    recebe_token = (int(vlr_total) / 15)
    recebe_token = round(recebe_token)

    idt_espresso = 1
    idt_torta = 2
    idt_agua = 3
    idt_cookie = 4

    mysql = sql.SQL("qZAqwXH0Wi", "O387pnW1tb", "qZAqwXH0Wi")
    comando = "/*!40103 SET TIME_ZONE='-03:00' */;"
    mysql.executar(comando, [])
    comando = "INSERT INTO tb_pedido (cod_funcionario, cod_cliente, DataHora, vlr_total, vlr_total_token) " \
              "VALUES (%s, %s, current_timestamp, %s, %s);"
    mysql.executar(comando, [idt_funcionario, idt_cliente, vlr_total, vlr_token])

    comando = "INSERT INTO ta_pedido_produto (cod_pedido, cod_produto, qtd_produto)" \
              "VALUES (LAST_INSERT_ID(), %s, %s);"
    mysql.executar(comando, [idt_espresso, espresso])

    comando = "INSERT INTO ta_pedido_produto (cod_pedido, cod_produto, qtd_produto)" \
              "VALUES (LAST_INSERT_ID(), %s, %s);"
    mysql.executar(comando, [idt_torta, torta])

    comando = "INSERT INTO ta_pedido_produto (cod_pedido, cod_produto, qtd_produto)" \
              "VALUES (LAST_INSERT_ID(), %s, %s);"
    mysql.executar(comando, [idt_agua, agua])

    comando = "INSERT INTO ta_pedido_produto (cod_pedido, cod_produto, qtd_produto)" \
              "VALUES (LAST_INSERT_ID(), %s, %s);"
    mysql.executar(comando, [idt_cookie, cookie])

    comando = "update tb_cliente set qtd_token = qtd_token + %s where idt_cliente = %s;"
    mysql.executar(comando, [recebe_token, idt_cliente])

    return render_template('sucesso.html', data=data, nme=nme, nome_funcionario=nome_funcionario, vlr_total=vlr_total,
                           vlr_token=vlr_token, recebe_token=recebe_token)


@app.route('/sucesso_token')
def token():
    data = str(datetime.now())
    idt_cliente = dados[0]
    nme = dados[1]
    end = dados[2]
    token = dados[3]
    cpf = dados[4]

    print(nme, end, token, cpf)
    print(espresso, vlr_espresso, torta, vlr_torta)
    vlr_total = vlr_espresso + vlr_torta + vlr_agua + vlr_cookie
    vlr_token = round((int(vlr_total) / 15) * 3)
    recebe_token = (int(vlr_total) / 15)
    recebe_token = round(recebe_token)

    idt_espresso = 1
    idt_torta = 2
    idt_agua = 3
    idt_cookie = 4

    mysql = sql.SQL("qZAqwXH0Wi", "O387pnW1tb", "qZAqwXH0Wi")
    comando = "/*!40103 SET TIME_ZONE='-03:00' */;"
    mysql.executar(comando, [])
    comando = "INSERT INTO tb_pedido (cod_funcionario, cod_cliente, DataHora, vlr_total, vlr_total_token) " \
              "VALUES (%s, %s, current_timestamp, %s, %s);"
    mysql.executar(comando, [idt_funcionario, idt_cliente, vlr_total, vlr_token])

    comando = "INSERT INTO ta_pedido_produto (cod_pedido, cod_produto, qtd_produto)" \
              "VALUES (LAST_INSERT_ID(), %s, %s);"
    mysql.executar(comando, [idt_espresso, espresso])

    comando = "INSERT INTO ta_pedido_produto (cod_pedido, cod_produto, qtd_produto)" \
              "VALUES (LAST_INSERT_ID(), %s, %s);"
    mysql.executar(comando, [idt_torta, torta])

    comando = "INSERT INTO ta_pedido_produto (cod_pedido, cod_produto, qtd_produto)" \
              "VALUES (LAST_INSERT_ID(), %s, %s);"
    mysql.executar(comando, [idt_agua, agua])

    comando = "INSERT INTO ta_pedido_produto (cod_pedido, cod_produto, qtd_produto)" \
              "VALUES (LAST_INSERT_ID(), %s, %s);"
    mysql.executar(comando, [idt_cookie, cookie])

    comando = "update tb_cliente set qtd_token = qtd_token - %s where idt_cliente = %s;"
    mysql.executar(comando, [vlr_token, idt_cliente])

    return render_template('sucesso_token.html', data=data, nme=nme, nome_funcionario=nome_funcionario,
                           vlr_total=vlr_total,
                           vlr_token=vlr_token, recebe_token=recebe_token)


@app.route('/relatorio')
def relatorio():
    global nme_mes
    data = str(datetime.now())

    date = datetime.now()
    mes = date.strftime("%m")

    if mes == '01':
        nme_mes = str('Janeiro')
        print(nme_mes)
    if mes == '02':
        nme_mes = str('Fevereiro')
        print(nme_mes)
    if mes == '03':
        nme_mes = str('Março')
        print(nme_mes)
    if mes == '04':
        nme_mes = str('Abril')
        print(nme_mes)
    if mes == '05':
        nme_mes = str('Maio')
        print(nme_mes)
    if mes == '06':
        nme_mes = str("Junho")
        print(nme_mes)
    if mes == '07':
        nme_mes = str("Julho")
        print(nme_mes)
    if mes == '08':
        nme_mes = str("Agosto")
        print(nme_mes)
    if mes == '09':
        nme_mes = str("Setembro")
        print(nme_mes)
    if mes == '10':
        nme_mes = str("Outubro")
        print(nme_mes)
    if mes == '11':
        nme_mes = str("Novembro")
        print(nme_mes)
    if mes == '12':
        nme_mes = str("Dezembro")
        print(nme_mes)

    mysql = sql.SQL("qZAqwXH0Wi", "O387pnW1tb", "qZAqwXH0Wi")
    comando = "/*!40103 SET TIME_ZONE='-03:00' */;"
    mysql.executar(comando, [])

    comando = "select current_date();"
    cs = mysql.consultar(comando, [])
    info = cs.fetchone()
    dia = info[0]
    print(dia)

    comando = "select count(*) from tb_pedido where DataHora LIKE CONCAT('%', %s, '%');"
    cs = mysql.consultar(comando, [dia])
    info = cs.fetchone()
    qtd_venda = info[0]

    comando = "select IFNULL(sum(vlr_total),0) from tb_pedido where DataHora LIKE CONCAT('%', %s, '%');"
    cs = mysql.consultar(comando, [dia])
    info = cs.fetchone()
    vlr_venda = info[0]

    comando = "select IFNULL(sum(vlr_total),0) from tb_pedido where DataHora LIKE CONCAT('%2021-', %s, '%');"
    cs = mysql.consultar(comando, [mes])
    info = cs.fetchone()
    vlr_venda_mes = info[0]

    comando = "select count(*) from tb_pedido where DataHora LIKE CONCAT('%2021-', %s, '%');"
    cs = mysql.consultar(comando, [mes])
    info = cs.fetchone()
    qtd_venda_mes = info[0]

    return render_template('relatorios.html', data=data, qtd_venda=qtd_venda, vlr_venda=vlr_venda,
                           nome_funcionario=nome_funcionario, vlr_venda_mes=vlr_venda_mes,
                           qtd_venda_mes=qtd_venda_mes, nme_mes=nme_mes)


app.run(debug=True)
