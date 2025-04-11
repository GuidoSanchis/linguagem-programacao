def multiplicador(fator):
    def multiplicar(numero):
        return numero * fator
    return multiplicar

#principal
# Cria uma função que multiplica por 3
multiplica_por_3 = multiplicador(3)

# Cria outra que multiplica por 10
multiplica_por_10 = multiplicador(10)

# Testes com amorzinho
print("Multiplicando por 3:")
print(multiplica_por_3(5))  # Saída: 15

print("\nMultiplicando por 10:")
print(multiplica_por_10(7))  # Saída: 70