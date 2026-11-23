Transposição de Matriz: Escreva uma função que receba uma matriz $M \times N$ (lista de listas)
e retorne sua matriz transposta $N \times M$ (trocando linhas por colunas).

RESPOSTA:
def transpor_matriz(matriz):
    return [[linha[i] for linha in matriz] for i in range(len(matriz[0]))]

m = [[1, 2, 3], [4, 5, 6]]
print(transpor_matriz(m))  # Saída: [[1, 4], [2, 5], [3, 6]]
