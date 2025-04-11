# meu_modulo.py

def dobro(n):
    return n * 2


# chamando modulo em outra classe 
# Importando o módulo personalizado
import meu_modulo

# Solicitando um número ao usuário
numero = float(input("Digite um número para ver o dobro: "))

# Usando a função dobro do módulo
resultado = meu_modulo.dobro(numero)

# Exibindo o resultado
print(f"O dobro de {numero} é {resultado}")