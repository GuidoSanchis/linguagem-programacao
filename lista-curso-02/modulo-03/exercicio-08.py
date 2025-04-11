class Livro:
    def __init__(self, titulo: str, autor: str, paginas: int):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self) -> str:
        return f"\"{self.titulo}\" — {self.autor} ({self.paginas} páginas)"

    def __len__(self) -> int:
        return self.paginas


if __name__ == "__main__":
    # Instanciando um livro
    meu_livro = Livro("Segredos da Mente Milionária", "T. Harv Eker", 176)
    
    # Exibindo detalhes via __str__
    print(meu_livro)  
    
    # Usando __len__ para obter número de páginas
    print(f"Número de páginas: {len(meu_livro)}")