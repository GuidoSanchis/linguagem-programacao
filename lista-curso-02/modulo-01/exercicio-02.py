import platform

# Obtendo informações do sistema
nome_sistema = platform.system()
versao_sistema = platform.version()
arquitetura = platform.architecture()[0]

# Exibindo as informações
print("=== Informações do Sistema Operacional ===")
print(f"Nome do sistema operacional: {nome_sistema}")
print(f"Versão do sistema: {versao_sistema}")
print(f"Arquitetura do processador: {arquitetura}")