Validador de Expressões com Pilha (Stack): Dada uma string contendo parênteses, colchetes 
e chaves (ex: "{[()()]}" ou "{[(])}"), verifique se todos os símbolos foram abertos
e fechados na ordem correta.


RESPOSTA:
def validar_expressao(expr):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expr:
        if char in '([{':
            pilha.append(char)
        elif char in ')]}':
            if not pilha or pilha.pop() != pares[char]:
                return False
    return len(pilha) == 0

print(validar_expressao("{[()()]}"))  # True
print(validar_expressao("{[(])}"))    # False
