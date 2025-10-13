# Relatório Detalhado de Simulação - Algoritmos de Cache

**Data da Simulação:** 12/10/2025 19:19:59

## 1. Configuração da Simulação

- **Algoritmos Testados:** ['FIFO', 'LRU', 'LFU']
- **Requisições por Usuário:** 200
- **Tamanho do Cache:** 10
- **Cenários de Usuário:**
  - **Usuário 1:** Distribuição `uniform`
  - **Usuário 2:** Distribuição `poisson`
  - **Usuário 3:** Distribuição `weighted`

## 2. Resultados Consolidados

| Algoritmo | Hit Rate Médio | Tempo Médio de Carga | Melhor Distribuição |
|:---:|:---:|:---:|:---:|
| **FIFO** | 24.33% | 0.0118s | poisson |
| **LRU** | 23.17% | 0.0119s | poisson |
| **LFU** | 23.67% | 0.0118s | poisson |

### **Algoritmo Recomendado:**
> O algoritmo **FIFO** apresentou o melhor desempenho geral, com um Hit Rate médio de **24.33%**.

## 3. Análise Detalhada por Combinação

### 3.1. Algoritmo: FIFO

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 10.00%
  - **Miss Rate:** 90.00%
  - **Tempo Médio de Carga:** 0.0138s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 96, 59, 82, 19, 79, 21, 43, 24, 20, 73 |
    | 150 | 10 / 10 | 98, 25, 4, 12, 17, 32, 80, 34, 92, 83 |
    | 200 | 10 / 10 | 28, 20, 94, 58, 11, 27, 81, 84, 50, 87 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 9 | 37 | HIT | 0.0000s |
    | 12 | 61 | HIT | 0.0000s |
    | 19 | 30 | HIT | 0.0000s |
    | 1 | 54 | MISS | 0.0132s |
    | 2 | 37 | MISS | 0.0168s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 42.50%
  - **Miss Rate:** 57.50%
  - **Tempo Médio de Carga:** 0.0090s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 44, 55, 56, 63, 51, 47, 58, 68, 48, 52 |
    | 150 | 10 / 10 | 66, 61, 50, 49, 53, 47, 43, 55, 52, 36 |
    | 200 | 10 / 10 | 52, 49, 45, 43, 44, 41, 40, 66, 51, 34 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 7 | 56 | HIT | 0.0000s |
    | 9 | 57 | HIT | 0.0000s |
    | 15 | 41 | HIT | 0.0000s |
    | 1 | 57 | MISS | 0.0109s |
    | 2 | 43 | MISS | 0.0199s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 20.50%
  - **Miss Rate:** 79.50%
  - **Tempo Médio de Carga:** 0.0126s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 38, 32, 73, 26, 42, 35, 20, 21, 28, 4 |
    | 150 | 10 / 10 | 100, 38, 97, 41, 7, 34, 72, 93, 76, 8 |
    | 200 | 10 / 10 | 54, 85, 26, 84, 22, 49, 39, 40, 81, 8 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 8 | 39 | HIT | 0.0000s |
    | 10 | 7 | HIT | 0.0000s |
    | 22 | 30 | HIT | 0.0000s |
    | 1 | 46 | MISS | 0.0158s |
    | 2 | 40 | MISS | 0.0203s |

### 3.1. Algoritmo: LRU

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 9.00%
  - **Miss Rate:** 91.00%
  - **Tempo Médio de Carga:** 0.0143s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 63, 29, 19, 47, 33, 91, 61, 13, 7, 85 |
    | 150 | 10 / 10 | 35, 92, 21, 79, 20, 29, 60, 77, 27, 26 |
    | 200 | 10 / 10 | 4, 61, 85, 8, 76, 91, 93, 77, 16, 15 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 31 | 13 | HIT | 0.0000s |
    | 35 | 93 | HIT | 0.0000s |
    | 45 | 33 | HIT | 0.0000s |
    | 1 | 36 | MISS | 0.0156s |
    | 2 | 96 | MISS | 0.0145s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 38.50%
  - **Miss Rate:** 61.50%
  - **Tempo Médio de Carga:** 0.0095s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 57, 44, 55, 42, 47, 56, 41, 37, 50, 48 |
    | 150 | 10 / 10 | 52, 53, 54, 48, 55, 51, 50, 49, 57, 44 |
    | 200 | 10 / 10 | 49, 55, 56, 58, 51, 47, 46, 48, 52, 43 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 5 | 51 | HIT | 0.0000s |
    | 8 | 49 | HIT | 0.0000s |
    | 11 | 47 | HIT | 0.0000s |
    | 1 | 49 | MISS | 0.0115s |
    | 2 | 35 | MISS | 0.0178s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 22.00%
  - **Miss Rate:** 78.00%
  - **Tempo Médio de Carga:** 0.0119s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 34, 32, 82, 18, 30, 77, 84, 2, 27, 36 |
    | 150 | 10 / 10 | 26, 34, 9, 51, 66, 89, 37, 80, 25, 31 |
    | 200 | 10 / 10 | 78, 81, 62, 30, 22, 49, 84, 3, 20, 31 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 11 | 53 | HIT | 0.0000s |
    | 14 | 40 | HIT | 0.0000s |
    | 21 | 69 | HIT | 0.0000s |
    | 1 | 53 | MISS | 0.0187s |
    | 2 | 32 | MISS | 0.0137s |

### 3.1. Algoritmo: LFU

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 8.50%
  - **Miss Rate:** 91.50%
  - **Tempo Médio de Carga:** 0.0139s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 6, 15, 93, 86, 33, 51, 28, 63, 69, 40 |
    | 150 | 10 / 10 | 6, 15, 93, 86, 33, 20, 77, 69, 23, 41 |
    | 200 | 10 / 10 | 6, 15, 93, 86, 33, 20, 77, 88, 70, 72 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 19 | 6 | HIT | 0.0000s |
    | 25 | 93 | HIT | 0.0000s |
    | 30 | 15 | HIT | 0.0001s |
    | 1 | 80 | MISS | 0.0194s |
    | 2 | 26 | MISS | 0.0127s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 37.00%
  - **Miss Rate:** 63.00%
  - **Tempo Médio de Carga:** 0.0097s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 51, 53, 65, 55, 47, 48, 57, 60, 46, 44 |
    | 150 | 10 / 10 | 51, 53, 65, 55, 47, 48, 57, 44, 45, 50 |
    | 200 | 10 / 10 | 51, 53, 65, 55, 47, 48, 57, 44, 45, 41 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 6 | 53 | HIT | 0.0000s |
    | 7 | 51 | HIT | 0.0000s |
    | 11 | 53 | HIT | 0.0000s |
    | 1 | 45 | MISS | 0.0163s |
    | 2 | 54 | MISS | 0.0159s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 25.50%
  - **Miss Rate:** 74.50%
  - **Tempo Médio de Carga:** 0.0118s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 39, 40, 38, 31, 13, 67, 18, 81, 27, 42 |
    | 150 | 10 / 10 | 39, 40, 38, 31, 81, 34, 35, 22, 72, 65 |
    | 200 | 10 / 10 | 39, 40, 38, 31, 81, 34, 35, 37, 84, 99 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 6 | 40 | HIT | 0.0000s |
    | 10 | 38 | HIT | 0.0000s |
    | 12 | 40 | HIT | 0.0000s |
    | 1 | 62 | MISS | 0.0108s |
    | 2 | 73 | MISS | 0.0121s |

## 4. Conclusões Finais

1. **Análise de Performance:** O relatório detalhado e os gráficos anexos fornecem uma visão completa do comportamento de cada algoritmo. A escolha do algoritmo ideal pode depender do padrão de acesso esperado (distribuição).
2. **Recomendação Prática:** Com base nos resultados, o algoritmo **FIFO** é o mais robusto para os cenários testados. Recomenda-se sua implementação para otimizar o tempo de acesso e a eficiência do sistema de cache.
3. **Próximos Passos:** Analisar os gráficos de `hit_rate`, `load_time` e `text_access` para obter insights visuais sobre a performance.
