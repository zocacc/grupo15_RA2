# 📝 Sistema de Simulação de Cache de Textos

Este projeto oferece uma plataforma para simular, analisar e comparar o desempenho de diferentes algoritmos de substituição de cache em um cenário de leitura de textos. O sistema foi projetado para ser uma ferramenta educacional e de análise, permitindo a avaliação de algoritmos como FIFO, LRU, LFU e MRU em um ambiente controlado.

## ✨ Funcionalidades Principais

- **Modo Interativo**: Permite ao usuário solicitar textos manualmente e observar o comportamento do cache em tempo real, incluindo hits e misses.
- **Modo de Simulação Avançado**: Executa simulações automatizadas com múltiplos usuários virtuais e diferentes padrões de acesso a textos (uniforme, ponderado e Poisson) para uma análise robusta.
- **Múltiplos Algoritmos de Cache**: Inclui implementações dos algoritmos FIFO, LRU, LFU e MRU, permitindo uma comparação direta de desempenho.
- **Métricas Detalhadas**: Coleta e exibe estatísticas cruciais, como taxa de acertos (hit rate), taxa de falhas (miss rate), tempo de carregamento de textos e tempo total de execução.
- **Geração Automática de Relatórios**: Ao final da simulação, gera relatórios completos em formato Markdown e gráficos visuais (PNG) que comparam os algoritmos, salvos no diretório `docs/`.

## 🧠 Algoritmos de Cache Implementados

O sistema inclui quatro algoritmos clássicos de substituição de cache, permitindo uma análise comparativa detalhada de suas estratégias:

-   **FIFO (First-In, First-Out)**: O primeiro texto que entrou no cache é o primeiro a ser removido quando o cache está cheio. É simples, mas nem sempre eficiente.
-   **LRU (Least Recently Used)**: Remove o texto que não foi acessado há mais tempo. Baseia-se na ideia de que textos acessados recentemente têm maior probabilidade de serem acessados novamente.
-   **LFU (Least Frequently Used)**: Remove o texto que foi acessado o menor número de vezes. É útil quando alguns textos são muito mais populares que outros.
-   **MRU (Most Recently Used)**: Remove o texto mais recentemente acessado. Esta abordagem pode ser eficaz em cenários onde o acesso a um item significa que ele não será mais necessário em breve.

## 📂 Estrutura do Projeto

O código-fonte está organizado nos seguintes diretórios:

```
.
├── ra2_main.py                 # Ponto de entrada principal da aplicação
├── requirements.txt            # Dependências do projeto
├── algorithms/                 # Implementação dos algoritmos de cache (FIFO, LRU, LFU, MRU)
├── core/                       # Módulos centrais (gerenciador de cache, interface, etc.)
├── simulation/                 # Lógica para o modo de simulação e geração de relatórios
├── texts/                      # Contém os 100 arquivos de texto usados pelo sistema
└── docs/                       # Armazena os relatórios e gráficos gerados pela simulação
```

## 🚀 Como Começar

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local.

### Pré-requisitos

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### Passos de Instalação

1.  **Clone o repositório:**
    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**
    ```sh
    # Para Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências necessárias:**
    ```sh
    pip install -r requirements.txt
    ```

##  kullanım Como Usar

O programa pode ser executado em dois modos principais: Interativo e Simulação.

### 🖥️ Modo Interativo

Este modo permite que você solicite textos manualmente e veja como o cache responde.

1.  **Execute o arquivo principal:**
    ```sh
    python ra2_main.py
    ```

2.  **Use os seguintes comandos no menu:**
    -   Digite um número de `1` a `100` para solicitar um texto. O sistema informará se foi um *cache hit* (o texto estava no cache) ou um *cache miss* (o texto precisou ser lido do disco).
    -   Digite `-1` para iniciar o Modo de Simulação.
    -   Digite `0` para encerrar o programa.

### ⚙️ Modo de Configuração (-2)

Para ajustar o comportamento do modo interativo, digite `-2` no menu principal. Esta tela permite:

1.  **Alterar o Algoritmo de Cache**: Mude dinamicamente qual algoritmo (FIFO, LRU, LFU ou MRU) será usado para os próximos pedidos de texto no modo interativo.
2.  **Configurar a Simulação de Atraso de Disco**:
    -   **Habilitar/Desabilitar**: Ative ou desative a simulação de um disco lento. Quando ativada, uma pequena pausa é adicionada a cada leitura de texto que resulta em *cache miss*.
    -   **Ajustar Atraso**: Configure os valores mínimo e máximo de atraso (em milissegundos) para simular diferentes velocidades de disco.

### 📊 Modo de Simulação

Este modo executa uma análise completa de todos os algoritmos de cache implementados, gerando relatórios detalhados ao final.

1.  **Inicie o programa** no modo interativo, como descrito acima.
2.  No menu principal, **digite `-1`** e pressione Enter.
3.  Aguarde a conclusão da simulação. O processo pode levar alguns minutos, pois simula milhares de requisições para cada algoritmo.
4.  Ao final, os resultados serão salvos no diretório `docs/`. Você encontrará:
    -   **Relatórios (`.md`)**: Análise detalhada com tabelas de hit rate, tempos de execução e outras métricas.
    -   **Gráficos (`.png`)**: Comparações visuais do desempenho dos algoritmos.

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas Principais**:
  - `matplotlib`: Para a geração dos gráficos de análise.
  - `numpy`: Para cálculos estatísticos e distribuições de acesso (Poisson).

---
Feito com ❤️ para a disciplina de Sistemas Operacionais.