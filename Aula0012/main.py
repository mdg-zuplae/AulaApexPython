from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/pessoa') # uma rota chama a execução de um método
def pessoa():
    return render_template('pessoa.html')

app.run(debug=True)