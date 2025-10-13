"""
Módulo de gerenciamento de textos - Aluno A
Responsável por carregar e gerenciar os 100 textos do disco
"""

import time
import random
from pathlib import Path
from core.config import settings

class TextManager:
    """Classe responsável pelo carregamento dos textos do disco"""

    def __init__(self, texts_directory):
        self.texts_dir = Path(texts_directory)
        self.texts_dir.mkdir(parents=True, exist_ok=True)

        # Estatísticas de leitura do disco
        self.total_read_time = 0.0
        self.disk_reads = 0

        # Verificar se todos os textos existem
        self._validate_texts()

    def _validate_texts(self):
        """Valida se todos os 100 textos estão disponíveis"""
        missing_texts = []
        for i in range(1, 101):
            text_file = self.texts_dir / f"{i}.txt"
            if not text_file.exists():
                missing_texts.append(i)

        if missing_texts:
            print(f"AVISO: {len(missing_texts)} textos não encontrados: {missing_texts[:10]}...")
            print("Execute o script generate_texts.py para criar os textos em falta.")

    def load_text(self, text_id):
        """
        Carrega um texto do disco (simula lentidão do sistema forense)

        Args:
            text_id (int): ID do texto (1-100)

        Returns:
            str: Conteúdo do texto ou None se não encontrado
        """
        if not (1 <= text_id <= 100):
            return None

        text_file = self.texts_dir / f"{text_id}.txt"

        if not text_file.exists():
            return None

        # Simular lentidão do disco forense
        if settings.DISK_DELAY_SIMULATION['enabled']:
            delay = random.uniform(
                settings.DISK_DELAY_SIMULATION['min_delay'],
                settings.DISK_DELAY_SIMULATION['max_delay']
            )
            time.sleep(delay)

        try:
            start_time = time.perf_counter()
            with open(text_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            elapsed_time = time.perf_counter() - start_time
            self.total_read_time += elapsed_time
            self.disk_reads += 1
            
            return content
        except Exception as e:
            print(f"Erro ao carregar texto {text_id}: {e}")
            return None

    def get_read_stats(self):
        """Retorna estatísticas de leitura do disco."""
        return {
            'total_time': self.total_read_time,
            'count': self.disk_reads
        }

    def reset_stats(self):
        """Reseta as estatísticas de leitura."""
        self.total_read_time = 0.0
        self.disk_reads = 0

    def get_text_info(self, text_id):
        """
        Retorna informações sobre um texto sem carregá-lo

        Args:
            text_id (int): ID do texto

        Returns:
            dict: Informações do texto ou None
        """
        if not (1 <= text_id <= 100):
            return None

        text_file = self.texts_dir / f"{text_id}.txt"

        if not text_file.exists():
            return None

        try:
            stat = text_file.stat()
            return {
                'id': text_id,
                'filename': text_file.name,
                'size_bytes': stat.st_size,
                'modified_time': stat.st_mtime
            }
        except Exception as e:
            print(f"Erro ao obter informações do texto {text_id}: {e}")
            return None

    def list_available_texts(self):
        """
        Lista todos os textos disponíveis

        Returns:
            list: Lista de IDs dos textos disponíveis
        """
        available = []
        for i in range(1, 101):
            text_file = self.texts_dir / f"{i}.txt"
            if text_file.exists():
                available.append(i)
        return available

    def get_word_count(self, text_id):
        """
        Conta palavras de um texto (para validação)

        Args:
            text_id (int): ID do texto

        Returns:
            int: Número de palavras ou 0 se erro
        """
        content = self.load_text(text_id)
        if content:
            return len(content.split())
        return 0