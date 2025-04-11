# Entrada do usuário
frase = input("Digite uma frase: ")

# Contando vogais com métodos prontos
vogais = "aeiou"
print("\nQuantidade de cada vogal:")
for v in vogais:
    print(f"{v.upper()}: {frase.count(v)}")

# Frase ao contrário (slicing puro amor)
print(f"\nFrase ao contrário: {frase[::-1]}")

# Substituindo espaços por hífens
print(f"\nFrase com espaços substituídos por '-': {frase.replace(' ', '-')}")