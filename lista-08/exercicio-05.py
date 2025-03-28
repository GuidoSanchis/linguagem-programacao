# 5. Operações Bancárias com Tratamento de Erros
# Crie um programa que simule um sistema bancário simples. O saldo inicial do
# usuário é de R$ 1000,00. O programa deve permitir que o usuário insira um valor
# para saque e, caso o valor solicitado seja maior que o saldo disponível, uma
# exceção personalizada deve ser lançada informando que o saldo é insuficiente.

saldo = 1000.00
saque = input("Digite o valor para saque: ")

try:
    saque = float(saque)
    if saque > saldo:
        raise ValueError("Saldo insuficiente para realizar o saque.")
    saldo -= saque
    print(f"Saque de R$ {saque:.2f} realizado com sucesso. Saldo restante: R$ {saldo:.2f}")
except ValueError as e:
    print(f"Erro: {e}")