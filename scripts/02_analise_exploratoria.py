# -*- coding: utf-8 -*-
"""
Script para Análise Exploratória de Dados (AED) de COVID-19 no Brasil.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def carregar_dados_limpos(caminho):
    """Carrega os dados limpos de um arquivo CSV."""
    try:
        df = pd.read_csv(caminho, parse_dates=['data'])
        print("Dados limpos carregados com sucesso.")
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho} não foi encontrado.")
        print("Execute o script '01_ingestao_limpeza.py' primeiro.")
        return None

def analise_estatistica_nacional(df):
    """Calcula e exibe estatísticas descritivas para o Brasil."""
    if df is None: return
    
    # Agrega os dados por data para ter o total do Brasil
    df_nacional = df.groupby('data')[['casos_novos', 'obitos_novos']].sum().reset_index()
    
    print("\n--- Estatísticas Descritivas (Brasil) ---")
    # Usamos o .describe() para obter as medidas de posição e dispersão
    print(df_nacional[['casos_novos', 'obitos_novos']].describe())
    
    return df_nacional

def visualizar_serie_temporal_nacional(df_nacional):
    """Gera e salva o gráfico da série temporal de casos e óbitos."""
    if df_nacional is None: return
    
    print("Gerando gráfico de série temporal nacional...")
    
    # Calcula a média móvel de 7 dias para suavizar a curva
    df_nacional['casos_novos_mm7'] = df_nacional['casos_novos'].rolling(window=7).mean()
    df_nacional['obitos_novos_mm7'] = df_nacional['obitos_novos'].rolling(window=7).mean()

    # Configuração do plot
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax1 = plt.subplots(figsize=(15, 8))

    # Eixo 1: Casos Novos
    color = 'tab:blue'
    ax1.set_xlabel('Data')
    ax1.set_ylabel('Casos Novos', color=color)
    ax1.plot(df_nacional['data'], df_nacional['casos_novos_mm7'], color=color, label='Média Móvel de 7 dias (Casos)')
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(False)

    # Eixo 2: Óbitos Novos
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('Óbitos Novos', color=color)
    ax2.plot(df_nacional['data'], df_nacional['obitos_novos_mm7'], color=color, label='Média Móvel de 7 dias (Óbitos)')
    ax2.tick_params(axis='y', labelcolor=color)
    ax2.grid(False)

    # Título e Legenda
    plt.title('Evolução de Casos e Óbitos de COVID-19 no Brasil (Média Móvel 7 dias)', fontsize=16)
    fig.tight_layout()
    
    # Salvar o gráfico
    caminho_grafico = 'grafico_serie_temporal_nacional.png'
    plt.savefig(caminho_grafico)
    print(f"Gráfico salvo em: {caminho_grafico}")
    plt.close()

def visualizar_casos_por_estado(df):
    """Gera e salva o gráfico de barras do total de casos por estado."""
    if df is None: return

    print("Gerando gráfico de casos acumulados por estado...")
    
    # Calcula o total de casos e óbitos por estado
    df_por_estado = df.groupby('estado')[['casos_novos', 'obitos_novos']].sum().sort_values(by='casos_novos', ascending=False)
    
    plt.figure(figsize=(15, 10))
    sns.barplot(x=df_por_estado['casos_novos'], y=df_por_estado.index, palette='viridis')
    plt.title('Total de Casos de COVID-19 por Estado', fontsize=16)
    plt.xlabel('Número de Casos (em milhões)')
    plt.ylabel('Estado')
    plt.tight_layout()
    
    # Salvar o gráfico
    caminho_grafico = 'grafico_casos_por_estado.png'
    plt.savefig(caminho_grafico)
    print(f"Gráfico salvo em: {caminho_grafico}")
    plt.close()

if __name__ == '__main__':
    # Define o caminho para o arquivo de dados limpos
    caminho_dados = 'data/covid_brasil_limpo.csv'
    
    # Pipeline de execução da análise
    df_covid = carregar_dados_limpos(caminho_dados)
    
    if df_covid is not None:
        # Realiza a análise a nível nacional
        df_nacional = analise_estatistica_nacional(df_covid)
        visualizar_serie_temporal_nacional(df_nacional)
        
        # Realiza a análise por estado
        visualizar_casos_por_estado(df_covid)
