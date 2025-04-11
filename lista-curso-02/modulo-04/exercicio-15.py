import os
import time
import datetime
import calendar

# 1. Exibe o diretório atual
diretorio_atual = os.getcwd()
print(f"📁 Diretório atual: {diretorio_atual}")

# 2. Exibe a data e a hora atuais
agora = datetime.datetime.now()
print(f"\n⏰ Data e hora atuais: {agora.strftime('%d/%m/%Y %H:%M:%S')}")

# 3. Exibe o calendário do mês atual
ano = agora.year
mes = agora.month
print(f"\n📆 Calendário de {calendar.month_name[mes]} {ano}:\n")
print(calendar.month(ano, mes))

# 4. Pausa de 3 segundos
print("⌛ Esperando 3 segundos...")
time.sleep(3)
print("✨ Pronto!")