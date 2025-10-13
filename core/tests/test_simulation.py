"""
Testes para o sistema de simulação
"""

import unittest
import sys
from pathlib import Path
from unittest.mock import Mock, patch

# Adicionar path do projeto
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from simulation.random_generators import RandomGenerators, UserSimulator
from algorithms.fifo_cache import FIFOCache

class TestRandomGenerators(unittest.TestCase):
    """Testes para geradores aleatórios"""

    def setUp(self):
        self.generator = RandomGenerators((1, 10))  # Range pequeno para testes

    def test_uniform_generation(self):
        """Teste geração uniforme"""
        samples = self.generator.generate_uniform(100)

        self.assertEqual(len(samples), 100)
        self.assertTrue(all(1 <= s <= 10 for s in samples))

    def test_poisson_generation(self):
        """Teste geração Poisson"""
        samples = self.generator.generate_poisson(100)

        self.assertEqual(len(samples), 100)
        self.assertTrue(all(1 <= s <= 10 for s in samples))

    def test_weighted_generation(self):
        """Teste geração ponderada"""
        # Configurar range especial pequeno para teste
        self.generator.weighted_params = {
            'special_range': (3, 5),
            'special_probability': 0.8,  # Alta probabilidade para teste
            'normal_probability': 0.2
        }

        samples = self.generator.generate_weighted(1000)

        # Contar quantos estão no range especial
        special_count = sum(1 for s in samples if 3 <= s <= 5)
        special_rate = special_count / len(samples)

        # Deve estar próximo de 80% (com margem de erro)
        self.assertGreater(special_rate, 0.6)  # Pelo menos 60%
        self.assertLess(special_rate, 1.0)     # Menos que 100%

    def test_analyze_distribution(self):
        """Teste análise de distribuição"""
        samples = [1, 2, 2, 3, 3, 3]
        analysis = self.generator.analyze_distribution(samples)

        self.assertEqual(analysis['total_samples'], 6)
        self.assertEqual(analysis['min_value'], 1)
        self.assertEqual(analysis['max_value'], 3)
        self.assertEqual(analysis['unique_values'], 3)

        freq = analysis['frequency_distribution']
        self.assertEqual(freq[1], 1)
        self.assertEqual(freq[2], 2)
        self.assertEqual(freq[3], 3)

class TestUserSimulator(unittest.TestCase):
    """Testes para simulador de usuário"""

    def setUp(self):
        self.generator = RandomGenerators((1, 10))
        self.user = UserSimulator(1, self.generator)

    def test_user_session(self):
        """Teste sessão de usuário"""
        requests = self.user.simulate_session(20, 'uniform')

        self.assertEqual(len(requests), 20)
        self.assertTrue(all(1 <= r <= 10 for r in requests))
        self.assertEqual(len(self.user.access_history), 20)

    def test_user_stats(self):
        """Teste estatísticas do usuário"""
        # Simular algumas requisições
        self.user.simulate_session(10, 'uniform')

        stats = self.user.get_user_stats()

        self.assertEqual(stats['user_id'], 1)
        self.assertEqual(stats['total_requests'], 10)
        self.assertGreater(stats['unique_texts'], 0)

class TestSimulationIntegration(unittest.TestCase):
    """Testes de integração da simulação"""

    def setUp(self):
        # Mock do text manager
        self.mock_text_manager = Mock()
        self.mock_text_manager.load_text.return_value = "texto de exemplo"

        # Cache real para teste
        self.cache_algorithms = {
            'FIFO': FIFOCache(5)
        }

    def test_cache_simulation_basic(self):
        """Teste básico de simulação com cache"""
        cache = self.cache_algorithms['FIFO']

        # Simular algumas operações
        hit_count = 0
        miss_count = 0

        test_requests = [1, 2, 1, 3, 1, 2, 4, 1]

        for text_id in test_requests:
            if cache.get(text_id) is not None:
                hit_count += 1
            else:
                miss_count += 1
                cache.put(text_id, f"texto{text_id}")

        self.assertGreater(hit_count, 0)  # Deve ter alguns hits
        self.assertGreater(miss_count, 0)  # Deve ter alguns misses

    @patch('time.sleep')  # Mock do delay de disco
    def test_performance_measurement(self, mock_sleep):
        """Teste medição de performance"""
        import time

        cache = FIFOCache(3)

        start_time = time.time()

        # Simular acesso com miss
        result = cache.get(1)
        self.assertIsNone(result)

        # Simular carregamento
        cache.put(1, "texto1")

        # Simular acesso com hit
        result = cache.get(1)
        self.assertEqual(result, "texto1")

        elapsed = time.time() - start_time

        # Tempo deve ser mensurável
        self.assertGreaterEqual(elapsed, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)
