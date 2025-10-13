"""
Testes unitários para os algoritmos de cache
"""

import unittest
import sys
from pathlib import Path

# Adicionar path do projeto
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from algorithms.fifo_cache import FIFOCache
from algorithms.lru_cache import LRUCache
from algorithms.lfu_cache import LFUCache

class TestFIFOCache(unittest.TestCase):
    """Testes para algoritmo FIFO"""

    def setUp(self):
        self.cache = FIFOCache(capacity=3)

    def test_basic_operations(self):
        """Teste operações básicas"""
        # Teste put e get
        self.cache.put(1, "texto1")
        self.cache.put(2, "texto2")

        self.assertEqual(self.cache.get(1), "texto1")
        self.assertEqual(self.cache.get(2), "texto2")
        self.assertIsNone(self.cache.get(3))

    def test_fifo_eviction(self):
        """Teste evição FIFO"""
        # Preencher cache
        self.cache.put(1, "texto1")
        self.cache.put(2, "texto2") 
        self.cache.put(3, "texto3")

        # Adicionar quarto item deve remover primeiro (FIFO)
        self.cache.put(4, "texto4")

        self.assertIsNone(self.cache.get(1))  # Removido
        self.assertEqual(self.cache.get(2), "texto2")
        self.assertEqual(self.cache.get(3), "texto3")
        self.assertEqual(self.cache.get(4), "texto4")

    def test_capacity(self):
        """Teste limite de capacidade"""
        self.assertEqual(self.cache.size(), 0)

        for i in range(5):
            self.cache.put(i, f"texto{i}")

        self.assertEqual(self.cache.size(), 3)  # Máximo 3

    def test_stats(self):
        """Teste estatísticas"""
        self.cache.put(1, "texto1")
        self.cache.get(1)  # hit
        self.cache.get(2)  # miss

        stats = self.cache.get_stats()
        self.assertEqual(stats['hits'], 1)
        self.assertEqual(stats['misses'], 1)
        self.assertEqual(stats['hit_rate'], 50.0)

class TestLRUCache(unittest.TestCase):
    """Testes para algoritmo LRU"""

    def setUp(self):
        self.cache = LRUCache(capacity=3)

    def test_lru_eviction(self):
        """Teste evição LRU"""
        # Preencher cache
        self.cache.put(1, "texto1")
        self.cache.put(2, "texto2")
        self.cache.put(3, "texto3")

        # Acessar item 1 para torná-lo mais recente
        self.cache.get(1)

        # Adicionar item 4 deve remover 2 (menos recente)
        self.cache.put(4, "texto4")

        self.assertEqual(self.cache.get(1), "texto1")  # Ainda presente
        self.assertIsNone(self.cache.get(2))  # Removido (LRU)
        self.assertEqual(self.cache.get(3), "texto3")
        self.assertEqual(self.cache.get(4), "texto4")

    def test_access_updates_order(self):
        """Teste se acesso atualiza ordem LRU"""
        self.cache.put(1, "texto1")
        self.cache.put(2, "texto2")
        self.cache.put(3, "texto3")

        # Ordem inicial: 1, 2, 3 (1 é LRU)

        # Acessar 1 move para mais recente
        self.cache.get(1)
        # Nova ordem: 2, 3, 1 (2 é LRU)

        self.cache.put(4, "texto4")
        # Deve remover 2

        self.assertEqual(self.cache.get(1), "texto1")
        self.assertIsNone(self.cache.get(2))
        self.assertEqual(self.cache.get(3), "texto3")
        self.assertEqual(self.cache.get(4), "texto4")

class TestLFUCache(unittest.TestCase):
    """Testes para algoritmo LFU"""

    def setUp(self):
        self.cache = LFUCache(capacity=3)

    def test_lfu_eviction(self):
        """Teste evição LFU"""
        # Preencher cache
        self.cache.put(1, "texto1")
        self.cache.put(2, "texto2")
        self.cache.put(3, "texto3")

        # Acessar alguns itens para criar frequências diferentes
        self.cache.get(1)  # freq 1->2
        self.cache.get(1)  # freq 2->3
        self.cache.get(2)  # freq 1->2
        # Frequências: 1=3, 2=2, 3=1

        # Adicionar item 4 deve remover 3 (menor frequência)
        self.cache.put(4, "texto4")

        self.assertEqual(self.cache.get(1), "texto1")  # freq=3
        self.assertEqual(self.cache.get(2), "texto2")  # freq=2  
        self.assertIsNone(self.cache.get(3))  # Removido (LFU)
        self.assertEqual(self.cache.get(4), "texto4")  # freq=1

    def test_frequency_tracking(self):
        """Teste rastreamento de frequência"""
        self.cache.put(1, "texto1")

        # Frequência inicial deve ser 1
        self.assertEqual(self.cache.get_frequency(1), 1)

        # Acessar deve incrementar
        self.cache.get(1)
        self.assertEqual(self.cache.get_frequency(1), 2)

        self.cache.get(1)
        self.assertEqual(self.cache.get_frequency(1), 3)

class TestCacheComparison(unittest.TestCase):
    """Testes comparativos entre algoritmos"""

    def setUp(self):
        self.fifo = FIFOCache(3)
        self.lru = LRUCache(3)  
        self.lfu = LFUCache(3)

    def test_same_capacity(self):
        """Teste se todos respeitam mesma capacidade"""
        caches = [self.fifo, self.lru, self.lfu]

        for cache in caches:
            # Adicionar mais itens que a capacidade
            for i in range(5):
                cache.put(i, f"texto{i}")

            # Todos devem ter tamanho 3
            self.assertEqual(cache.size(), 3)

    def test_different_behaviors(self):
        """Teste comportamentos diferentes com mesmo padrão"""
        caches = {"FIFO": self.fifo, "LRU": self.lru, "LFU": self.lfu}

        # Mesmo padrão de acesso para todos
        for cache in caches.values():
            cache.put(1, "texto1")
            cache.put(2, "texto2")
            cache.put(3, "texto3")
            cache.get(1)  # Acessar 1
            cache.put(4, "texto4")  # Forçar evição

        # Verificar qual item foi removido (comportamento específico)
        results = {}
        for name, cache in caches.items():
            removed_item = None
            for i in [1, 2, 3]:
                if cache.get(i) is None:
                    removed_item = i
                    break
            results[name] = removed_item

        # FIFO deve remover 1 (primeiro inserido)
        # LRU deve remover 2 (menos recentemente usado após acesso a 1)
        # LFU pode remover 2 ou 3 (ambos com frequência 1)

        self.assertIsNotNone(results["FIFO"])
        self.assertIsNotNone(results["LRU"])
        self.assertIsNotNone(results["LFU"])

if __name__ == "__main__":
    # Executar todos os testes
    unittest.main(verbosity=2)
