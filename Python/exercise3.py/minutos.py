total_segundos = int(input("Digite o número de segundos: "))
horas = total_segundos // 3600
resto_segundos = total_segundos % 3600
minutos = resto_segundos // 60
segundos = resto_segundos % 60


print(f"{total_segundos} segundos equivalem a:")
print(f"{horas} horas, {minutos} minutos e {segundos} segundos.")
