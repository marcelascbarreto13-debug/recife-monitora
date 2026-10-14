# Recife Monitora - Análise de Dados

Projeto desenvolvido na disciplina de **Projetos 5**, do curso de **Gestão de Tecnologia da Informação da CESAR School**.

## Sobre o projeto

O projeto tem como objetivo realizar o entendimento, preparação, tratamento, análise exploratória e visualização de dados relacionados ao programa **Recife Monitora**.
O trabalho busca estruturar um processo de análise de dados reproduzível, permitindo analisar a participação e o desempenho das equipes ao longo dos ciclos, além de explorar indicadores, NPS e planos de ação.

> **Importante:** os dados utilizados nesta etapa são **sintéticos**, desenvolvidos exclusivamente para fins acadêmicos, e não representam resultados reais das equipes ou da Secretaria de Saúde do Recife.

## Estrutura do projeto

```text
recife-monitora/
│
├── dados/                  # Bases originais
├── dados_tratados/         # Bases após tratamento
├── notebooks/
│   ├── 01_entendimento_dados.ipynb
│   ├── 02_preparacao_dados.ipynb
│   └── 03_analise_exploratoria.ipynb
│
├── src/
│   ├── carregar_dados.py
│   └── tratamento.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Etapas desenvolvidas

### 1. Entendimento dos dados

Perfilamento inicial das cinco bases, incluindo análise de:

- dimensões e tipos das variáveis;
- valores ausentes;
- duplicidades;
- cardinalidade e consistência das chaves;
- formatos dos ciclos;
- limites esperados das variáveis;
- relacionamento entre as bases.

### 2. Preparação e tratamento

Foram realizadas etapas de:

- padronização de identificadores e categorias;
- padronização dos ciclos;
- conversão de variáveis numéricas;
- tratamento de duplicidades;
- identificação e tratamento de valores inválidos;
- tratamento de valores ausentes conforme as regras de negócio;
- validação das pontuações e classificações;
- validação da integridade entre as bases.

As principais regras de tratamento também foram implementadas em funções reutilizáveis na pasta `src/`.

### 3. Análise exploratória

A análise exploratória contempla:

- evolução da participação das equipes;
- evolução das pontuações ao longo dos ciclos;
- comparação dos três eixos de avaliação;
- análise por distrito sanitário e unidade;
- indicadores do Eixo 3;
- relação entre população adscrita e desempenho;
- análise dos atributos de NPS;
- análise dos planos de ação;
- qualidade dos dados;
- visualizações estáticas e interativas.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/marcelascbarreto13-debug/recife-monitora.git
cd recife-monitora
```

### 2. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o pipeline de tratamento

```bash
python src/tratamento.py
```

As bases originais são lidas da pasta `dados/` e os arquivos processados são gerados em `dados_tratados/`.

### 5. Explorar as análises

Os notebooks estão organizados na pasta `notebooks/`:

```text
01_entendimento_dados.ipynb
02_preparacao_dados.ipynb
03_analise_exploratoria.ipynb
```

O fluxo principal do projeto é:

```text
dados/
   ↓
carregamento
   ↓
tratamento
   ↓
dados_tratados/
   ↓
análise exploratória
   ↓
visualizações e conclusões
```

## Reprodutibilidade

A leitura, o tratamento e a análise foram organizados de forma separada.
O módulo `carregar_dados.py` centraliza a leitura das bases e o `tratamento.py` contém as funções de preparação, limpeza e validação.
Assim, o tratamento pode ser executado novamente a partir dos dados originais, permitindo reproduzir as bases utilizadas nas análises.
A estrutura também facilita a futura substituição dos dados sintéticos por dados reais.

## Tecnologias utilizadas

Python, Pandas, NumPy, Matplotlib, Seaborn, Plotly, Jupyter Notebook, VS Code, Git e GitHub.

## Limitações

A participação das equipes deve ser considerada na interpretação dos resultados, pois a ausência de uma equipe em determinado ciclo não representa necessariamente baixo desempenho.
Valores ausentes foram preservados quando não havia justificativa metodológica para sua substituição.
Como a base atual é **sintética**, os resultados apresentados servem para validar a metodologia e o pipeline desenvolvido, não representando o desempenho real das equipes de saúde do Recife.