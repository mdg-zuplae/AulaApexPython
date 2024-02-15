from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/lista')
def lista():
    return render_template('lista.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

app.run(debug=True)