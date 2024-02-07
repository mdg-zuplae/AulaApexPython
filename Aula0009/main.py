from pessoa import Pessoa
from endereco import Endereco

nome = 'Jorgin'
sobrenome = 'Silva'
idade = 69
endereco = Endereco('Rua do Vini',6969,'ao lado da casa vini', 'Salto', 'Blumenau')

#Composicao - quando uma classe contem outra classe nas suas propriedades
p1 = Pessoa(nome, sobrenome, idade, endereco)

print(p1)