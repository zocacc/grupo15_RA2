# Relatório Detalhado de Simulação - Algoritmos de Cache

**Data da Simulação:** 13/10/2025 19:18:47

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
| **FIFO** | 21.50% | 0.0121s | poisson |
| **LRU** | 20.67% | 0.0123s | poisson |
| **LFU** | 25.17% | 0.0117s | poisson |
| **MRU** | 20.00% | 0.0124s | poisson |

### **Algoritmo Recomendado:**
> O algoritmo **LFU** apresentou o melhor desempenho geral, com um Hit Rate médio de **25.17%**.

## 3. Análise Detalhada por Combinação

### 3.1. Algoritmo: FIFO

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 9.50%
  - **Miss Rate:** 90.50%
  - **Tempo Médio de Carga:** 0.0139s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 1, 50, 93, 39, 65, 95, 48, 84, 25, 81 |
    | 150 | 10 / 10 | 2, 91, 40, 37, 52, 56, 50, 60, 89, 53 |
    | 200 | 10 / 10 | 27, 24, 98, 44, 86, 92, 61, 23, 5, 48 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 19 | 29 | HIT | 0.0000s |
    | 24 | 49 | HIT | 0.0000s |
    | 41 | 1 | HIT | 0.0000s |
    | 1 | 38 | MISS | 0.0129s |
    | 2 | 54 | MISS | 0.0172s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 41.50%
  - **Miss Rate:** 58.50%
  - **Tempo Médio de Carga:** 0.0090s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 50, 51, 37, 46, 44, 48, 58, 56, 36, 61 |
    | 150 | 10 / 10 | 50, 56, 63, 46, 60, 52, 54, 49, 44, 40 |
    | 200 | 10 / 10 | 45, 65, 47, 44, 64, 53, 34, 56, 63, 54 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 8 | 47 | HIT | 0.0000s |
    | 12 | 48 | HIT | 0.0000s |
    | 14 | 56 | HIT | 0.0000s |
    | 1 | 50 | MISS | 0.0109s |
    | 2 | 57 | MISS | 0.0119s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 13.50%
  - **Miss Rate:** 86.50%
  - **Tempo Médio de Carga:** 0.0134s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 76, 70, 79, 100, 16, 19, 30, 55, 34, 60 |
    | 150 | 10 / 10 | 34, 23, 32, 37, 36, 35, 95, 83, 44, 31 |
    | 200 | 10 / 10 | 29, 8, 37, 39, 96, 53, 21, 35, 40, 84 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 2 | 40 | HIT | 0.0000s |
    | 4 | 40 | HIT | 0.0000s |
    | 12 | 31 | HIT | 0.0000s |
    | 1 | 40 | MISS | 0.0188s |
    | 3 | 75 | MISS | 0.0149s |

### 3.1. Algoritmo: LRU

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 12.00%
  - **Miss Rate:** 88.00%
  - **Tempo Médio de Carga:** 0.0139s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 28, 19, 82, 17, 65, 84, 45, 8, 92, 78 |
    | 150 | 10 / 10 | 59, 28, 34, 84, 69, 41, 52, 56, 53, 15 |
    | 200 | 10 / 10 | 87, 19, 66, 30, 83, 32, 67, 17, 61, 18 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 17 | 86 | HIT | 0.0000s |
    | 22 | 83 | HIT | 0.0000s |
    | 23 | 4 | HIT | 0.0000s |
    | 1 | 34 | MISS | 0.0106s |
    | 2 | 90 | MISS | 0.0203s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 32.00%
  - **Miss Rate:** 68.00%
  - **Tempo Médio de Carga:** 0.0105s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 43, 49, 55, 51, 59, 66, 47, 56, 46, 50 |
    | 150 | 10 / 10 | 63, 54, 64, 65, 47, 52, 51, 46, 41, 56 |
    | 200 | 10 / 10 | 45, 40, 58, 53, 54, 44, 47, 59, 62, 49 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 9 | 51 | HIT | 0.0000s |
    | 13 | 41 | HIT | 0.0000s |
    | 18 | 59 | HIT | 0.0000s |
    | 1 | 50 | MISS | 0.0134s |
    | 2 | 56 | MISS | 0.0119s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 18.00%
  - **Miss Rate:** 82.00%
  - **Tempo Médio de Carga:** 0.0125s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 40, 30, 93, 38, 78, 22, 11, 15, 35, 71 |
    | 150 | 10 / 10 | 63, 31, 40, 62, 29, 68, 4, 95, 34, 30 |
    | 200 | 10 / 10 | 79, 85, 32, 17, 80, 72, 21, 39, 35, 38 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 12 | 38 | HIT | 0.0000s |
    | 27 | 31 | HIT | 0.0001s |
    | 31 | 31 | HIT | 0.0000s |
    | 1 | 34 | MISS | 0.0199s |
    | 2 | 65 | MISS | 0.0138s |

### 3.1. Algoritmo: LFU

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 12.00%
  - **Miss Rate:** 88.00%
  - **Tempo Médio de Carga:** 0.0138s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 34, 83, 53, 63, 30, 71, 20, 27, 33, 18 |
    | 150 | 10 / 10 | 34, 53, 63, 30, 71, 98, 73, 28, 81, 48 |
    | 200 | 10 / 10 | 34, 53, 63, 30, 71, 98, 73, 28, 81, 84 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 21 | 34 | HIT | 0.0000s |
    | 30 | 83 | HIT | 0.0000s |
    | 34 | 53 | HIT | 0.0000s |
    | 1 | 70 | MISS | 0.0200s |
    | 2 | 43 | MISS | 0.0138s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 38.00%
  - **Miss Rate:** 62.00%
  - **Tempo Médio de Carga:** 0.0095s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 47, 54, 55, 43, 58, 46, 40, 42, 67, 48 |
    | 150 | 10 / 10 | 47, 54, 55, 43, 58, 46, 50, 44, 49, 70 |
    | 200 | 10 / 10 | 47, 54, 55, 43, 58, 46, 50, 44, 49, 38 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 6 | 47 | HIT | 0.0000s |
    | 7 | 47 | HIT | 0.0000s |
    | 14 | 54 | HIT | 0.0000s |
    | 1 | 47 | MISS | 0.0124s |
    | 2 | 52 | MISS | 0.0194s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 25.50%
  - **Miss Rate:** 74.50%
  - **Tempo Médio de Carga:** 0.0117s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 31, 33, 38, 30, 35, 44, 45, 36, 40, 53 |
    | 150 | 10 / 10 | 31, 33, 38, 30, 35, 36, 23, 19, 90, 71 |
    | 200 | 10 / 10 | 31, 33, 38, 30, 35, 36, 23, 40, 39, 68 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 18 | 31 | HIT | 0.0000s |
    | 24 | 33 | HIT | 0.0000s |
    | 26 | 38 | HIT | 0.0000s |
    | 1 | 36 | MISS | 0.0131s |
    | 2 | 35 | MISS | 0.0189s |

### 3.1. Algoritmo: MRU

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 8.00%
  - **Miss Rate:** 92.00%
  - **Tempo Médio de Carga:** 0.0145s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 95, 4, 46, 7, 25, 79, 14, 20, 42, 100 |
    | 150 | 10 / 10 | 95, 46, 25, 79, 14, 75, 54, 92, 4, 20 |
    | 200 | 10 / 10 | 95, 46, 79, 14, 54, 92, 16, 4, 10, 84 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 21 | 36 | HIT | 0.0000s |
    | 37 | 20 | HIT | 0.0000s |
    | 38 | 10 | HIT | 0.0000s |
    | 1 | 10 | MISS | 0.0164s |
    | 2 | 95 | MISS | 0.0141s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 38.00%
  - **Miss Rate:** 62.00%
  - **Tempo Médio de Carga:** 0.0096s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 42, 61, 51, 41, 66, 55, 50, 53, 45, 32 |
    | 150 | 10 / 10 | 66, 49, 41, 40, 53, 46, 50, 55, 47, 48 |
    | 200 | 10 / 10 | 66, 48, 53, 47, 50, 55, 52, 54, 43, 59 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 7 | 47 | HIT | 0.0000s |
    | 10 | 54 | HIT | 0.0000s |
    | 12 | 57 | HIT | 0.0000s |
    | 1 | 42 | MISS | 0.0119s |
    | 2 | 47 | MISS | 0.0109s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 14.00%
  - **Miss Rate:** 86.00%
  - **Tempo Médio de Carga:** 0.0131s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 75, 65, 20, 89, 4, 35, 93, 24, 34, 87 |
    | 150 | 10 / 10 | 75, 20, 93, 65, 41, 26, 53, 36, 38, 24 |
    | 200 | 10 / 10 | 75, 65, 41, 53, 21, 42, 68, 36, 17, 78 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 7 | 31 | HIT | 0.0000s |
    | 21 | 73 | HIT | 0.0000s |
    | 25 | 31 | HIT | 0.0000s |
    | 1 | 75 | MISS | 0.0143s |
    | 2 | 65 | MISS | 0.0190s |

## 4. Conclusões Finais

1. **Análise de Performance:** O relatório detalhado e os gráficos anexos fornecem uma visão completa do comportamento de cada algoritmo. A escolha do algoritmo ideal pode depender do padrão de acesso esperado (distribuição).
2. **Recomendação Prática:** Com base nos resultados, o algoritmo **LFU** é o mais robusto para os cenários testados. Recomenda-se sua implementação para otimizar o tempo de acesso e a eficiência do sistema de cache.
3. **Próximos Passos:** Analisar os gráficos de `hit_rate`, `load_time` e `text_access` para obter insights visuais sobre a performance.
