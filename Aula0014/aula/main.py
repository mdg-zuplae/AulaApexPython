from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/listar')
def listar():
    return render_template('listar.html')

@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')

app.run(debug=True)