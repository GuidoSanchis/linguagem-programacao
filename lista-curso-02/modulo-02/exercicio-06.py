try:
    # Solicita os dois números ao usuário
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Tenta fazer a divisão
    resultado = num1 / num2
    print(f"\nResultado da divisão: {resultado}")

except ZeroDivisionError:
    print("\n Não é possível dividir por zero. Tente outro número.")

except ValueError:
    print("\n Por favor, digite apenas números válidos. Vamos tentar de novo")

else:
    print("\n Divisão realizada com sucesso!")

finally:
    print("Foi!")