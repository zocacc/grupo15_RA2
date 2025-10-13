"""
Implementação do algoritmo LFU (Least Frequently Used) - Aluno D
Cache que remove o item menos frequentemente usado quando atinge capacidade máxima
"""

from collections import defaultdict, OrderedDict
import time

class LFUCache:
    """
    Implementação do algoritmo de cache LFU (Least Frequently Used)

    O LFU remove o item com menor frequência de uso quando o cache está cheio.
    Em caso de empate, remove o menos recentemente usado (LRU como desempate).
    """

    def __init__(self, capacity: int):
        """
        Inicializa o cache LFU

        Args:
            capacity (int): Capacidade máxima do cache
        """
        self.capacity = capacity
        self.cache = {}  # key -> value
        self.frequencies = defaultdict(int)  # key -> frequency count
        self.freq_to_keys = defaultdict(OrderedDict)  # frequency -> {key: access_time}
        self.min_frequency = 0
        self.access_count = 0
        self.hit_count = 0
        self.miss_count = 0
        self.access_times = {}

    def _update_freq(self, key: int) -> None:
        """
        Atualiza a frequência de uso de uma chave

        Args:
            key (int): Chave a atualizar
        """
        current_time = time.time()
        freq = self.frequencies[key]

        # Remover da frequência atual
        del self.freq_to_keys[freq][key]

        # Se era a única chave com frequência mínima, atualizar min_frequency
        if freq == self.min_frequency and not self.freq_to_keys[freq]:
            self.min_frequency += 1

        # Adicionar na nova frequência
        new_freq = freq + 1
        self.frequencies[key] = new_freq
        self.freq_to_keys[new_freq][key] = current_time
        self.access_times[key] = current_time

    def get(self, key: int) -> str:
        """
        Recupera um item do cache e incrementa sua frequência

        Args:
            key (int): Chave do item

        Returns:
            str: Valor do item ou None se não encontrado
        """
        self.access_count += 1

        if key in self.cache:
            # Atualizar frequência
            self._update_freq(key)
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
        if self.capacity <= 0:
            return

        current_time = time.time()

        if key in self.cache:
            # Atualizar valor existente
            self.cache[key] = value
            self._update_freq(key)
            return

        # Se cache está cheio, remover o LFU
        if len(self.cache) >= self.capacity:
            # Encontrar chave com menor frequência
            # Em caso de empate, remove a menos recentemente usada
            lfu_key = next(iter(self.freq_to_keys[self.min_frequency]))

            # Remover da estrutura
            del self.cache[lfu_key]
            del self.frequencies[lfu_key]
            del self.freq_to_keys[self.min_frequency][lfu_key]
            if lfu_key in self.access_times:
                del self.access_times[lfu_key]

        # Adicionar novo item com frequência 1
        self.cache[key] = value
        self.frequencies[key] = 1
        self.freq_to_keys[1][key] = current_time
        self.access_times[key] = current_time
        self.min_frequency = 1

    def clear(self) -> None:
        """Limpa todo o cache"""
        self.cache.clear()
        self.frequencies.clear()
        self.freq_to_keys.clear()
        self.access_times.clear()
        self.min_frequency = 0

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

        # Calcular estatísticas de frequência
        freq_distribution = {}
        for key, freq in self.frequencies.items():
            if freq not in freq_distribution:
                freq_distribution[freq] = 0
            freq_distribution[freq] += 1

        return {
            'algorithm': 'LFU',
            'capacity': self.capacity,
            'current_size': len(self.cache),
            'total_accesses': self.access_count,
            'hits': self.hit_count,
            'misses': self.miss_count,
            'hit_rate': hit_rate,
            'keys_in_cache': list(self.cache.keys()),
            'min_frequency': self.min_frequency,
            'frequency_distribution': freq_distribution
        }

    def reset_stats(self) -> None:
        """Reinicia as estatísticas sem limpar o cache"""
        self.access_count = 0
        self.hit_count = 0
        self.miss_count = 0

    def get_frequency(self, key: int) -> int:
        """
        Retorna a frequência de uso de uma chave

        Args:
            key (int): Chave a consultar

        Returns:
            int: Frequência de uso
        """
        return self.frequencies.get(key, 0)

    def get_keys_by_frequency(self) -> dict:
        """
        Retorna chaves agrupadas por frequência

        Returns:
            dict: Frequência -> lista de chaves
        """
        result = {}
        for freq, keys_dict in self.freq_to_keys.items():
            if keys_dict:  # Apenas frequências com chaves
                result[freq] = list(keys_dict.keys())
        return result

    def peek_lfu(self) -> int:
        """
        Retorna a chave menos frequentemente usada sem removê-la

        Returns:
            int: Chave LFU ou None se cache vazio
        """
        if self.freq_to_keys[self.min_frequency]:
            return next(iter(self.freq_to_keys[self.min_frequency]))
        return None

    def contains(self, key: int) -> bool:
        """
        Verifica se uma chave está no cache

        Args:
            key (int): Chave a verificar

        Returns:
            bool: True se a chave está no cache
        """
        return key in self.cache

    def __str__(self) -> str:
        """Representação string do cache"""
        return f"LFUCache(capacity={self.capacity}, size={len(self.cache)}, hit_rate={self.get_stats()['hit_rate']:.1f}%)"

    def __repr__(self) -> str:
        return self.__str__()
