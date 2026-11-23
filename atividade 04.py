Inversor de Número de 3 Dígitos: Peça um número inteiro de 3 dígitos (ex: 482) e imprima-o invertido (284) 
usando apenas operações matemáticas (// e %), sem converter para string.

RESPOSTA:
num = int(input("Digite um número inteiro de 3 dígitos: "))

centena = num // 100
dezena = (num % 100) // 10
unidade = num % 10

invertido = (unidade * 100) + (dezena * 10) + centena
print(f"Número invertido: {invertido}")
