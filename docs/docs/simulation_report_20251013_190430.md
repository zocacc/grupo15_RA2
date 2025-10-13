# Relatório Detalhado de Simulação - Algoritmos de Cache

**Data da Simulação:** 13/10/2025 19:04:31

## 1. Configuração da Simulação

- **Algoritmos Testados:** ['FIFO', 'LRU', 'LFU', 'MRU']
- **Requisições por Usuário:** 200
- **Tamanho do Cache:** 10
- **Cenários de Usuário:**
  - **Usuário 1:** Distribuição `uniform`
  - **Usuário 2:** Distribuição `poisson`
  - **Usuário 3:** Distribuição `weighted`

## 2. Resultados Consolidados

| Algoritmo | Hit Rate Médio | Tempo Médio de Carga | Melhor Distribuição |
|:---:|:---:|:---:|:---:|
| **FIFO** | 20.50% | 0.0124s | poisson |
| **LRU** | 22.83% | 0.0120s | poisson |
| **LFU** | 27.00% | 0.0113s | poisson |
| **MRU** | 18.67% | 0.0127s | poisson |

### **Algoritmo Recomendado:**
> O algoritmo **LFU** apresentou o melhor desempenho geral, com um Hit Rate médio de **27.00%**.

## 3. Análise Detalhada por Combinação

### 3.1. Algoritmo: FIFO

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 11.00%
  - **Miss Rate:** 89.00%
  - **Tempo Médio de Carga:** 0.0137s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 4, 1, 76, 75, 16, 43, 5, 9, 47, 48 |
    | 150 | 10 / 10 | 42, 3, 69, 40, 7, 23, 66, 85, 51, 56 |
    | 200 | 10 / 10 | 49, 55, 31, 14, 50, 15, 27, 39, 24, 47 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 19 | 1 | HIT | 0.0000s |
    | 21 | 17 | HIT | 0.0000s |
    | 25 | 33 | HIT | 0.0000s |
    | 1 | 9 | MISS | 0.0236s |
    | 2 | 6 | MISS | 0.0201s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 34.00%
  - **Miss Rate:** 66.00%
  - **Tempo Médio de Carga:** 0.0106s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 49, 42, 47, 54, 45, 53, 59, 51, 63, 48 |
    | 150 | 10 / 10 | 62, 45, 35, 50, 61, 60, 52, 42, 57, 40 |
    | 200 | 10 / 10 | 44, 61, 37, 48, 54, 42, 41, 62, 45, 46 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 9 | 61 | HIT | 0.0000s |
    | 11 | 54 | HIT | 0.0000s |
    | 12 | 51 | HIT | 0.0000s |
    | 1 | 54 | MISS | 0.0141s |
    | 2 | 58 | MISS | 0.0287s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 16.50%
  - **Miss Rate:** 83.50%
  - **Tempo Médio de Carga:** 0.0131s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 32, 13, 51, 33, 39, 34, 22, 46, 30, 14 |
    | 150 | 10 / 10 | 98, 37, 25, 32, 30, 39, 55, 5, 74, 33 |
    | 200 | 10 / 10 | 42, 33, 38, 30, 39, 32, 40, 34, 53, 100 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 5 | 71 | HIT | 0.0000s |
    | 6 | 32 | HIT | 0.0000s |
    | 8 | 33 | HIT | 0.0000s |
    | 1 | 30 | MISS | 0.0146s |
    | 2 | 71 | MISS | 0.0183s |

### 3.1. Algoritmo: LRU

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 9.00%
  - **Miss Rate:** 91.00%
  - **Tempo Médio de Carga:** 0.0140s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 26, 99, 39, 95, 22, 84, 86, 21, 72, 18 |
    | 150 | 10 / 10 | 57, 62, 56, 69, 77, 4, 47, 71, 93, 52 |
    | 200 | 10 / 10 | 17, 15, 39, 20, 59, 80, 22, 75, 19, 63 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 25 | 34 | HIT | 0.0000s |
    | 34 | 60 | HIT | 0.0000s |
    | 48 | 21 | HIT | 0.0000s |
    | 1 | 90 | MISS | 0.0139s |
    | 2 | 91 | MISS | 0.0118s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 39.00%
  - **Miss Rate:** 61.00%
  - **Tempo Médio de Carga:** 0.0097s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 50, 44, 66, 43, 52, 57, 59, 62, 54, 61 |
    | 150 | 10 / 10 | 60, 45, 58, 51, 47, 40, 63, 56, 52, 69 |
    | 200 | 10 / 10 | 58, 53, 50, 45, 38, 46, 51, 43, 52, 57 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 7 | 47 | HIT | 0.0000s |
    | 8 | 44 | HIT | 0.0000s |
    | 11 | 57 | HIT | 0.0000s |
    | 1 | 46 | MISS | 0.0168s |
    | 2 | 57 | MISS | 0.0163s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 20.50%
  - **Miss Rate:** 79.50%
  - **Tempo Médio de Carga:** 0.0122s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 25, 50, 4, 38, 6, 33, 36, 43, 40, 23 |
    | 150 | 10 / 10 | 20, 8, 33, 36, 90, 30, 22, 39, 77, 55 |
    | 200 | 10 / 10 | 33, 14, 32, 36, 57, 75, 40, 34, 31, 81 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 13 | 39 | HIT | 0.0000s |
    | 15 | 31 | HIT | 0.0000s |
    | 16 | 31 | HIT | 0.0000s |
    | 1 | 33 | MISS | 0.0112s |
    | 2 | 64 | MISS | 0.0178s |

### 3.1. Algoritmo: LFU

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 10.00%
  - **Miss Rate:** 90.00%
  - **Tempo Médio de Carga:** 0.0139s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 89, 18, 20, 83, 62, 66, 3, 44, 33, 37 |
    | 150 | 10 / 10 | 89, 18, 62, 37, 8, 87, 7, 20, 17, 96 |
    | 200 | 10 / 10 | 89, 62, 37, 8, 87, 7, 20, 46, 59, 69 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 4 | 89 | HIT | 0.0000s |
    | 19 | 18 | HIT | 0.0000s |
    | 50 | 62 | HIT | 0.0000s |
    | 1 | 86 | MISS | 0.0162s |
    | 2 | 2 | MISS | 0.0174s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 41.50%
  - **Miss Rate:** 58.50%
  - **Tempo Médio de Carga:** 0.0091s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 48, 45, 47, 54, 60, 49, 50, 52, 53, 62 |
    | 150 | 10 / 10 | 48, 45, 47, 54, 60, 49, 50, 52, 53, 59 |
    | 200 | 10 / 10 | 48, 45, 47, 54, 60, 49, 50, 52, 53, 57 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 10 | 45 | HIT | 0.0000s |
    | 11 | 48 | HIT | 0.0000s |
    | 12 | 48 | HIT | 0.0000s |
    | 1 | 48 | MISS | 0.0112s |
    | 2 | 45 | MISS | 0.0185s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 29.50%
  - **Miss Rate:** 70.50%
  - **Tempo Médio de Carga:** 0.0109s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 37, 34, 86, 29, 31, 33, 35, 57, 88, 38 |
    | 150 | 10 / 10 | 37, 34, 86, 31, 33, 35, 39, 30, 40, 69 |
    | 200 | 10 / 10 | 37, 34, 86, 31, 33, 35, 39, 30, 40, 87 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 10 | 29 | HIT | 0.0000s |
    | 11 | 34 | HIT | 0.0000s |
    | 12 | 34 | HIT | 0.0000s |
    | 1 | 64 | MISS | 0.0145s |
    | 2 | 40 | MISS | 0.0129s |

### 3.1. Algoritmo: MRU

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 6.50%
  - **Miss Rate:** 93.50%
  - **Tempo Médio de Carga:** 0.0147s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 96, 23, 54, 40, 22, 92, 97, 78, 55, 19 |
    | 150 | 10 / 10 | 96, 40, 22, 78, 7, 82, 60, 71, 28, 27 |
    | 200 | 10 / 10 | 40, 22, 78, 7, 82, 60, 71, 28, 4, 56 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 2 | 96 | HIT | 0.0000s |
    | 5 | 23 | HIT | 0.0000s |
    | 17 | 87 | HIT | 0.0000s |
    | 1 | 96 | MISS | 0.0200s |
    | 3 | 53 | MISS | 0.0119s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 34.50%
  - **Miss Rate:** 65.50%
  - **Tempo Médio de Carga:** 0.0103s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 53, 55, 63, 45, 42, 47, 62, 52, 46, 57 |
    | 150 | 10 / 10 | 63, 64, 58, 44, 42, 39, 53, 50, 47, 57 |
    | 200 | 10 / 10 | 63, 39, 61, 59, 37, 45, 44, 43, 54, 48 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 10 | 45 | HIT | 0.0000s |
    | 12 | 54 | HIT | 0.0000s |
    | 14 | 50 | HIT | 0.0000s |
    | 1 | 53 | MISS | 0.0177s |
    | 2 | 58 | MISS | 0.0169s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 15.00%
  - **Miss Rate:** 85.00%
  - **Tempo Médio de Carga:** 0.0132s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 41, 13, 94, 47, 15, 40, 22, 10, 62, 35 |
    | 150 | 10 / 10 | 41, 13, 47, 15, 62, 27, 77, 3, 30, 39 |
    | 200 | 10 / 10 | 41, 13, 47, 15, 62, 27, 3, 49, 6, 33 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 9 | 30 | HIT | 0.0000s |
    | 13 | 33 | HIT | 0.0000s |
    | 20 | 30 | HIT | 0.0000s |
    | 1 | 31 | MISS | 0.0190s |
    | 2 | 41 | MISS | 0.0123s |

## 4. Conclusões Finais

1. **Análise de Performance:** O relatório detalhado e os gráficos anexos fornecem uma visão completa do comportamento de cada algoritmo. A escolha do algoritmo ideal pode depender do padrão de acesso esperado (distribuição).
2. **Recomendação Prática:** Com base nos resultados, o algoritmo **LFU** é o mais robusto para os cenários testados. Recomenda-se sua implementação para otimizar o tempo de acesso e a eficiência do sistema de cache.
3. **Próximos Passos:** Analisar os gráficos de `hit_rate`, `load_time` e `text_access` para obter insights visuais sobre a performance.
