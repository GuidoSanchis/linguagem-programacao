import struct

# Lista de números inteiros
numeros = [10, 20, 30, 40, 50]

# Abre (ou cria) o arquivo binário para escrita
with open("dados.bin", "wb") as arquivo:
    for numero in numeros:
        # 'i' = inteiro (4 bytes), escreve cada número em formato binário
        arquivo.write(struct.pack('i', numero))

print(" Números gravados com sucesso no arquivo binário!")


import struct

# Abre o arquivo binário para leitura
with open("dados.bin", "rb") as arquivo:
    numeros_lidos = []

    while True:
        bytes_lidos = arquivo.read(4)  # Lê 4 bytes por inteiro

        if not bytes_lidos:
            break  # Fim do arquivo

        numero = struct.unpack('i', bytes_lidos)[0]  # Desempacota o inteiro
        numeros_lidos.append(numero)

print(" Números lidos do arquivo binário:")
print(numeros_lidos)