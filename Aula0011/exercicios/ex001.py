from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Seja bem-vindo!'

@app.route('/pessoas')
def pessoas():
    return 'Bem-vindo ao módulo de pessoas!'


app.run(host='0.0.0.0', port=8080, debug=True)