#jinja
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    nome_pagina = 'HOME'
    nome_usuario = 'Jorge'
    return render_template('index.html', nome = nome_pagina, usuario=nome_usuario)

@app.route('/listar')
def cadastrar():
    lista = ['Skol', 'Schin', 'Bavaria', 'Kaiser', 'Glacial']
    return render_template('listar.html', nome = 'Listagem', lista = lista)

app.run(debug=True)


