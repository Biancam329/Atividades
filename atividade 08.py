Fatorial de um Número: Peça um número inteiro positivo e calcule o seu fatorial (ex: $5! = 5 \times 4 \times 3 \times 2 \times 1 = 120$)
usando um loop.


RESPOSTA:
n = int(input("Digite um número inteiro positivo: "))
fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f"{n}! = {fatorial}")
