Jogo de Adivinhação: Gere um número aleatório entre 1 e 50 (usando random.randint)
e dê ao usuário até 7 tentativas para acertar, informando a cada erro se o palpite
foi "muito alto" ou "muito baixo".


RESPOSTA:
import random

secreto = random.randint(1, 50)
tentativas = 7

for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}/{tentativas} - Seu palpite: "))
    if palpite == secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite < secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")
else:
    print(f"Fim de jogo! O número era {secreto}.")
