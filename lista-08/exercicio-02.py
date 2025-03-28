# 2. Abertura Segura de Arquivo
# Escreva um programa que solicite ao usuário o nome de um arquivo para leitura. O
# programa deve tentar abrir o arquivo e exibir seu conteúdo. Utilize tratamento de
# exceções para lidar com a ausência do arquivo e outros possíveis erros.

arquivo = input("Digite o nome do arquivo para leitura: ")

try:
    with open(arquivo, 'r') as file:
        conteudo = file.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print(f"Erro: O arquivo '{arquivo}' não foi encontrado.")
except IOError:
    print(f"Erro: Ocorreu um erro ao tentar ler o arquivo '{arquivo}'.")
except Exception as e:
    print(f"Erro inesperado: {e}")