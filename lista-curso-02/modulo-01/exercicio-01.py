# Importando os módulos necessários
import math
import random

# Solicita ao usuário um número para calcular a raiz quadrada
numero = float(input("Digite um número para calcular a raiz quadrada: "))

# Calcula a raiz quadrada com o módulo math
raiz_quadrada = math.sqrt(numero)
print(f"A raiz quadrada de {numero} é {raiz_quadrada:.2f}")

# Gera um número aleatório entre 1 e 100 com o módulo random
numero_aleatorio = random.randint(1, 100)
print(f"O número aleatório gerado entre 1 e 100 é: {numero_aleatorio}")