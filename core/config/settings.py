"""
Arquivo de configurações do projeto de cache de textos
"""

import os
from pathlib import Path

# Diretório raiz do projeto
PROJECT_ROOT = Path(__file__).parent.parent.parent

# Configurações de cache
CACHE_SIZE = 10  # Máximo de 10 textos no cache, conforme especificado

# Diretórios
TEXT_DIR = PROJECT_ROOT / "texts"
DOCS_DIR = PROJECT_ROOT / "docs"
GRAPHS_DIR = DOCS_DIR / "graficos"

# Configurações de simulação
SIMULATION_CONFIG = {
    'requests_per_user': 200,
    'algorithms': ['FIFO', 'LRU', 'LFU', 'MRU'],
    'user_scenarios': [
        {'user_id': 1, 'distribution': 'uniform'},
        {'user_id': 2, 'distribution': 'poisson'},
        {'user_id': 3, 'distribution': 'weighted'}
    ]
}

# Configurações específicas das distribuições
DISTRIBUTION_PARAMS = {
    'poisson': {
        'lambda': 50  # Parâmetro lambda para distribuição de Poisson
    },
    'weighted': {
        'special_range': (30, 40),  # Textos especiais (30-40)
        'special_probability': 0.43,  # 43% de chance
        'normal_probability': 0.57   # 57% para outros textos
    }
}

# Configurações de performance
DISK_DELAY_SIMULATION = {
    'enabled': True,       # Simular lentidão do disco forense
    'min_delay': 0.01,      # Delay mínimo em segundos
    'max_delay': 0.02       # Delay máximo em segundos
}

# Configurações de relatórios
REPORT_CONFIG = {
    'save_graphs': True,
    'graph_formats': ['png', 'pdf'],
    'detailed_logs': True,
    'export_csv': True
}

# Validar diretórios necessários
def ensure_directories():
    """Cria diretórios necessários se não existirem"""
    directories = [TEXT_DIR, DOCS_DIR, GRAPHS_DIR]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

if __name__ == "__main__":
    ensure_directories()
    print("Diretórios configurados com sucesso!")
