"""
Testes para o gerenciador de textos
"""

import unittest
import tempfile
import os
import sys
from pathlib import Path

# Adicionar path do projeto
project_root = Path(__file__).parent.parent.parent
sys.path.append(str(project_root))

from core.text_manager import TextManager

class TestTextManager(unittest.TestCase):
    """Testes para TextManager"""

    def setUp(self):
        # Criar diretório temporário para testes
        self.temp_dir = tempfile.mkdtemp()
        self.text_manager = TextManager(self.temp_dir)

        # Criar alguns arquivos de teste
        self.create_test_files()

    def tearDown(self):
        # Limpar arquivos temporários
        import shutil
        shutil.rmtree(self.temp_dir)

    def create_test_files(self):
        """Criar arquivos de teste"""
        test_texts = {
            1: "Este é o texto número um com mais de mil palavras. " * 50,
            2: "Segundo texto para teste do sistema de cache. " * 50,
            3: "Terceiro documento com conteúdo extenso para validação. " * 50
        }

        for text_id, content in test_texts.items():
            file_path = Path(self.temp_dir) / f"texto_{text_id:03d}.txt"
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)

    def test_load_existing_text(self):
        """Teste carregamento de texto existente"""
        content = self.text_manager.load_text(1)
        self.assertIsNotNone(content)
        self.assertIn("texto número um", content)

    def test_load_nonexistent_text(self):
        """Teste carregamento de texto inexistente"""
        content = self.text_manager.load_text(999)
        self.assertIsNone(content)

    def test_invalid_text_id(self):
        """Teste IDs inválidos"""
        # ID fora do range
        self.assertIsNone(self.text_manager.load_text(0))
        self.assertIsNone(self.text_manager.load_text(101))
        self.assertIsNone(self.text_manager.load_text(-1))

    def test_get_text_info(self):
        """Teste informações do texto"""
        info = self.text_manager.get_text_info(1)

        self.assertIsNotNone(info)
        self.assertEqual(info['id'], 1)
        self.assertEqual(info['filename'], 'texto_001.txt')
        self.assertGreater(info['size_bytes'], 0)

    def test_list_available_texts(self):
        """Teste listagem de textos disponíveis"""
        available = self.text_manager.list_available_texts()

        self.assertIn(1, available)
        self.assertIn(2, available)
        self.assertIn(3, available)
        self.assertNotIn(4, available)

    def test_word_count(self):
        """Teste contagem de palavras"""
        count = self.text_manager.get_word_count(1)
        self.assertGreater(count, 100)  # Deve ter muitas palavras

    def test_disk_delay_simulation(self):
        """Teste simulação de lentidão do disco"""
        import time
        from core.config.settings import DISK_DELAY_SIMULATION

        if DISK_DELAY_SIMULATION['enabled']:
            start_time = time.time()
            self.text_manager.load_text(1)
            elapsed = time.time() - start_time

            # Deve haver algum delay
            min_expected = DISK_DELAY_SIMULATION['min_delay']
            self.assertGreaterEqual(elapsed, min_expected * 0.8)  # Margem de erro

if __name__ == "__main__":
    unittest.main(verbosity=2)
