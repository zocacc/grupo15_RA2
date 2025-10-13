"""
Implementação do algoritmo LRU (Least Recently Used) - Aluno C
Cache que remove o item menos recentemente usado quando atinge capacidade máxima
"""

from collections import OrderedDict
import time

class LRUCache:
    """
    Implementação do algoritmo de cache LRU (Least Recently Used)

    O LRU remove o item que foi acessado há mais tempo quando o cache está cheio.
    Utiliza OrderedDict para manter eficiência O(1) nas operações.
    """

    def __init__(self, capacity: int):
        """
        Inicializa o cache LRU

        Args:
            capacity (int): Capacidade máxima do cache
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        self.access_count = 0
        self.hit_count = 0
        self.miss_count = 0
        self.access_times = {}  # Rastrear tempos de acesso

    def get(self, key: int) -> str:
        """
        Recupera um item do cache e marca como recentemente usado

        Args:
            key (int): Chave do item

        Returns:
            str: Valor do item ou None se não encontrado
        """
        self.access_count += 1
        current_time = time.time()

        if key in self.cache:
            # Mover para o final (mais recente)
            value = self.cache.pop(key)
            self.cache[key] = value
            self.access_times[key] = current_time
            self.hit_count += 1
            return value
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
        current_time = time.time()

        if key in self.cache:
            # Atualizar valor e mover para o final
            self.cache.pop(key)
            self.cache[key] = value
            self.access_times[key] = current_time
            return

        # Se cache está cheio, remover o LRU (primeiro item)
        if len(self.cache) >= self.capacity:
            # Remove o item menos recentemente usado
            lru_key = next(iter(self.cache))
            del self.cache[lru_key]
            if lru_key in self.access_times:
                del self.access_times[lru_key]

        # Adicionar novo item (sempre no final = mais recente)
        self.cache[key] = value
        self.access_times[key] = current_time

    def clear(self) -> None:
        """Limpa todo o cache"""
        self.cache.clear()
        self.access_times.clear()

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
            'algorithm': 'LRU',
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

    def get_access_order(self) -> list:
        """
        Retorna as chaves na ordem de acesso (LRU primeiro)

        Returns:
            list: Lista de chaves ordenadas por uso recente
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

    def peek_lru(self) -> int:
        """
        Retorna a chave menos recentemente usada sem removê-la

        Returns:
            int: Chave LRU ou None se cache vazio
        """
        if self.cache:
            return next(iter(self.cache))
        return None

    def get_access_time(self, key: int) -> float:
        """
        Retorna o tempo do último acesso de uma chave

        Args:
            key (int): Chave a consultar

        Returns:
            float: Timestamp do último acesso ou None
        """
        return self.access_times.get(key)

    def __str__(self) -> str:
        """Representação string do cache"""
        return f"LRUCache(capacity={self.capacity}, size={len(self.cache)}, hit_rate={self.get_stats()['hit_rate']:.1f}%)"

    def __repr__(self) -> str:
        return self.__str__()
