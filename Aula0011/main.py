#Flask é uma biblioteca do Python, para auxiliar na criacao de sistemas WEB
#Framaworks alternativos ao flask = Django e Fast
# biblioteca é um conjunto de classes metodos e funcionalidade para auxiliar na criacao de algo
# framework  = é um conjunto de bibliotecas que auxiliam na criacao de uma funcionalidade
# PIP = repositorio de bibliotecas, pacotes e frameworks Python = https://pypi.org
# instalação do Flask = pip install Flask
# remover Flask = pip uninstall Flask
# uso de blibliotecas e frameworks externos é igual ao uso de pacotes criados internamente
# ou seja, utilizando from e import
# / é o endereco raiz(inicio) de um site, a rota inicial de um site ou sistema linux
# endereco da minha maquina = 127.0.0.1 ou localhost
# porta é por onde libera a entrada para uma determinada aplicacao na sua maquina
# a porta padrao de um site é 80
# o modo de debug ativa o recarregamento automatico e melhora os logs

from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return 'Olá'

@app.route('/pessoa')
def pessoa():
    return 'pagina pessoa '

app.run(host='0.0.0.0', port=80, debug=True)
