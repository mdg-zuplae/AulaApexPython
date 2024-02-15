from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/cadastro')
def cadastro(): 
    return render_template('cadastro.html')


app.run(host='0.0.0.0', port=80, debug=True)