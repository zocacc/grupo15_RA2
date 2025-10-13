#!/usr/bin/env python3
"""
Arquivo principal do projeto de cache de textos - RA2
Sistema de leitura de textos com cache implementando algoritmos FIFO, LRU e LFU

Autores: [Nomes dos integrantes do grupo]
"""

import sys
import time
from pathlib import Path

# Adicionar diretórios do projeto ao path
project_root = Path(__file__).parent
sys.path.append(str(project_root))

from core.user_interface import UserInterface
from core.text_manager import TextManager
from core.cache_manager import CacheManager
from algorithms.fifo_cache import FIFOCache
from algorithms.lru_cache import LRUCache
from algorithms.lfu_cache import LFUCache
from algorithms.mru_cache import MRUCache
from simulation.simulator import CacheSimulator
from simulation.report_generator import ReportGenerator
from core.config import settings

class CacheTextReader:
    """Classe principal da aplicação"""

    def __init__(self):
        self.text_manager = TextManager(settings.TEXT_DIR)
        self.ui = UserInterface()

        # Inicializar algoritmos de cache
        self.cache_algorithms = {
            'FIFO': FIFOCache(settings.CACHE_SIZE),
            'LRU': LRUCache(settings.CACHE_SIZE),
            'LFU': LFUCache(settings.CACHE_SIZE),
            'MRU': MRUCache(settings.CACHE_SIZE)
        }

        # Cache manager para coordenar algoritmos
        self.cache_manager = CacheManager(self.cache_algorithms)

        # Algoritmo padrão (pode ser alterado pela simulação)
        self.current_algorithm = 'LRU'

    def load_text(self, text_id):
        """Carrega um texto usando o sistema de cache"""
        start_time = time.perf_counter()

        # Verificar se texto existe no cache
        cached_text = self.cache_manager.get(text_id, self.current_algorithm)

        if cached_text is not None:
            # Cache hit
            load_time = time.perf_counter() - start_time
            return cached_text, True, load_time
        else:
            # Cache miss - carregar do disco (simulando lentidão)
            text_content = self.text_manager.load_text(text_id)
            if text_content:
                # Adicionar ao cache
                self.cache_manager.put(text_id, text_content, self.current_algorithm)
                load_time = time.perf_counter() - start_time
                return text_content, False, load_time
            else:
                return None, False, time.perf_counter() - start_time

    def run_interactive_mode(self):
        """Executa o modo interativo principal"""
        self.ui.show_welcome()

        while True:
            try:
                text_id = self.ui.get_text_selection(self.text_manager, self.current_algorithm)

                if text_id == 0:
                    # Encerrar programa
                    self.ui.show_goodbye()
                    break
                elif text_id == -1:
                    # Modo simulação
                    self.run_simulation_mode()
                    self.ui.show_welcome()
                elif text_id == -2:
                    # Modo configuração
                    self.run_config_mode()
                    self.ui.show_welcome()
                elif 1 <= text_id <= 100:
                    # Carregar e exibir texto
                    text_content, was_cached, load_time = self.load_text(text_id)

                    if text_content:
                        self.ui.display_text(text_id, text_content, was_cached, load_time, self.current_algorithm)
                    else:
                        self.ui.show_error(f"Texto {text_id} não encontrado!")
                else:
                    self.ui.show_error("Número inválido! Digite um número entre 1-100, 0 para sair, -1 para simulação ou -2 para configurações.")

            except KeyboardInterrupt:
                self.ui.show_goodbye()
                break
            except Exception as e:
                self.ui.show_error(f"Erro inesperado: {e}")

    def run_simulation_mode(self):
        """Executa o modo de simulação"""
        print("\n" + "="*60)
        print("MODO DE SIMULAÇÃO - ANÁLISE DE ALGORITMOS DE CACHE")
        print("="*60)

        simulator = CacheSimulator(
            text_manager=self.text_manager,
            cache_algorithms=self.cache_algorithms
        )

        try:
            # Executar simulação
            results = simulator.run_full_simulation()

            # Gerar relatórios
            report_gen = ReportGenerator()
            report_gen.generate_all_reports(results)

            # Determinar melhor algoritmo
            best_algorithm = simulator.get_best_algorithm(results)

            print(f"\nAlgoritmo recomendado baseado na simulação: {best_algorithm}")
            print(f"Algoritmo atual será alterado para: {best_algorithm}")

            # Atualizar algoritmo padrão
            self.current_algorithm = best_algorithm

            input("\nPressione Enter para voltar ao menu principal...")

        except Exception as e:
            print(f"Erro durante simulação: {e}")
            input("Pressione Enter para continuar...")

    def run_config_mode(self):
        """Executa o modo de configuração."""
        while True:
            current_config = {
                'algorithm': self.current_algorithm,
                'disk_delay': settings.DISK_DELAY_SIMULATION
            }
            available_algs = list(self.cache_algorithms.keys())
            
            choice = self.ui.show_config_menu(current_config, available_algs)

            if choice == '1':
                new_alg = self.ui.get_algorithm_choice(self.current_algorithm, available_algs)
                self.current_algorithm = new_alg
                print(f"\nAlgoritmo de cache alterado para: {self.current_algorithm}")
                time.sleep(1.5)
            elif choice == '2':
                new_delay_config = self.ui.get_disk_delay_config(settings.DISK_DELAY_SIMULATION)
                settings.DISK_DELAY_SIMULATION.update(new_delay_config)
                print("\nConfigurações de atraso de disco atualizadas.")
                time.sleep(1.5)
            elif choice == '0':
                break
            else:
                self.ui.show_error("Opção inválida.")
                time.sleep(1)


def main():
    """Função principal"""
    try:
        app = CacheTextReader()
        app.run_interactive_mode()
    except Exception as e:
        print(f"Erro fatal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()