"""
Gerador de relatórios e gráficos - Aluno D
Cria visualizações e análises dos resultados da simulação
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any
import json

from core.config.settings import GRAPHS_DIR, REPORT_CONFIG

class ReportGenerator:
    """
    Classe para gerar relatórios e visualizações dos resultados
    """

    def __init__(self):
        # Configurar estilo dos gráficos
        plt.style.use('default')
        sns.set_palette("husl")

        # Garantir que diretório de gráficos existe
        GRAPHS_DIR.mkdir(parents=True, exist_ok=True)
        self.graphs_dir = GRAPHS_DIR

    def generate_hit_rate_comparison(self, results: Dict) -> str:
        """
        Gera gráfico comparativo de hit rates entre algoritmos

        Args:
            results: Resultados da simulação

        Returns:
            Caminho do arquivo do gráfico salvo
        """
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Comparação de Hit Rates por Algoritmo e Distribuição', fontsize=16)

        algorithms = list(results['results_by_algorithm'].keys())
        distributions = ['uniform', 'poisson', 'weighted']

        # Gráfico 1: Hit rate médio por algoritmo
        ax1 = axes[0, 0]
        alg_hit_rates = []
        for alg in algorithms:
            alg_rates = []
            for dist in distributions:
                if dist in results['results_by_algorithm'][alg]:
                    users_results = results['results_by_algorithm'][alg][dist]
                    alg_rates.extend([user['hit_rate'] for user in users_results])
            alg_hit_rates.append(np.mean(alg_rates) if alg_rates else 0)

        bars1 = ax1.bar(algorithms, alg_hit_rates, color=['skyblue', 'lightgreen', 'lightcoral'])
        ax1.set_title('Hit Rate Médio por Algoritmo')
        ax1.set_ylabel('Hit Rate (%)')
        ax1.set_ylim(0, 100)

        # Adicionar valores nas barras
        for bar, rate in zip(bars1, alg_hit_rates):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    f'{rate:.1f}%', ha='center', va='bottom')

        # Gráfico 2: Hit rate por distribuição
        ax2 = axes[0, 1]
        dist_data = {dist: [] for dist in distributions}

        for alg in algorithms:
            for dist in distributions:
                if dist in results['results_by_algorithm'][alg]:
                    users_results = results['results_by_algorithm'][alg][dist]
                    dist_data[dist].extend([user['hit_rate'] for user in users_results])

        box_data = [dist_data[dist] for dist in distributions]
        bp = ax2.boxplot(box_data, labels=distributions, patch_artist=True)

        colors = ['lightblue', 'lightgreen', 'lightpink']
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)

        ax2.set_title('Distribuição de Hit Rates por Tipo')
        ax2.set_ylabel('Hit Rate (%)')
        ax2.set_ylim(0, 100)

        # Gráfico 3: Heatmap algoritmo vs distribuição
        ax3 = axes[1, 0]
        heatmap_data = []
        for alg in algorithms:
            row = []
            for dist in distributions:
                if dist in results['results_by_algorithm'][alg]:
                    users_results = results['results_by_algorithm'][alg][dist]
                    avg_rate = np.mean([user['hit_rate'] for user in users_results])
                    row.append(avg_rate)
                else:
                    row.append(0)
            heatmap_data.append(row)

        im = ax3.imshow(heatmap_data, cmap='RdYlGn', aspect='auto', vmin=0, vmax=100)
        ax3.set_xticks(range(len(distributions)))
        ax3.set_yticks(range(len(algorithms)))
        ax3.set_xticklabels(distributions)
        ax3.set_yticklabels(algorithms)
        ax3.set_title('Heatmap: Hit Rate por Combinação')

        # Adicionar valores no heatmap
        for i in range(len(algorithms)):
            for j in range(len(distributions)):
                ax3.text(j, i, f'{heatmap_data[i][j]:.1f}%', 
                        ha='center', va='center', color='black')

        plt.colorbar(im, ax=ax3, label='Hit Rate (%)')

        # Gráfico 4: Evolução temporal (usando primeiro algoritmo como exemplo)
        ax4 = axes[1, 1]
        first_alg = algorithms[0]
        first_dist = distributions[0]

        if (first_dist in results['results_by_algorithm'][first_alg] and 
            results['results_by_algorithm'][first_alg][first_dist]):

            user_result = results['results_by_algorithm'][first_alg][first_dist][0]
            cache_states = user_result.get('cache_states', [])

            if cache_states:
                x_vals = [state['request_number'] for state in cache_states]
                y_vals = [state['hit_rate_so_far'] for state in cache_states]

                ax4.plot(x_vals, y_vals, marker='o', markersize=4)
                ax4.set_title(f'Evolução Hit Rate - {first_alg} ({first_dist})')
                ax4.set_xlabel('Número de Requisições')
                ax4.set_ylabel('Hit Rate (%)')
                ax4.grid(True, alpha=0.3)

        plt.tight_layout()

        # Salvar gráfico
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"hit_rate_comparison_{timestamp}.png"
        filepath = self.graphs_dir / filename

        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()

        return str(filepath)

    def generate_load_time_analysis(self, results: Dict) -> str:
        """
        Gera análise de tempos de carregamento

        Args:
            results: Resultados da simulação

        Returns:
            Caminho do arquivo do gráfico salvo
        """
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Análise de Tempos de Carregamento', fontsize=16)

        algorithms = list(results['results_by_algorithm'].keys())
        distributions = ['uniform', 'poisson', 'weighted']

        # Coletar dados de tempo de carregamento
        load_time_data = {}
        for alg in algorithms:
            load_time_data[alg] = {}
            for dist in distributions:
                if dist in results['results_by_algorithm'][alg]:
                    users_results = results['results_by_algorithm'][alg][dist]
                    load_time_data[alg][dist] = [user['avg_load_time'] for user in users_results]

        # Gráfico 1: Tempo médio por algoritmo
        ax1 = axes[0, 0]
        alg_times = []
        for alg in algorithms:
            all_times = []
            for dist in distributions:
                if dist in load_time_data[alg]:
                    all_times.extend(load_time_data[alg][dist])
            alg_times.append(np.mean(all_times) if all_times else 0)

        bars = ax1.bar(algorithms, alg_times, color=['skyblue', 'lightgreen', 'lightcoral'])
        ax1.set_title('Tempo Médio de Carregamento por Algoritmo')
        ax1.set_ylabel('Tempo (segundos)')

        for bar, time_val in zip(bars, alg_times):
            ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.001,
                    f'{time_val:.3f}s', ha='center', va='bottom')

        # Gráfico 2: Comparação por distribuição
        ax2 = axes[0, 1]
        x_pos = np.arange(len(algorithms))
        width = 0.25

        for i, dist in enumerate(distributions):
            dist_times = []
            for alg in algorithms:
                if dist in load_time_data[alg] and load_time_data[alg][dist]:
                    dist_times.append(np.mean(load_time_data[alg][dist]))
                else:
                    dist_times.append(0)

            ax2.bar(x_pos + i * width, dist_times, width, label=dist, alpha=0.8)

        ax2.set_title('Tempo de Carregamento por Algoritmo e Distribuição')
        ax2.set_xlabel('Algoritmo')
        ax2.set_ylabel('Tempo (segundos)')
        ax2.set_xticks(x_pos + width)
        ax2.set_xticklabels(algorithms)
        ax2.legend()

        # Gráfico 3: Correlação Hit Rate vs Tempo
        ax3 = axes[1, 0]
        for i, alg in enumerate(algorithms):
            hit_rates = []
            load_times = []
            for dist in distributions:
                if dist in results['results_by_algorithm'][alg]:
                    users_results = results['results_by_algorithm'][alg][dist]
                    hit_rates.extend([user['hit_rate'] for user in users_results])
                    load_times.extend([user['avg_load_time'] for user in users_results])

            if hit_rates and load_times:
                ax3.scatter(hit_rates, load_times, label=alg, alpha=0.7, s=50)

        ax3.set_title('Correlação: Hit Rate vs Tempo de Carregamento')
        ax3.set_xlabel('Hit Rate (%)')
        ax3.set_ylabel('Tempo de Carregamento (s)')
        ax3.legend()
        ax3.grid(True, alpha=0.3)

        # Gráfico 4: Distribuição de tempos
        ax4 = axes[1, 1]
        all_times_by_alg = {}
        for alg in algorithms:
            all_times = []
            for dist in distributions:
                if dist in load_time_data[alg]:
                    all_times.extend(load_time_data[alg][dist])
            all_times_by_alg[alg] = all_times

        ax4.hist([all_times_by_alg[alg] for alg in algorithms], 
                bins=20, alpha=0.7, label=algorithms)
        ax4.set_title('Distribuição de Tempos de Carregamento')
        ax4.set_xlabel('Tempo (segundos)')
        ax4.set_ylabel('Frequência')
        ax4.legend()

        plt.tight_layout()

        # Salvar gráfico
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"load_time_analysis_{timestamp}.png"
        filepath = self.graphs_dir / filename

        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()

        return str(filepath)

    def generate_execution_time_analysis(self, results: Dict) -> str:
        """
        Gera análise de tempos de execução por usuário e distribuição.

        Args:
            results: Resultados da simulação

        Returns:
            Caminho do arquivo do gráfico salvo
        """
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Análise de Tempo de Execução por Usuário e Distribuição', fontsize=16)

        algorithms = list(results['results_by_algorithm'].keys())
        distributions = ['uniform', 'poisson', 'weighted']
        
        # Coletar dados
        data = []
        for alg in algorithms:
            for dist in distributions:
                if dist in results['results_by_algorithm'][alg]:
                    for user_result in results['results_by_algorithm'][alg][dist]:
                        data.append({
                            'user_id': user_result['user_id'],
                            'algorithm': alg,
                            'distribution': dist,
                            'avg_load_time': user_result['avg_load_time'],
                            'hit_rate': user_result['hit_rate']
                        })
        
        df = pd.DataFrame(data)

        # Gráfico 1: Tempo de execução por usuário
        ax1 = axes[0, 0]
        sns.barplot(ax=ax1, x='user_id', y='avg_load_time', hue='distribution', data=df, errorbar=None)
        ax1.set_title('Tempo Médio de Execução por Usuário')
        ax1.set_ylabel('Tempo Médio de Carregamento (s)')
        ax1.set_xlabel('ID do Usuário')
        ax1.legend(title='Distribuição')

        # Gráfico 2: Boxplot por tipo de distribuição
        ax2 = axes[0, 1]
        sns.boxplot(ax=ax2, x='distribution', y='avg_load_time', data=df)
        ax2.set_title('Distribuição dos Tempos de Execução')
        ax2.set_ylabel('Tempo Médio de Carregamento (s)')
        ax2.set_xlabel('Tipo de Distribuição')

        # Gráfico 3: Tempo de execução por distribuição e algoritmo
        ax3 = axes[1, 0]
        sns.barplot(ax=ax3, x='distribution', y='avg_load_time', hue='algorithm', data=df, errorbar=None)
        ax3.set_title('Tempo de Execução por Distribuição e Algoritmo')
        ax3.set_ylabel('Tempo Médio de Carregamento (s)')
        ax3.set_xlabel('Tipo de Distribuição')

        # Gráfico 4: Correlação Hit Rate vs. Tempo de Execução
        ax4 = axes[1, 1]
        sns.scatterplot(ax=ax4, x='hit_rate', y='avg_load_time', hue='algorithm', style='distribution', data=df, s=100)
        ax4.set_title('Correlação Hit Rate vs. Tempo de Execução')
        ax4.set_xlabel('Hit Rate (%)')
        ax4.set_ylabel('Tempo Médio de Carregamento (s)')
        ax4.grid(True, alpha=0.3)

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])

        # Salvar gráfico
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"execution_time_analysis_{timestamp}.png"
        filepath = self.graphs_dir / filename

        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()

        return str(filepath)

    def generate_text_access_analysis(self, results: Dict) -> str:
        """
        Gera análise dos padrões de acesso aos textos

        Args:
            results: Resultados da simulação

        Returns:
            Caminho do arquivo do gráfico salvo
        """
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Análise de Padrões de Acesso aos Textos', fontsize=16)

        # Coletar dados de acesso por texto
        text_access_counts = {i: 0 for i in range(1, 101)}

        for alg in results['results_by_algorithm'].values():
            for dist in alg.values():
                for user in dist:
                    for request in user['request_details']:
                        text_id = request['text_id']
                        text_access_counts[text_id] += 1

        # Gráfico 1: Distribuição geral de acessos
        ax1 = axes[0, 0]
        text_ids = list(text_access_counts.keys())
        access_counts = list(text_access_counts.values())

        ax1.bar(text_ids, access_counts, alpha=0.7, color='skyblue')
        ax1.set_title('Distribuição de Acessos por Texto')
        ax1.set_xlabel('ID do Texto')
        ax1.set_ylabel('Número de Acessos')
        ax1.grid(True, alpha=0.3)

        # Destacar região 30-40
        ax1.axvspan(30, 40, alpha=0.2, color='red', label='Textos 30-40 (43% esperado)')
        ax1.legend()

        # Gráfico 2: Top 20 textos mais acessados
        ax2 = axes[0, 1]
        sorted_texts = sorted(text_access_counts.items(), key=lambda x: x[1], reverse=True)
        top_20 = sorted_texts[:20]

        top_ids = [str(item[0]) for item in top_20]
        top_counts = [item[1] for item in top_20]

        ax2.bar(range(len(top_20)), top_counts, color='lightgreen')
        ax2.set_title('Top 20 Textos Mais Acessados')
        ax2.set_xlabel('Ranking')
        ax2.set_ylabel('Número de Acessos')
        ax2.set_xticks(range(0, len(top_20), 2))
        ax2.set_xticklabels([top_ids[i] for i in range(0, len(top_20), 2)], rotation=45)

        # Gráfico 3: Análise da região especial (30-40)
        ax3 = axes[1, 0]
        special_range_counts = [text_access_counts[i] for i in range(30, 41)]
        other_counts = [text_access_counts[i] for i in range(1, 101) if not (30 <= i <= 40)]

        data_to_plot = [special_range_counts, other_counts]
        labels = ['Textos 30-40', 'Outros Textos']
        colors = ['lightcoral', 'lightblue']

        bp = ax3.boxplot(data_to_plot, labels=labels, patch_artist=True)
        for patch, color in zip(bp['boxes'], colors):
            patch.set_facecolor(color)

        ax3.set_title('Comparação: Textos Especiais vs Outros')
        ax3.set_ylabel('Número de Acessos')

        # Gráfico 4: Heatmap de acessos
        ax4 = axes[1, 1]

        # Reorganizar dados em matriz 10x10
        heatmap_data = np.zeros((10, 10))
        for text_id, count in text_access_counts.items():
            row = (text_id - 1) // 10
            col = (text_id - 1) % 10
            heatmap_data[row][col] = count

        im = ax4.imshow(heatmap_data, cmap='YlOrRd', aspect='auto')
        ax4.set_title('Heatmap de Acessos aos Textos')

        # Configurar ticks
        ax4.set_xticks(range(10))
        ax4.set_yticks(range(10))
        ax4.set_xticklabels([f'{i+1}-{i+10}' for i in range(0, 100, 10)])
        ax4.set_yticklabels([f'{i*10+1}-{(i+1)*10}' for i in range(10)])

        plt.colorbar(im, ax=ax4, label='Número de Acessos')

        plt.tight_layout()

        # Salvar gráfico
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"text_access_analysis_{timestamp}.png"
        filepath = self.graphs_dir / filename

        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()

        return str(filepath)

    def generate_summary_report(self, results: Dict) -> str:
        """
        Gera relatório textual detalhado da simulação.

        Args:
            results: Resultados da simulação.

        Returns:
            Caminho do arquivo de relatório salvo.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"simulation_report_{timestamp}.md"
        filepath = self.graphs_dir.parent / "docs" / filename

        filepath.parent.mkdir(parents=True, exist_ok=True)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write("# Relatório Detalhado de Simulação - Algoritmos de Cache\n\n")
            f.write(f"**Data da Simulação:** {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n")

            # Configuração da Simulação
            f.write("## 1. Configuração da Simulação\n\n")
            config = results['simulation_info']['config']
            f.write(f"- **Algoritmos Testados:** {config['algorithms']}\n")
            f.write(f"- **Requisições por Usuário:** {config['requests_per_user']}\n")
            f.write(f"- **Tamanho do Cache:** {results['simulation_info']['cache_size']}\n")
            f.write("- **Cenários de Usuário:**\n")
            for scenario in config['user_scenarios']:
                f.write(f"  - **Usuário {scenario['user_id']}:** Distribuição `{scenario['distribution']}`\n")

            # Resultados Consolidados
            f.write("\n## 2. Resultados Consolidados\n\n")
            summary = results['summary_stats']
            f.write("| Algoritmo | Hit Rate Médio | Tempo Médio de Carga | Melhor Distribuição |\n")
            f.write("|:---:|:---:|:---:|:---:|\n")
            for alg, stats in summary['by_algorithm'].items():
                f.write(f"| **{alg}** | {stats['avg_hit_rate']:.2f}% | {stats['avg_load_time']:.4f}s | {stats['best_distribution']} |\n")

            # Recomendação Final
            best = summary['overall_best']
            f.write("\n### **Algoritmo Recomendado:**\n")
            f.write(f"> O algoritmo **{best['algorithm']}** apresentou o melhor desempenho geral, com um Hit Rate médio de **{best['hit_rate']:.2f}%**.\n")

            # Análise Detalhada
            f.write("\n## 3. Análise Detalhada por Combinação\n")
            for alg, distributions in results['results_by_algorithm'].items():
                f.write(f"\n### 3.1. Algoritmo: {alg}\n")
                for dist, users in distributions.items():
                    f.write(f"\n#### Distribuição: {dist}\n")
                    for user_result in users:
                        f.write(f"- **Usuário {user_result['user_id']}**\n")
                        f.write(f"  - **Hit Rate:** {user_result['hit_rate']:.2f}%\n")
                        f.write(f"  - **Miss Rate:** {user_result['miss_rate']:.2f}%\n")
                        f.write(f"  - **Tempo Médio de Carga:** {user_result['avg_load_time']:.4f}s\n")
                        
                        # Estatísticas do usuário
                        user_stats = user_result.get('user_stats', {})
                        if user_stats.get('most_requested'):
                            top_3 = user_stats['most_requested'][:3]
                            f.write(f"  - **Top 3 Textos Mais Acessados:** {', '.join([str(t) for t in top_3])}\n")

                        # Amostra de estados do cache
                        cache_states = user_result.get('cache_states', [])
                        if cache_states:
                            f.write("  - **Amostra de Evolução do Cache:**\n")
                            f.write("    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |\n")
                            f.write("    |:---:|:---:|:---|\n")
                            # Pegar 3 amostras: início, meio e fim
                            sample_indices = [0, len(cache_states) // 2, len(cache_states) - 1]
                            for i in sample_indices:
                                state = cache_states[i]
                                contents = ", ".join(map(str, state['cache_contents']))
                                f.write(f"    | {state['request_number']} | {state['cache_size']} / {results['simulation_info']['cache_size']} | {contents} |\n")

                        # Amostra de requisições
                        req_details = user_result.get('request_details', [])
                        if req_details:
                            f.write("  - **Amostra de Requisições:**\n")
                            f.write("    | Nº | ID Texto | Resultado | Tempo de Carga |\n")
                            f.write("    |:---:|:---:|:---:|:---:|\n")
                            # Pegar 5 amostras, incluindo hits e misses
                            hits = [r for r in req_details if r['was_cache_hit']][:3]
                            misses = [r for r in req_details if not r['was_cache_hit']][:2]
                            for r in hits + misses:
                                result_text = "HIT" if r['was_cache_hit'] else "MISS"
                                f.write(f"    | {r['request_number']} | {r['text_id']} | {result_text} | {r['load_time']:.4f}s |\n")

            # Conclusões
            f.write("\n## 4. Conclusões Finais\n\n")
            f.write("1. **Análise de Performance:** O relatório detalhado e os gráficos anexos fornecem uma visão completa do comportamento de cada algoritmo. A escolha do algoritmo ideal pode depender do padrão de acesso esperado (distribuição).\n")
            f.write(f"2. **Recomendação Prática:** Com base nos resultados, o algoritmo **{best['algorithm']}** é o mais robusto para os cenários testados. Recomenda-se sua implementação para otimizar o tempo de acesso e a eficiência do sistema de cache.\n")
            f.write("3. **Próximos Passos:** Analisar os gráficos de `hit_rate`, `load_time` e `text_access` para obter insights visuais sobre a performance.\n")

        return str(filepath)

    def generate_all_reports(self, results: Dict) -> List[str]:
        """
        Gera todos os relatórios e gráficos

        Args:
            results: Resultados da simulação

        Returns:
            Lista com caminhos de todos os arquivos gerados
        """
        generated_files = []

        print("\nGerando relatórios...")

        try:
            # Gráfico de hit rates
            hit_rate_file = self.generate_hit_rate_comparison(results)
            generated_files.append(hit_rate_file)
            print(f"✓ Gráfico de hit rates: {hit_rate_file}")

            # Análise de tempos
            load_time_file = self.generate_load_time_analysis(results)
            generated_files.append(load_time_file)
            print(f"✓ Análise de tempos: {load_time_file}")

            # Análise de acessos
            access_file = self.generate_text_access_analysis(results)
            generated_files.append(access_file)
            print(f"✓ Análise de acessos: {access_file}")

            # Análise de tempo de execução
            execution_time_file = self.generate_execution_time_analysis(results)
            generated_files.append(execution_time_file)
            print(f"✓ Análise de tempo de execução: {execution_time_file}")

            # Relatório textual
            report_file = self.generate_summary_report(results)
            generated_files.append(report_file)
            print(f"✓ Relatório resumo: {report_file}")

        except Exception as e:
            print(f"Erro ao gerar relatórios: {e}")
            # Continuar mesmo com erros

        return generated_files
