TXT
{Linha 1: Olá, mundo!
Linha 2: Estou aprendendo Python.
Linha 3: E estou odiando}

try:
    with open("dados.txt", "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()
        total_linhas = len(linhas)

        print(f"📄 O arquivo tem {total_linhas} linhas.\n")
        print("📝 Conteúdo do arquivo:")
        for linha in linhas:
            print(linha.strip())  # remove o \n com carinho

except FileNotFoundError:
    print("❌ Arquivo 'dados.txt' não encontrado. Verifique o nome ou se ele está na mesma pasta do programa.")