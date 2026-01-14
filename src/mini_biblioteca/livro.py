class Livro:
    def __init__(self, titulo: str, autor: str, codigo: str):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"Livro: {self.titulo} | Autor: {self.autor} | Status: {status}"