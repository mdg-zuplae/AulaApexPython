from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def inicio():
    return '<h1>Bem-vindo</h1>'

@app.route('/cadastro')
def cadastro():
    return render_template('index.html')


@app.route('/listagem')
def listagem():
    p1 = {'nome':'Dyego', 'sobrenome': 'Rauen'}
    p2 = {'nome':'Maria', 'sobrenome': 'Silva'}
    pessoas = [p1, p2]
    return render_template('listagem.html', lista_pessoas = pessoas)

app.run(debug=True, host='0.0.0.0')