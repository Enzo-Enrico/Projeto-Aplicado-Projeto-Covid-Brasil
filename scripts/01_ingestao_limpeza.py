# -*- coding: utf-8 -*-
"""
Script para ingestão e limpeza dos dados de COVID-19 do Ministério da Saúde.
"""

import pandas as pd
import os

def baixar_e_carregar_dados():
    """
    Baixa o arquivo de dados históricos de COVID-19 do Brasil e o carrega em um DataFrame.
    
    Returns:
        pd.DataFrame: DataFrame com os dados brutos.
    """
    print("Iniciando o download dos dados...")
    # URL do dataset histórico de COVID-19 (pode precisar ser atualizada)
    url = 'https://covid.saude.gov.br/dados/HIST_PAINEL_COVIDBR.csv'
    
    # Parâmetros para a leitura do CSV
    # O arquivo usa ';' como separador e ',' como separador decimal
    try:
        df = pd.read_csv(url, sep=';', parse_dates=['data'], decimal=',')
        print("Download e carregamento concluídos.")
        return df
    except Exception as e:
        print(f"Erro ao baixar ou carregar os dados: {e}")
        return None

def limpar_dados(df):
    """
    Realiza a limpeza e pré-processamento básico do DataFrame.
    
    Args:
        df (pd.DataFrame): DataFrame com os dados brutos.
        
    Returns:
        pd.DataFrame: DataFrame com os dados limpos e filtrados para o escopo Brasil.
    """
    if df is None:
        return None
        
    print("Iniciando a limpeza dos dados...")
    
    # 1. Filtrar apenas os dados consolidados do Brasil (município em branco)
    # Para uma análise mais detalhada, poderíamos remover este filtro.
    # Neste caso, vamos focar nos dados por estado.
    df_brasil = df[df['regiao'] != 'Brasil'].copy()
    
    # 2. Renomear colunas para facilitar o uso (opcional)
    df_brasil.rename(columns={'casosNovos': 'casos_novos', 'obitosNovos': 'obitos_novos'}, inplace=True)

    # 3. Converter a coluna 'data' para o formato datetime
    # O parâmetro parse_dates no read_csv já tenta fazer isso, mas vamos garantir.
    df_brasil['data'] = pd.to_datetime(df_brasil['data'])

    # 4. Selecionar colunas de interesse para a análise
    colunas_interesse = [
        'data', 'estado', 'casos_novos', 'obitos_novos', 
        'casosAcumulado', 'obitosAcumulado'
    ]
    df_limpo = df_brasil[colunas_interesse]

    # 5. Ordenar os dados por estado e data
    df_limpo = df_limpo.sort_values(by=['estado', 'data']).reset_index(drop=True)
    
    print("Limpeza concluída.")
    return df_limpo

def salvar_dados(df, caminho):
    """
    Salva o DataFrame limpo em um arquivo CSV.
    
    Args:
        df (pd.DataFrame): DataFrame limpo.
        caminho (str): Caminho para salvar o arquivo.
    """
    if df is not None:
        # Garante que o diretório 'data' exista
        os.makedirs(os.path.dirname(caminho), exist_ok=True)
        df.to_csv(caminho, index=False)
        print(f"Dados limpos salvos em: {caminho}")

if __name__ == '__main__':
    # Define o caminho para o arquivo de dados limpos
    caminho_dados_limpos = 'data/covid_brasil_limpo.csv'
    
    # Pipeline de execução
    dados_brutos = baixar_e_carregar_dados()
    dados_limpos = limpar_dados(dados_brutos)
    salvar_dados(dados_limpos, caminho_dados_limpos)
