Conversor de Tempo: Leia uma quantidade inteira de segundos (ex: 3665) e converta para o formato Horas:Minutos:Segundos (1:1:5).

RESPOTA:
total_segundos = int(input("Digite o tempo em segundos: "))

horas = total_segundos // 3600
resto = total_segundos % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas}:{minutos}:{segundos}")
