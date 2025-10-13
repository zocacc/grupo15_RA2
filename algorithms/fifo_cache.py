"""
Implementação do algoritmo FIFO (First-In, First-Out) - Aluno B
Cache que remove o item mais antigo quando atinge capacidade máxima
"""

from collections import OrderedDict
import time

class FIFOCache:
    """
    Implementação do algoritmo de cache FIFO (First-In, First-Out)

    O FIFO remove o primeiro item inserido quando o cache está cheio,
    independentemente de quão recentemente foi acessado.
    """

    def __init__(self, capacity: int):
        """
        Inicializa o cache FIFO

        Args:
            capacity (int): Capacidade máxima do cache
        """
        self.capacity = capacity
        self.cache = OrderedDict()  # Mantém ordem de inserção
        self.access_count = 0
        self.hit_count = 0
        self.miss_count = 0
        self.insertion_order = {}  # Rastrear ordem de inserção
        self.order_counter = 0

    def get(self, key: int) -> str:
        """
        Recupera um item do cache

        Args:
            key (int): Chave do item

        Returns:
            str: Valor do item ou None se não encontrado
        """
        self.access_count += 1

        if key in self.cache:
            self.hit_count += 1
            return self.cache[key]
        else:
            self.miss_count += 1
            return None

    def put(self, key: int, value: str) -> None:
        """
        Adiciona um item ao cache

        Args:
            key (int): Chave do item
            value (str): Valor do item
        """
        # Se a chave já existe, atualizar valor mas manter posição FIFO
        if key in self.cache:
            self.cache[key] = value
            return

        # Se cache está cheio, remover o primeiro item (FIFO)
        if len(self.cache) >= self.capacity:
            # Remove o primeiro item inserido
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
            if oldest_key in self.insertion_order:
                del self.insertion_order[oldest_key]

        # Adicionar novo item
        self.cache[key] = value
        self.insertion_order[key] = self.order_counter
        self.order_counter += 1

    def clear(self) -> None:
        """Limpa todo o cache"""
        self.cache.clear()
        self.insertion_order.clear()
        self.order_counter = 0

    def size(self) -> int:
        """Retorna o tamanho atual do cache"""
        return len(self.cache)

    def is_full(self) -> bool:
        """Verifica se o cache está cheio"""
        return len(self.cache) >= self.capacity

    def get_stats(self) -> dict:
        """
        Retorna estatísticas do cache

        Returns:
            dict: Estatísticas detalhadas
        """
        hit_rate = (self.hit_count / self.access_count * 100) if self.access_count > 0 else 0

        return {
            'algorithm': 'FIFO',
            'capacity': self.capacity,
            'current_size': len(self.cache),
            'total_accesses': self.access_count,
            'hits': self.hit_count,
            'misses': self.miss_count,
            'hit_rate': hit_rate,
            'keys_in_cache': list(self.cache.keys())
        }

    def reset_stats(self) -> None:
        """Reinicia as estatísticas sem limpar o cache"""
        self.access_count = 0
        self.hit_count = 0
        self.miss_count = 0

    def get_insertion_order(self) -> list:
        """
        Retorna as chaves na ordem de inserção (FIFO)

        Returns:
            list: Lista de chaves ordenadas por inserção
        """
        return list(self.cache.keys())

    def contains(self, key: int) -> bool:
        """
        Verifica se uma chave está no cache

        Args:
            key (int): Chave a verificar

        Returns:
            bool: True se a chave está no cache
        """
        return key in self.cache

    def peek_oldest(self) -> int:
        """
        Retorna a chave mais antiga sem removê-la

        Returns:
            int: Chave mais antiga ou None se cache vazio
        """
        if self.cache:
            return next(iter(self.cache))
        return None

    def __str__(self) -> str:
        """Representação string do cache"""
        return f"FIFOCache(capacity={self.capacity}, size={len(self.cache)}, hit_rate={self.get_stats()['hit_rate']:.1f}%)"

    def __repr__(self) -> str:
        return self.__str__()
