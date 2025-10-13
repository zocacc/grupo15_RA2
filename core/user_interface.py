"""
Módulo de interface com usuário - Aluno A
Responsável pela intera
uevo com o usuário no terminal
"""

import os
import time
from datetime import datetime

class UserInterface:
    """Classe responsável pela interface com o usuário"""

    def __init__(self):
        self.stats = {
            'texts_viewed': 0,
            'cache_hits': 0,
            'cache_misses': 0,
            'total_time': 0,
            'total_hit_time': 0.0,
            'total_miss_time': 0.0
        }

    def clear_screen(self):
        """Limpa a tela do terminal"""
        os.system('clear' if os.name == 'posix' else 'cls')

    def show_welcome(self):
        """Exibe mensagem de boas-vindas"""
        self.clear_screen()
        print("="*70)
        print("    SISTEMA DE LEITURA DE TEXTOS COM CACHE - RA2")
        print("="*70)
        print("Empresa: Texto é Vida")
        print("Sistema: Leitura eficiente de 100 textos importantes")
        print("Algoritmos: FIFO, LRU, LFU, MRU")
        print("="*70)
        print()
        print("Instruções:")
        print("• Digite o número do texto desejado (1-100)")
        print("• Digite 0 para sair do programa")
        print("• Digite -1 para entrar no modo de simulação")
        print("• Digite -2 para acessar as configurações")
        print()

    def get_text_selection(self, text_manager, algorithm: str):
        """
        Solicita ao usuário a seleção de um texto

        Args:
            text_manager (TextManager): Instância do gerenciador de textos
            algorithm (str): Algoritmo de cache atual

        Returns:
            int: ID do texto selecionado
        """
        while True:
            try:
                print("Estatísticas da sessão:")
                print(f"  - Algoritmo: {algorithm}")
                print(f"  - Textos visualizados: {self.stats['texts_viewed']}")
                print(f"  - Cache hits: {self.stats['cache_hits']}")
                print(f"  - Cache misses: {self.stats['cache_misses']}")
                if self.stats['texts_viewed'] > 0:
                    hit_rate = (self.stats['cache_hits'] / self.stats['texts_viewed']) * 100
                    print(f"  - Taxa de cache hit: {hit_rate:.1f}%")

                # Métricas de tempo de leitura
                if self.stats['cache_hits'] > 0:
                    avg_hit_time_us = (self.stats['total_hit_time'] / self.stats['cache_hits']) * 1_000_000
                    print(f"  - Tempo médio (com cache): {avg_hit_time_us:.2f}µs")
                if self.stats['cache_misses'] > 0:
                    avg_miss_time_ms = (self.stats['total_miss_time'] / self.stats['cache_misses']) * 1000
                    print(f"  - Tempo médio (sem cache): {avg_miss_time_ms:.2f}ms")
                print()

                user_input = input("Digite o número do texto desejado: ").strip()
                return int(user_input)
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.")
            except KeyboardInterrupt:
                return 0

    def display_text(self, text_id, content, was_cached, load_time, algorithm):
        """
        Exibe um texto para o usuário

        Args:
            text_id (int): ID do texto
            content (str): Conteúdo do texto
            was_cached (bool): Se o texto estava em cache
            load_time (float): Tempo de carregamento
            algorithm (str): Algoritmo de cache usado
        """
        self.clear_screen()

        # Atualizar estatísticas
        self.stats['texts_viewed'] += 1
        self.stats['total_time'] += load_time
        if was_cached:
            self.stats['cache_hits'] += 1
            self.stats['total_hit_time'] += load_time
        else:
            self.stats['cache_misses'] += 1
            self.stats['total_miss_time'] += load_time

        # Cabeçalho
        print("="*80)
        print(f"TEXTO {text_id:03d} | {datetime.now().strftime('%H:%M:%S')}")
        print("="*80)

        # Informações de performance
        cache_status = "CACHE HIT" if was_cached else "CACHE MISS (carregado do disco)"
        print(f"Status: {cache_status}")
        print(f"Algoritmo: {algorithm}")
        print(f"Tempo de carregamento: {load_time:.3f}s")
        print(f"Tamanho: {len(content)} caracteres | {len(content.split())} palavras")
        print("-"*80)
        print()

        # Conteúdo do texto (primeiras linhas)
        lines = content.split('\n')
        max_lines = 30  # Limitar exibição para não poluir terminal

        for i, line in enumerate(lines[:max_lines]):
            print(line)
            if i > 0 and i % 20 == 0:  # Pausar a cada 20 linhas
                input("\nPressione Enter para continuar a leitura...")

        if len(lines) > max_lines:
            print(f"\n... ({len(lines) - max_lines} linhas restantes)")
            print("\nTexto completo disponível para leitura.")

        print("\n" + "="*80)
        input("Pressione Enter para voltar ao menu...")

    def show_error(self, message):
        """
        Exibe mensagem de erro

        Args:
            message (str): Mensagem de erro
        """
        print(f"\n❌ ERRO: {message}\n")

    def show_goodbye(self):
        """Exibe mensagem de despedida"""
        print("\n" + "="*50)
        print("    OBRIGADO POR USAR O SISTEMA!")
        print("="*50)
        print(f"Sessão finalizada às {datetime.now().strftime('%H:%M:%S')}")
        print("\nEstatísticas finais:")
        print(f"  - Textos visualizados: {self.stats['texts_viewed']}")
        print(f"  - Cache hits: {self.stats['cache_hits']}")
        print(f"  - Cache misses: {self.stats['cache_misses']}")
        if self.stats['texts_viewed'] > 0:
            hit_rate = (self.stats['cache_hits'] / self.stats['texts_viewed']) * 100
            print(f"  - Taxa de cache hit: {hit_rate:.1f}%")

            # Métricas de tempo com e sem cache
            if self.stats['cache_hits'] > 0:
                avg_hit_time_us = (self.stats['total_hit_time'] / self.stats['cache_hits']) * 1_000_000
                print(f"  - Tempo médio (com cache): {avg_hit_time_us:.2f}µs")
            if self.stats['cache_misses'] > 0:
                avg_miss_time_ms = (self.stats['total_miss_time'] / self.stats['cache_misses']) * 1000
                print(f"  - Tempo médio (sem cache): {avg_miss_time_ms:.2f}ms")

        print("="*50)

    def show_progress(self, current, total, message="Processando"):
        """
        Exibe barra de progresso

        Args:
            current (int): Progresso atual
            total (int): Total de itens
            message (str): Mensagem a exibir
        """
        percentage = (current / total) * 100
        bar_length = 40
        filled_length = int(bar_length * current // total)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        print(f'\r{message}: |{bar}| {percentage:.1f}% ({current}/{total})', end='', flush=True)

        if current == total:
            print()  # Nova linha ao finalizar

    def show_config_menu(self, current_config, available_algorithms):
        """Mostra o menu de configurações e retorna a nova configuração."""
        self.clear_screen()
        print("="*70)
        print("    CONFIGURAÇÕES")
        print("="*70)
        print("1. Alterar Algoritmo de Cache")
        print(f"   (Atual: {current_config['algorithm']})")
        print("\n2. Simulação de Atraso de Disco (DISK_DELAY_SIMULATION)")
        print(f"   - Habilitado: {'Sim' if current_config['disk_delay']['enabled'] else 'Não'}")
        print(f"   - Atraso Mínimo: {current_config['disk_delay']['min_delay'] * 1000:.0f} ms")
        print(f"   - Atraso Máximo: {current_config['disk_delay']['max_delay'] * 1000:.0f} ms")
        print("\n0. Voltar ao Menu Principal")
        print("="*70)

        choice = input("Escolha uma opção: ").strip()
        return choice

    def get_algorithm_choice(self, current_algorithm, available_algorithms):
        """Solicita ao usuário a escolha de um novo algoritmo de cache."""
        print("\nEscolha o novo algoritmo de cache:")
        for i, alg in enumerate(available_algorithms, 1):
            print(f"{i}. {alg} {'(Atual)' if alg == current_algorithm else ''}")

        while True:
            try:
                choice = int(input(f"Digite o número (1-{len(available_algorithms)}): ").strip())
                if 1 <= choice <= len(available_algorithms):
                    return available_algorithms[choice - 1]
                else:
                    self.show_error(f"Escolha um número entre 1 e {len(available_algorithms)}.")
            except ValueError:
                self.show_error("Entrada inválida. Digite um número.")

    def get_disk_delay_config(self, current_config):
        """Solicita ao usuário as novas configurações de atraso de disco."""
        new_config = current_config.copy()
        
        # Habilitar/Desabilitar
        while True:
            choice = input(f"Habilitar simulação de atraso? (s/n, atual: {'s' if current_config['enabled'] else 'n'}): ").strip().lower()
            if choice in ['s', 'n', '']:
                new_config['enabled'] = current_config['enabled'] if choice == '' else (choice == 's')
                break
            self.show_error("Digite 's' para sim ou 'n' para não.")

        # Atraso Mínimo
        while True:
            try:
                min_delay_ms = input(f"Atraso mínimo em ms (atual: {current_config['min_delay'] * 1000:.0f}): ").strip()
                if min_delay_ms == '':
                    break
                new_config['min_delay'] = float(min_delay_ms) / 1000.0
                break
            except ValueError:
                self.show_error("Entrada inválida. Digite um número.")

        # Atraso Máximo
        while True:
            try:
                max_delay_ms = input(f"Atraso máximo em ms (atual: {current_config['max_delay'] * 1000:.0f}): ").strip()
                if max_delay_ms == '':
                    break
                new_config['max_delay'] = float(max_delay_ms) / 1000.0
                if new_config['max_delay'] < new_config['min_delay']:
                    self.show_error("O atraso máximo não pode ser menor que o mínimo.")
                    new_config['max_delay'] = current_config['max_delay'] # Reverte
                else:
                    break
            except ValueError:
                self.show_error("Entrada inválida. Digite um número.")
        
        return new_config