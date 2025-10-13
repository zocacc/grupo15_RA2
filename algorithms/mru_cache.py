"""
Implementação do algoritmo MRU (Most Recently Used)
Cache que remove o item mais recentemente usado quando atinge capacidade máxima
"""

from collections import OrderedDict
import time

class MRUCache:
    """
    Implementação do algoritmo de cache MRU (Most Recently Used)

    O MRU remove o item que foi acessado mais recentemente quando o cache está cheio.
    Isso pode ser útil em cenários onde, se um item foi acessado recentemente,
    é provável que não seja necessário em breve.
    """

    def __init__(self, capacity: int):
        """
        Inicializa o cache MRU

        Args:
            capacity (int): Capacidade máxima do cache
        """
        self.capacity = capacity
        self.cache = OrderedDict()
        self.access_count = 0
        self.hit_count = 0
        self.miss_count = 0

    def get(self, key: int) -> str:
        """
        Recupera um item do cache e o marca como o mais recentemente usado.

        Args:
            key (int): Chave do item

        Returns:
            str: Valor do item ou None se não encontrado
        """
        self.access_count += 1
        if key in self.cache:
            # Mover para o final para marcá-lo como o mais recente
            value = self.cache.pop(key)
            self.cache[key] = value
            self.hit_count += 1
            return value
        else:
            self.miss_count += 1
            return None

    def put(self, key: int, value: str) -> None:
        """
        Adiciona ou atualiza um item no cache.

        Se a chave já existe, seu valor é atualizado e ela é movida
        para o final (mais recentemente usada).

        Se a chave não existe e o cache está cheio, o item mais
        recentemente usado (o último) é removido antes da inserção.

        Args:
            key (int): Chave do item
            value (str): Valor do item
        """
        if key in self.cache:
            # Se a chave existe, mova para o final
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Se o cache está cheio, remove o mais recentemente usado (o último)
            self.cache.popitem(last=True)

        self.cache[key] = value

    def clear(self) -> None:
        """Limpa todo o cache."""
        self.cache.clear()
        self.access_count = 0
        self.hit_count = 0
        self.miss_count = 0

    def size(self) -> int:
        """Retorna o tamanho atual do cache."""
        return len(self.cache)

    def is_full(self) -> bool:
        """Verifica se o cache está cheio."""
        return len(self.cache) >= self.capacity

    def get_stats(self) -> dict:
        """
        Retorna estatísticas de desempenho do cache.

        Returns:
            dict: Dicionário com estatísticas detalhadas.
        """
        hit_rate = (self.hit_count / self.access_count * 100) if self.access_count > 0 else 0
        return {
            'algorithm': 'MRU',
            'capacity': self.capacity,
            'current_size': len(self.cache),
            'total_accesses': self.access_count,
            'hits': self.hit_count,
            'misses': self.miss_count,
            'hit_rate': hit_rate,
            'keys_in_cache': list(self.cache.keys())
        }

    def reset_stats(self) -> None:
        """Reinicia as estatísticas sem limpar o cache."""
        self.access_count = 0
        self.hit_count = 0
        self.miss_count = 0

    def __str__(self) -> str:
        """Representação em string do estado do cache."""
        stats = self.get_stats()
        return (
            f"MRUCache(capacity={self.capacity}, "
            f"size={stats['current_size']}, "
            f"hit_rate={stats['hit_rate']:.1f}%)"
        )

    def __repr__(self) -> str:
        """Representação oficial do objeto."""
        return self.__str__()
