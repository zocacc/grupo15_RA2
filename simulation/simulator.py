"""
Módulo principal de simulação - Aluno D
Executa simulações completas comparando algoritmos de cache
"""

import time
import random
from typing import Dict, List, Tuple, Any
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

from .random_generators import RandomGenerators, UserSimulator
from core.config.settings import SIMULATION_CONFIG, CACHE_SIZE

class CacheSimulator:
    """
    Simulador principal para análise de algoritmos de cache
    """

    def __init__(self, text_manager, cache_algorithms: Dict[str, Any]):
        self.text_manager = text_manager
        self.cache_algorithms = cache_algorithms
        self.generator = RandomGenerators()
        self.simulation_results = {}

    def simulate_user_algorithm_combination(self, algorithm_name: str, user_id: int, 
                                          distribution_type: str) -> Dict:
        """
        Simula um usuário usando um algoritmo específico

        Args:
            algorithm_name: Nome do algoritmo de cache
            user_id: ID do usuário
            distribution_type: Tipo de distribuição dos acessos

        Returns:
            Dicionário com resultados da simulação
        """
        # Criar novo cache para esta simulação
        cache_class = type(self.cache_algorithms[algorithm_name])
        cache = cache_class(CACHE_SIZE)

        # Criar simulador de usuário
        user = UserSimulator(user_id, self.generator)

        # Gerar requisições
        requests = user.simulate_session(
            SIMULATION_CONFIG['requests_per_user'],
            distribution_type
        )

        # Simular execução das requisições
        results = {
            'algorithm': algorithm_name,
            'user_id': user_id,
            'distribution_type': distribution_type,
            'total_requests': len(requests),
            'cache_hits': 0,
            'cache_misses': 0,
            'total_load_time': 0,
            'request_details': [],
            'cache_states': []
        }

        total_requests = len(requests)
        for i, text_id in enumerate(requests):
            start_time = time.time()

            # Verificar cache
            cached_content = cache.get(text_id)

            if cached_content is not None:
                # Cache hit
                load_time = time.time() - start_time
                results['cache_hits'] += 1
                was_hit = True
            else:
                # Cache miss - carregar do disco
                content = self.text_manager.load_text(text_id)
                if content:
                    cache.put(text_id, content)

                load_time = time.time() - start_time
                results['cache_misses'] += 1
                was_hit = False

            results['total_load_time'] += load_time

            # Registrar detalhes da requisição
            request_detail = {
                'request_number': i + 1,
                'text_id': text_id,
                'was_cache_hit': was_hit,
                'load_time': load_time,
                'cache_size': cache.size()
            }
            results['request_details'].append(request_detail)
            
            # Visualização do progresso
            progress = (i + 1) / total_requests
            bar_length = 20
            filled_length = int(bar_length * progress)
            bar = '█' * filled_length + '-' * (bar_length - filled_length)
            print(f"\r    - Usuário {user_id}: [{bar}] {progress:.0%} lendo livro {i+1}/{total_requests}", end='')


            # Registrar estado do cache a cada 50 requisições
            if (i + 1) % 50 == 0:
                cache_state = {
                    'request_number': i + 1,
                    'cache_contents': list(cache.cache.keys()) if hasattr(cache, 'cache') else [],
                    'cache_size': cache.size(),
                    'hit_rate_so_far': (results['cache_hits'] / (i + 1)) * 100
                }
                results['cache_states'].append(cache_state)
        
        print() # Newline after progress bar

        # Calcular métricas finais
        results['hit_rate'] = (results['cache_hits'] / results['total_requests']) * 100
        results['miss_rate'] = (results['cache_misses'] / results['total_requests']) * 100
        results['avg_load_time'] = results['total_load_time'] / results['total_requests']
        results['user_stats'] = user.get_user_stats()
        results['final_cache_stats'] = cache.get_stats() if hasattr(cache, 'get_stats') else {}

        return results



    def run_full_simulation(self) -> Dict:
        """
        Executa simulação completa de todos os algoritmos e distribuições
        Returns:
            Dicionário com todos os resultados
        """
        print("Iniciando simulação completa...")
        print(f"Algoritmos: {SIMULATION_CONFIG['algorithms']}")
        print(f"Cenários de usuário: {SIMULATION_CONFIG['user_scenarios']}")
        print(f"Requisições por usuário: {SIMULATION_CONFIG['requests_per_user']}")
        print("-" * 60)

        all_results = {
            'simulation_info': {
                'timestamp': datetime.now().isoformat(),
                'config': SIMULATION_CONFIG,
                'cache_size': CACHE_SIZE
            },
            'results_by_algorithm': {},
            'summary_stats': {}
        }

        total_combinations = (len(SIMULATION_CONFIG['algorithms']) *
                            len(SIMULATION_CONFIG['user_scenarios']))
        current_combination = 0

        for algorithm in SIMULATION_CONFIG['algorithms']:
            if algorithm not in self.cache_algorithms:
                print(f"AVISO: Algoritmo {algorithm} não disponível")
                continue

            all_results['results_by_algorithm'][algorithm] = {}

            for scenario in SIMULATION_CONFIG['user_scenarios']:
                user_id = scenario['user_id']
                distribution = scenario['distribution']
                current_combination += 1
                print(f"\n[{current_combination}/{total_combinations}] Executando: {algorithm} com usuário {user_id} (distribuição {distribution})")

                if distribution not in all_results['results_by_algorithm'][algorithm]:
                    all_results['results_by_algorithm'][algorithm][distribution] = []

                simulation_result = self.simulate_user_algorithm_combination(algorithm, user_id, distribution)
                all_results['results_by_algorithm'][algorithm][distribution].append(simulation_result)

        # Gerar estatísticas resumidas
        all_results['summary_stats'] = self._generate_summary_stats(all_results['results_by_algorithm'])

        self.simulation_results = all_results
        return all_results

    def _generate_summary_stats(self, results_by_algorithm: Dict) -> Dict:
        """
        Gera estatísticas resumidas dos resultados

        Args:
            results_by_algorithm: Resultados organizados por algoritmo

        Returns:
            Dicionário com estatísticas resumidas
        """
        summary = {
            'by_algorithm': {},
            'by_distribution': {},
            'overall_best': {}
        }

        # Estatísticas por algoritmo
        for algorithm, distributions in results_by_algorithm.items():
            alg_stats = {
                'total_simulations': 0,
                'avg_hit_rate': 0,
                'avg_load_time': 0,
                'best_distribution': '',
                'best_hit_rate': 0
            }

            total_hit_rates = []
            total_load_times = []

            for distribution, user_simulations in distributions.items():
                dist_hit_rates = [user['hit_rate'] for user in user_simulations]
                dist_load_times = [user['avg_load_time'] for user in user_simulations]

                avg_dist_hit_rate = sum(dist_hit_rates) / len(dist_hit_rates)

                total_hit_rates.extend(dist_hit_rates)
                total_load_times.extend(dist_load_times)
                alg_stats['total_simulations'] += len(user_simulations)

                # Verificar se é a melhor distribuição para este algoritmo
                if avg_dist_hit_rate > alg_stats['best_hit_rate']:
                    alg_stats['best_hit_rate'] = avg_dist_hit_rate
                    alg_stats['best_distribution'] = distribution

            alg_stats['avg_hit_rate'] = sum(total_hit_rates) / len(total_hit_rates)
            alg_stats['avg_load_time'] = sum(total_load_times) / len(total_load_times)

            summary['by_algorithm'][algorithm] = alg_stats

        # Encontrar melhor algoritmo geral
        best_algorithm = max(summary['by_algorithm'].keys(),
                           key=lambda x: summary['by_algorithm'][x]['avg_hit_rate'])

        summary['overall_best'] = {
            'algorithm': best_algorithm,
            'hit_rate': summary['by_algorithm'][best_algorithm]['avg_hit_rate'],
            'load_time': summary['by_algorithm'][best_algorithm]['avg_load_time']
        }

        return summary

    def get_best_algorithm(self, results: Dict = None) -> str:
        """
        Determina o melhor algoritmo baseado nos resultados

        Args:
            results: Resultados da simulação (usa self.simulation_results se None)

        Returns:
            Nome do melhor algoritmo
        """
        if results is None:
            results = self.simulation_results

        if 'summary_stats' in results and 'overall_best' in results['summary_stats']:
            return results['summary_stats']['overall_best']['algorithm']

        return 'LRU'  # Default fallback

    def export_results_to_csv(self, filename: str = None) -> str:
        """
        Exporta resultados para CSV

        Args:
            filename: Nome do arquivo (gera automaticamente se None)

        Returns:
            Caminho do arquivo criado
        """
        if filename is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"simulation_results_{timestamp}.csv"

        # Implementar exportação CSV
        # (Por brevidade, retornando o nome do arquivo)
        return filename


import re
from pathlib import Path

def update_default_algorithm(new_algorithm: str):
    """
    Atualiza o algoritmo padrão no arquivo de configurações.

    Args:
        new_algorithm: O nome do novo algoritmo padrão (ex: 'LRU', 'FIFO').
    """
    settings_file = Path(__file__).parent.parent / "core" / "config" / "settings.py"
    
    try:
        with open(settings_file, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        new_lines = []
        updated = False
        for line in lines:
            # Procura pela linha que define DEFAULT_ALGORITHM
            if re.match(r"^\s*DEFAULT_ALGORITHM\s*=\s*['\"]\w+['\"]", line):
                new_lines.append(f"DEFAULT_ALGORITHM = '{new_algorithm}'  # Algoritmo padrão para uso normal\n")
                updated = True
            else:
                new_lines.append(line)

        if updated:
            with open(settings_file, 'w', encoding='utf-8') as f:
                f.writelines(new_lines)
            print(f"\n-> Algoritmo padrão atualizado para: {new_algorithm}")
        else:
            print("\n-> AVISO: Não foi possível encontrar a configuração DEFAULT_ALGORITHM para atualizar.")

    except IOError as e:
        print(f"\nERRO: Não foi possível ler ou escrever no arquivo de configurações: {e}")
