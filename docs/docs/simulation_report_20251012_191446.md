# Relatório Detalhado de Simulação - Algoritmos de Cache

**Data da Simulação:** 12/10/2025 19:14:46

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
| **FIFO** | 22.00% | 0.0121s | poisson |
| **LRU** | 22.50% | 0.0122s | poisson |
| **LFU** | 23.50% | 0.0120s | poisson |

### **Algoritmo Recomendado:**
> O algoritmo **LFU** apresentou o melhor desempenho geral, com um Hit Rate médio de **23.50%**.

## 3. Análise Detalhada por Combinação

### 3.1. Algoritmo: FIFO

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 13.50%
  - **Miss Rate:** 86.50%
  - **Tempo Médio de Carga:** 0.0134s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 65, 26, 3, 32, 57, 27, 37, 45, 68, 38 |
    | 150 | 10 / 10 | 73, 75, 42, 68, 99, 76, 32, 91, 60, 7 |
    | 200 | 10 / 10 | 43, 61, 28, 95, 26, 74, 3, 71, 64, 15 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 11 | 95 | HIT | 0.0000s |
    | 12 | 32 | HIT | 0.0000s |
    | 21 | 93 | HIT | 0.0000s |
    | 1 | 32 | MISS | 0.0131s |
    | 2 | 44 | MISS | 0.0186s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 34.00%
  - **Miss Rate:** 66.00%
  - **Tempo Médio de Carga:** 0.0101s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 52, 47, 55, 66, 50, 43, 44, 49, 53, 54 |
    | 150 | 10 / 10 | 46, 52, 47, 48, 42, 63, 37, 43, 53, 50 |
    | 200 | 10 / 10 | 52, 62, 51, 48, 42, 57, 61, 53, 54, 47 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 3 | 58 | HIT | 0.0000s |
    | 11 | 53 | HIT | 0.0000s |
    | 14 | 53 | HIT | 0.0000s |
    | 1 | 58 | MISS | 0.0135s |
    | 2 | 54 | MISS | 0.0202s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 18.50%
  - **Miss Rate:** 81.50%
  - **Tempo Médio de Carga:** 0.0129s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 96, 7, 17, 32, 31, 9, 35, 13, 36, 88 |
    | 150 | 10 / 10 | 92, 38, 44, 36, 16, 33, 34, 37, 68, 32 |
    | 200 | 10 / 10 | 99, 41, 98, 39, 74, 2, 71, 68, 93, 33 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 6 | 30 | HIT | 0.0000s |
    | 10 | 30 | HIT | 0.0000s |
    | 14 | 32 | HIT | 0.0000s |
    | 1 | 30 | MISS | 0.0170s |
    | 2 | 89 | MISS | 0.0158s |

### 3.1. Algoritmo: LRU

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 10.00%
  - **Miss Rate:** 90.00%
  - **Tempo Médio de Carga:** 0.0139s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 36, 80, 39, 16, 38, 28, 94, 76, 27, 7 |
    | 150 | 10 / 10 | 42, 66, 58, 5, 23, 22, 83, 57, 49, 17 |
    | 200 | 10 / 10 | 74, 57, 47, 1, 91, 94, 89, 76, 9, 65 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 10 | 85 | HIT | 0.0000s |
    | 15 | 20 | HIT | 0.0000s |
    | 26 | 21 | HIT | 0.0000s |
    | 1 | 85 | MISS | 0.0178s |
    | 2 | 27 | MISS | 0.0117s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 37.50%
  - **Miss Rate:** 62.50%
  - **Tempo Médio de Carga:** 0.0100s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 64, 47, 45, 59, 48, 58, 43, 56, 55, 52 |
    | 150 | 10 / 10 | 55, 43, 45, 53, 42, 40, 49, 54, 44, 47 |
    | 200 | 10 / 10 | 63, 56, 49, 43, 40, 64, 46, 57, 45, 51 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 8 | 67 | HIT | 0.0000s |
    | 11 | 55 | HIT | 0.0000s |
    | 13 | 57 | HIT | 0.0000s |
    | 1 | 43 | MISS | 0.0115s |
    | 2 | 33 | MISS | 0.0196s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 20.00%
  - **Miss Rate:** 80.00%
  - **Tempo Médio de Carga:** 0.0126s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 55, 48, 9, 38, 39, 36, 77, 99, 31, 12 |
    | 150 | 10 / 10 | 47, 36, 37, 34, 90, 35, 30, 27, 59, 99 |
    | 200 | 10 / 10 | 35, 94, 34, 80, 97, 32, 37, 24, 39, 54 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 3 | 35 | HIT | 0.0000s |
    | 13 | 84 | HIT | 0.0000s |
    | 14 | 35 | HIT | 0.0000s |
    | 1 | 35 | MISS | 0.0143s |
    | 2 | 70 | MISS | 0.0134s |

### 3.1. Algoritmo: LFU

#### Distribuição: uniform
- **Usuário 1**
  - **Hit Rate:** 12.50%
  - **Miss Rate:** 87.50%
  - **Tempo Médio de Carga:** 0.0137s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 62, 89, 50, 49, 23, 17, 4, 28, 96, 48 |
    | 150 | 10 / 10 | 62, 89, 50, 49, 23, 28, 19, 29, 70, 41 |
    | 200 | 10 / 10 | 62, 89, 50, 49, 28, 19, 29, 70, 35, 13 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 11 | 89 | HIT | 0.0000s |
    | 18 | 62 | HIT | 0.0000s |
    | 19 | 50 | HIT | 0.0000s |
    | 1 | 40 | MISS | 0.0206s |
    | 2 | 2 | MISS | 0.0184s |

#### Distribuição: poisson
- **Usuário 2**
  - **Hit Rate:** 38.50%
  - **Miss Rate:** 61.50%
  - **Tempo Médio de Carga:** 0.0096s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 42, 52, 45, 43, 46, 48, 54, 59, 64, 56 |
    | 150 | 10 / 10 | 42, 52, 45, 43, 46, 56, 54, 63, 58, 55 |
    | 200 | 10 / 10 | 42, 52, 45, 43, 46, 56, 54, 63, 58, 60 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 7 | 43 | HIT | 0.0000s |
    | 8 | 45 | HIT | 0.0000s |
    | 13 | 45 | HIT | 0.0000s |
    | 1 | 53 | MISS | 0.0118s |
    | 2 | 42 | MISS | 0.0169s |

#### Distribuição: weighted
- **Usuário 3**
  - **Hit Rate:** 19.50%
  - **Miss Rate:** 80.50%
  - **Tempo Médio de Carga:** 0.0126s
  - **Amostra de Evolução do Cache:**
    | Nº Requisição | Tamanho Cache | Conteúdo (IDs) |
    |:---:|:---:|:---|
    | 50 | 10 / 10 | 91, 34, 40, 38, 31, 51, 14, 98, 66, 65 |
    | 150 | 10 / 10 | 91, 34, 40, 38, 31, 29, 28, 37, 19, 33 |
    | 200 | 10 / 10 | 91, 34, 40, 38, 31, 28, 37, 32, 36, 17 |
  - **Amostra de Requisições:**
    | Nº | ID Texto | Resultado | Tempo de Carga |
    |:---:|:---:|:---:|:---:|
    | 11 | 91 | HIT | 0.0000s |
    | 16 | 34 | HIT | 0.0000s |
    | 20 | 40 | HIT | 0.0000s |
    | 1 | 73 | MISS | 0.0137s |
    | 2 | 100 | MISS | 0.0200s |

## 4. Conclusões Finais

1. **Análise de Performance:** O relatório detalhado e os gráficos anexos fornecem uma visão completa do comportamento de cada algoritmo. A escolha do algoritmo ideal pode depender do padrão de acesso esperado (distribuição).
2. **Recomendação Prática:** Com base nos resultados, o algoritmo **LFU** é o mais robusto para os cenários testados. Recomenda-se sua implementação para otimizar o tempo de acesso e a eficiência do sistema de cache.
3. **Próximos Passos:** Analisar os gráficos de `hit_rate`, `load_time` e `text_access` para obter insights visuais sobre a performance.
