from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/recuperar')
def recuperar():
    return render_template('recuperar.html')

app.run(debug=True)