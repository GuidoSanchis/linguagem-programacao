# 1. Divisão Segura
# Crie um programa que solicite ao usuário dois números e realize a divisão do
# primeiro pelo segundo. Utilize tratamento de exceções para evitar erros de
# divisão por zero e erros de entrada inválida (como caracteres não numéricos).

numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")

try:
    numero1 = float(numero1)
    numero2 = float(numero2)
    resultado = numero1 / numero2
    print(f"O resultado da divisão de {numero1} por {numero2} é: {resultado}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite números válidos.")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
