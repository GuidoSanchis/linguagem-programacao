def contar_pares(n):
    for i in range(0, n + 1, 2):
        yield i

# Solicita o valor ao usuário
limite = int(input("Digite um número inteiro para ver os pares até ele: "))

print("\nNúmeros pares até", limite, "são:")
for par in contar_pares(limite):
    print(par)