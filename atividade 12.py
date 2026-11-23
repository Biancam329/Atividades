Verificador de Anagramas: Crie uma função que receba duas strings e retorne True se 
forem anagramas uma da outra (ex: "amor" e "roma"), ignorando espaços e maiúsculas.


RESPOSTA: 
def sao_anagramas(str1, str2):
    limpa1 = sorted(str1.replace(" ", "").lower())
    limpa2 = sorted(str2.replace(" ", "").lower())
    return limpa1 == limpa2

print(sao_anagramas("Amor", "Roma"))  # Saída: True
