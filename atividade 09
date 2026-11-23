Simulados de Caixa Eletrônico: dado um valor inteiro de saque em reais, 
informe a menor quantidade possível de cédulas de R$100, R$50, R$20, R$10, R$5 e R$2 
necessárias para compor o valor.

RESPOSTA:
valor = int(input("Valor do saque (R$): "))
cedulas = [100, 50, 20, 10, 5, 2]

for cedula in cedulas:
    quantidade = valor // cedula
    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R$ {cedula}")
        valor %= cedula
