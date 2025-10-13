"""
Geradores de números aleatórios para simulação - Aluno D
Implementa três tipos de distribuições: uniforme, Poisson e ponderada
"""

import random
import numpy as np
from typing import List, Tuple
from core.config.settings import DISTRIBUTION_PARAMS

class RandomGenerators:
    """
    Classe para gerar números aleatórios seguindo diferentes distribuições
    """

    def __init__(self, text_range: Tuple[int, int] = (1, 100)):
        """
        Inicializa o gerador

        Args:
            text_range: Tupla (min, max) do range de textos disponíveis
        """
        self.min_text, self.max_text = text_range
        self.poisson_params = DISTRIBUTION_PARAMS['poisson']
        self.weighted_params = DISTRIBUTION_PARAMS['weighted']

    def generate_uniform(self, num_samples: int) -> List[int]:
        """
        Gera números aleatórios com distribuição uniforme

        Args:
            num_samples: Número de amostras a gerar

        Returns:
            Lista de IDs de textos gerados aleatoriamente
        """
        return [random.randint(self.min_text, self.max_text) for _ in range(num_samples)]

    def generate_poisson(self, num_samples: int) -> List[int]:
        """
        Gera números aleatórios com distribuição de Poisson

        Args:
            num_samples: Número de amostras a gerar

        Returns:
            Lista de IDs de textos seguindo distribuição de Poisson
        """
        lambda_param = self.poisson_params['lambda']

        # Gerar números seguindo distribuição de Poisson
        poisson_values = np.random.poisson(lambda_param, num_samples)

        # Mapear valores para o range de textos (1-100)
        # Usar módulo para garantir que ficam no range
        mapped_values = []
        for value in poisson_values:
            # Mapear valor de Poisson para range de textos
            mapped_value = ((value % (self.max_text - self.min_text + 1)) + self.min_text)
            mapped_values.append(mapped_value)

        return mapped_values

    def generate_weighted(self, num_samples: int) -> List[int]:
        """
        Gera números aleatórios ponderados (textos 30-40 com 43% de chance)

        Args:
            num_samples: Número de amostras a gerar

        Returns:
            Lista de IDs de textos com distribuição ponderada
        """
        special_range = self.weighted_params['special_range']
        special_prob = self.weighted_params['special_probability']

        special_texts = list(range(special_range[0], special_range[1] + 1))
        normal_texts = [i for i in range(self.min_text, self.max_text + 1) 
                       if i not in special_texts]

        results = []
        for _ in range(num_samples):
            if random.random() < special_prob:
                # Escolher texto especial (30-40)
                text_id = random.choice(special_texts)
            else:
                # Escolher texto normal
                text_id = random.choice(normal_texts)
            results.append(text_id)

        return results

    def generate_mixed_distribution(self, num_samples: int, 
                                  uniform_weight: float = 0.33,
                                  poisson_weight: float = 0.33,
                                  weighted_weight: float = 0.34) -> List[int]:
        """
        Gera números usando uma mistura das três distribuições

        Args:
            num_samples: Número de amostras total
            uniform_weight: Peso da distribuição uniforme
            poisson_weight: Peso da distribuição de Poisson  
            weighted_weight: Peso da distribuição ponderada

        Returns:
            Lista de IDs de textos com distribuição mista
        """
        # Calcular quantos números gerar de cada tipo
        num_uniform = int(num_samples * uniform_weight)
        num_poisson = int(num_samples * poisson_weight)
        num_weighted = num_samples - num_uniform - num_poisson

        results = []

        # Gerar cada tipo
        if num_uniform > 0:
            results.extend(self.generate_uniform(num_uniform))
        if num_poisson > 0:
            results.extend(self.generate_poisson(num_poisson))
        if num_weighted > 0:
            results.extend(self.generate_weighted(num_weighted))

        # Embaralhar para misturar as distribuições
        random.shuffle(results)

        return results

    def analyze_distribution(self, samples: List[int]) -> dict:
        """
        Analisa uma lista de amostras e retorna estatísticas

        Args:
            samples: Lista de amostras a analisar

        Returns:
            Dicionário com estatísticas da distribuição
        """
        if not samples:
            return {}

        # Estatísticas básicas
        stats = {
            'total_samples': len(samples),
            'min_value': min(samples),
            'max_value': max(samples),
            'mean': np.mean(samples),
            'std': np.std(samples),
            'unique_values': len(set(samples))
        }

        # Frequência por valor
        frequency = {}
        for sample in samples:
            frequency[sample] = frequency.get(sample, 0) + 1

        stats['frequency_distribution'] = frequency

        # Análise específica para textos 30-40
        special_range = self.weighted_params['special_range']
        special_count = sum(1 for s in samples if special_range[0] <= s <= special_range[1])
        special_percentage = (special_count / len(samples)) * 100

        stats['special_range_analysis'] = {
            'range': special_range,
            'count': special_count,
            'percentage': special_percentage,
            'expected_percentage': self.weighted_params['special_probability'] * 100
        }

        return stats

    def validate_poisson_parameter(self, samples: List[int]) -> dict:
        """
        Valida se as amostras seguem uma distribuição de Poisson

        Args:
            samples: Lista de amostras geradas

        Returns:
            Dicionário com informações sobre a validação
        """
        # Remapear amostras para valores contínuos de Poisson
        remapped = [(s - self.min_text) for s in samples]

        # Calcular parâmetros estimados
        estimated_lambda = np.mean(remapped)
        theoretical_lambda = self.poisson_params['lambda']

        return {
            'theoretical_lambda': theoretical_lambda,
            'estimated_lambda': estimated_lambda,
            'difference': abs(estimated_lambda - theoretical_lambda),
            'relative_error': abs(estimated_lambda - theoretical_lambda) / theoretical_lambda * 100
        }

class UserSimulator:
    """
    Simula comportamento de diferentes usuários
    """

    def __init__(self, user_id: int, generator: RandomGenerators):
        self.user_id = user_id
        self.generator = generator
        self.access_history = []

    def simulate_session(self, num_requests: int, distribution_type: str) -> List[int]:
        """
        Simula uma sessão de usuário

        Args:
            num_requests: Número de requisições a fazer
            distribution_type: Tipo de distribuição ('uniform', 'poisson', 'weighted')

        Returns:
            Lista de IDs de textos requisitados
        """
        if distribution_type == 'uniform':
            requests = self.generator.generate_uniform(num_requests)
        elif distribution_type == 'poisson':
            requests = self.generator.generate_poisson(num_requests)
        elif distribution_type == 'weighted':
            requests = self.generator.generate_weighted(num_requests)
        else:
            raise ValueError(f"Tipo de distribuição desconhecido: {distribution_type}")

        self.access_history.extend(requests)
        return requests

    def get_user_stats(self) -> dict:
        """
        Retorna estatísticas do usuário

        Returns:
            Dicionário com estatísticas do usuário
        """
        if not self.access_history:
            return {'user_id': self.user_id, 'total_requests': 0}

        return {
            'user_id': self.user_id,
            'total_requests': len(self.access_history),
            'unique_texts': len(set(self.access_history)),
            'most_accessed': max(set(self.access_history), key=self.access_history.count),
            'access_distribution': self.generator.analyze_distribution(self.access_history)
        }
