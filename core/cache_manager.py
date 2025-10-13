"""
Módulo gerenciador de cache - Aluno A
Interface unificada para coordenar os diferentes algoritmos de cache
"""

from typing import Any, Optional, Dict
import time

class CacheManager:
    """
    Gerenciador central dos algoritmos de cache
    Coordena FIFO, LRU e LFU de forma unificada
    """

    def __init__(self, cache_algorithms: Dict[str, Any]):
        self.algorithms = cache_algorithms
        self.stats = {alg: {'hits': 0, 'misses': 0, 'total_time': 0} for alg in cache_algorithms}

    def get(self, key: int, algorithm: str) -> Optional[str]:
        """
        Recupera um item do cache usando o algoritmo especificado

        Args:
            key (int): Chave do item (ID do texto)
            algorithm (str): Nome do algoritmo ('FIFO', 'LRU', 'LFU')

        Returns:
            Optional[str]: Conteúdo do cache ou None se não encontrado
        """
        if algorithm not in self.algorithms:
            raise ValueError(f"Algoritmo '{algorithm}' não disponível")

        start_time = time.time()
        result = self.algorithms[algorithm].get(key)
        elapsed_time = time.time() - start_time

        # Atualizar estatísticas
        if result is not None:
            self.stats[algorithm]['hits'] += 1
        else:
            self.stats[algorithm]['misses'] += 1

        self.stats[algorithm]['total_time'] += elapsed_time

        return result

    def put(self, key: int, value: str, algorithm: str) -> None:
        """
        Armazena um item no cache usando o algoritmo especificado

        Args:
            key (int): Chave do item (ID do texto)
            value (str): Valor a armazenar (conteúdo do texto)
            algorithm (str): Nome do algoritmo ('FIFO', 'LRU', 'LFU')
        """
        if algorithm not in self.algorithms:
            raise ValueError(f"Algoritmo '{algorithm}' não disponível")

        self.algorithms[algorithm].put(key, value)

    def clear(self, algorithm: str = None) -> None:
        """
        Limpa o cache do algoritmo especificado ou todos

        Args:
            algorithm (str, optional): Nome do algoritmo ou None para todos
        """
        if algorithm:
            if algorithm in self.algorithms:
                self.algorithms[algorithm].clear()
        else:
            for alg in self.algorithms.values():
                alg.clear()

    def get_stats(self, algorithm: str = None) -> Dict:
        """
        Retorna estatísticas dos algoritmos

        Args:
            algorithm (str, optional): Nome do algoritmo ou None para todos

        Returns:
            Dict: Estatísticas do algoritmo ou de todos
        """
        if algorithm:
            return self.stats.get(algorithm, {})
        return self.stats.copy()

    def get_cache_info(self, algorithm: str) -> Dict:
        """
        Retorna informações detalhadas do cache

        Args:
            algorithm (str): Nome do algoritmo

        Returns:
            Dict: Informações do cache
        """
        if algorithm not in self.algorithms:
            return {}

        cache = self.algorithms[algorithm]
        stats = self.stats[algorithm]

        total_requests = stats['hits'] + stats['misses']
        hit_rate = (stats['hits'] / total_requests * 100) if total_requests > 0 else 0

        return {
            'algorithm': algorithm,
            'size': len(cache.cache) if hasattr(cache, 'cache') else 0,
            'capacity': cache.capacity if hasattr(cache, 'capacity') else 0,
            'hits': stats['hits'],
            'misses': stats['misses'],
            'hit_rate': hit_rate,
            'total_time': stats['total_time'],
            'avg_time': stats['total_time'] / total_requests if total_requests > 0 else 0
        }

    def reset_stats(self):
        """Reinicia todas as estatísticas"""
        for alg in self.stats:
            self.stats[alg] = {'hits': 0, 'misses': 0, 'total_time': 0}

        # Limpar estatísticas dos algoritmos individuais
        for alg in self.algorithms.values():
            if hasattr(alg, 'reset_stats'):
                alg.reset_stats()

    def compare_algorithms(self, num_requests: int = None) -> Dict:
        """
        Compara performance de todos os algoritmos

        Args:
            num_requests (int, optional): Número de requests para considerar

        Returns:
            Dict: Comparação detalhada dos algoritmos
        """
        comparison = {}

        for alg_name in self.algorithms:
            info = self.get_cache_info(alg_name)
            comparison[alg_name] = info

        # Determinar melhor algoritmo baseado na taxa de hit
        best_algorithm = max(comparison.keys(), 
                           key=lambda x: comparison[x]['hit_rate'])

        comparison['best_algorithm'] = best_algorithm
        comparison['summary'] = {
            'total_algorithms': len(self.algorithms),
            'best_hit_rate': comparison[best_algorithm]['hit_rate']
        }

        return comparison
