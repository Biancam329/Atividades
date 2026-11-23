Cache LRU (Least Recently Used): Implemente uma classe LRUCache(capacidade) com os
métodos get(chave) e put(chave, valor) onde ambos operem em tempo $O(1)$, descartando
automaticamente o item menos recentemente usado quando a capacidade máxima for atingida.

RESPOSTA:
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacidade: int):
        self.cache = OrderedDict()
        self.capacidade = capacidade

    def get(self, chave: int) -> int:
        if chave not in self.cache:
            return -1
        self.cache.move_to_end(chave)  # Marca como usado recentemente
        return self.cache[chave]

    def put(self, chave: int, valor: int) -> None:
        if chave in self.cache:
            self.cache.move_to_end(chave)
        self.cache[chave] = valor
        if len(self.cache) > self.capacidade:
            self.cache.popitem(last=False)  # Remove o menos recente

cache = LRUCache(2)
cache.put(1, 10)
cache.put(2, 20)
print(cache.get(1))  # Retorna 10
cache.put(3, 30)     # Remove a chave 2
print(cache.get(2))  # Retorna -1 (não encontrada)
