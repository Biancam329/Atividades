Busca Binária Recursiva: Implemente o algoritmo de Busca Binária utilizando recursão
para encontrar o índice de um elemento em uma lista ordenada em tempo $O(\log n)$.


RESPOSTA:
def busca_binaria(lista, alvo, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2
    if lista[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return busca_binaria(lista, alvo, meio + 1, fim)
    else:
        return busca_binaria(lista, alvo, inicio, meio - 1)

numeros = [2, 5, 8, 12, 16, 23, 38, 56]
print(busca_binaria(numeros, 23))  # Saída: 5
