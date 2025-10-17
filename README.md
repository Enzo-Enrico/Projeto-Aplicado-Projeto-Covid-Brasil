# Projeto Aplicado I: Análise Exploratória de Dados da COVID-19 no Brasil

Este repositório contém os materiais referentes ao Projeto Aplicado I do curso de [Seu Curso]. O objetivo é realizar uma análise exploratória dos dados de casos e óbitos da COVID-19 no Brasil, utilizando dados abertos do Ministério da Saúde.

## 🎯 Objetivo

O projeto visa aplicar técnicas de análise de dados para extrair insights e sumarizar as principais características da pandemia de COVID-19 no Brasil. As principais questões de pesquisa estão focadas na evolução temporal, distribuição geográfica e características estatísticas dos dados.

## 📁 Estrutura do Repositório

* **/data:** Pasta destinada ao armazenamento do conjunto de dados original e processado.
* **/scripts:** Contém os scripts Python utilizados para a análise.
    * `01_ingestao_limpeza.py`: Script para baixar, carregar e limpar os dados.
    * `02_analise_exploratoria.py`: Script que realiza a análise exploratória e gera as visualizações.
* `README.md`: Este arquivo.
* `requirements.txt`: Lista de dependências Python para executar o projeto.

## 🚀 Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone [https://www.youtube.com/watch?v=6YQIWRyPxnk](https://www.youtube.com/watch?v=6YQIWRyPxnk)
    cd projeto-aplicado-covid
    ```

2.  **Crie um ambiente virtual e instale as dependências:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3.  **Execute os scripts:**
    Execute os scripts na ordem numérica para garantir que os dados sejam processados corretamente.
    ```bash
    python scripts/01_ingestao_limpeza.py
    python scripts/02_analise_exploratoria.py
    ```
    Os gráficos gerados pela análise serão salvos na pasta raiz do projeto.

## 📊 Fonte dos Dados

Os dados utilizados são públicos e foram obtidos através da plataforma OpenDataSUS do Ministério da Saúde do Brasil.

**Autor:** Enzo Enrico Braga Cavalcante
