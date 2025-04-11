# Solicita a entrada do usuário
entrada = input("Digite várias palavras separadas por espaço: ")

# Divide a string em uma lista de palavras
palavras = entrada.split()

# Exibe a lista ordenada alfabeticamente
ordenadas = sorted(palavras)
print(f"\nPalavras em ordem alfabética: {ordenadas}")

# Mostra o número total de palavras
print(f"Total de palavras: {len(palavras)}")

# Converte todas as palavras para maiúsculas
maiusculas = [palavra.upper() for palavra in palavras]
print(f"Palavras em maiúsculas: {maiusculas}")