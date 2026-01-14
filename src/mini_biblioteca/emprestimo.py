from mini_biblioteca.livro import Livro
from mini_biblioteca.usuario import Usuario

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario):
        self.livro = livro
        self.usuario = usuario
        self.ativo = True
        self.livro.disponivel = False

    def devolver(self):
        self.ativo = False
        self.livro.disponivel = True