from mini_biblioteca.livro import Livro
from mini_biblioteca.usuario import Usuario
from mini_biblioteca.emprestimo import Emprestimo

def run():
    usuario1 = Usuario("Relampago McQueen", "01")
    
    livro1 = Livro("Odissséia", "Homero", "02")
    
    print(livro1)
    
    emprestimo1 = Emprestimo(livro1, usuario1)
    print(f"\nEmpréstimo realizado para: {usuario1.nome}")
    print(f"Estado do livro: {'Disponível' if livro1.disponivel else 'Emprestado'}")
    
    emprestimo1.devolver()
    print("\n--- Após a Devolução ---")
    print(f"Empréstimo ativo? {emprestimo1.ativo}")
    print(livro1)

if __name__ == "__main__":
    run()