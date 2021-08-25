from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime 
import funcoes


app = Flask(__name__)
timeObj = datetime.now()
mesAtualStr = timeObj.strftime('%B').upper()
timeString = timeObj.strftime("%H:%M:%S.%f - %b %d %Y")

@app.route('/', methods=['GET', 'POST'])
def home(): #ta funcionando ok
    if request.method == 'GET':
        return render_template('home.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro(): #ta funcionando ok
    if request.method == 'GET':
        return render_template('signup.html')

    elif request.method == 'POST':
        nomeUsuario = request.form['nome']
        user = request.form['username']
        conta = request.form['email']
        segredo = request.form['senha']
        
        farma = [nomeUsuario, user, conta, segredo]
        farma = ','.join(farma)
        with open('database.csv', 'a') as dados:
            dados.write('\n')
            dados.write(farma)

        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login(): #ta funcionando ok
    if request.method == 'GET':
        return render_template('login.html')
        
    elif request.method == 'POST':
        login = request.form['login']
        password = request.form['pw']
        user = login, password

        secret = funcoes.encriptando(password)
        historico = []
        historico.append(login)
        historico.append(timeString)
        historico = ','.join(historico)
    
        with open('database.csv', 'r', encoding='utf-8') as farmadb: 
            farmadb = farmadb.readlines()
            farmaceutica = funcoes.arrumarcsv(farmadb)

        if user[0] in farmaceutica and user[1] in farmaceutica:
            with open('acessos.csv', 'a', encoding='utf-8') as acessos:
                acessos.write('\n')
                acessos.write(historico)

            with open('senhastemporarias.txt', 'w', encoding='utf-8') as controle:
                controle.write(secret)           

            return redirect(url_for("inicio", encriptada=secret))

        else:
            return redirect(url_for('senhaincorreta'))

@app.route('/inicio', methods=['GET', 'POST'])
def inicio(): #ta funcionando ok
    encriptada = request.args.get('encriptada')
    if request.method == 'GET':
        return render_template('inicial.html', encriptada = encriptada)
    elif request.method == 'POST':
        senhacontrole = request.form['segredo']
        basicaf = request.form['basic']

        with open('senhastemporarias.txt', 'r', encoding='utf-8') as controle:
            controle = controle.read()

            if senhacontrole in controle and basicaf:
                return redirect(url_for('farmaciabasica'))
            
            else:
               return redirect(url_for('senhaincorreta'))


@app.route('/farmaciabasica', methods=['GET', 'POST'])
def farmaciabasica(): #ta funcionando ok
    if request.method == 'GET':
        return render_template('cons_regist.html') 
    elif request.method == 'POST':
        entraramb = request.form['entradab']
        consumiramb = request.form['consumob']
        razaob = request.form['motivob']
        sairamb = request.form['saidab']

        templatecsv = [mesAtualStr, entraramb, consumiramb, sairamb, razaob]
        templatecsv = ','.join(templatecsv)

        with open ('basicdb.csv', 'a') as basica:
            basica.write('\n')
            basica.write(templatecsv)
        
        return redirect(url_for('sucesso'))

@app.route('/sucesso')
def sucesso():
    return '<h1>Registro de medicamentos feito com sucesso!</h1>'    

@app.route('/erro')
def erro():
    return '<h1>Página não encontrada ou em construção, perdão!</h1>'

@app.route('/senhaincorreta')
def senhaincorreta():
    return '<h1>Senha inserida está incorreta, por favor, volte e tente novamente!</h1>'

if __name__ == ('__main__'):
    app.run(debug=True)