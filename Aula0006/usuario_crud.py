from usuario import Usuario

class CrudUsuario: 
    lista_usuarios = []

    def cadastrar(self, nome, sobrenome, email, senha):
        usuario = Usuario()
        usuario.nome = nome
        usuario.sobrenome = sobrenome
        usuario.email = email
        usuario.senha = senha
        self.lista_usuarios.append(usuario)


    def listar(self):
        return self.lista_usuarios