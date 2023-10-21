# -*- coding: utf-8 -*-
"""Analise Vacinação_Covid_2021 .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OPr0-Ad-HWLfHHnMv1e-aVp6PuTtwnHj
"""

import pandas as pd
import numpy as np

url = "http://dados.recife.pe.gov.br/dataset/perfil-das-pessoas-vacinadas-covid-19/resource/99b42b09-95af-47de-8411-ab99c380c3ef"
df = pd.read_csv("/content/99b42b09-95af-47de-8411-ab99c380c3ef.csv", delimiter =',')

df.head()

df.shape

df.columns

df.query('municipio == "RECIFE"')

df.groupby('municipio')['municipio'].count()

total_pessoas_vacinadas = df['sistema_origem'].value_counts()
print("Total de Pessoas vacinadas Covid no ano 2021: ", total_pessoas_vacinadas)

df.groupby('vacina_fabricante')['municipio'].count()

cid_Sao_Lourenco = df.query('municipio == "SÃO LOURENÇO DA MATA"').copy()

cid_Sao_Lourenco.groupby('vacina_fabricante')['municipio'].count()

coronavac = df.query('vacina_fabricante == "1 - CORONAVAC - SINOVAC (BUTANTAN)"').copy()

coronavac.groupby('municipio')['vacina_fabricante'].count()

vacina = df['vacina_fabricante'].value_counts()
vacina

def determinar_faixa_etaria(idade):
    if 3 <= idade <= 12:
        return 'Crianças'
    elif 13 <= idade <= 19:
        return 'Adolescentes'
    elif 20 <= idade <= 39:
        return 'Jovens adultos'
    elif 40 <= idade <= 59:
        return 'Adultos de meia-idade'
    else:
        return 'Idosos'


df['tipo_faixa_etaria'] = df['idade'].apply(determinar_faixa_etaria)


df.head(5)

def determinar_regiao(municipio):
    cidades_metropolitanas = ['RECIFE', 'JABOATÃO DOS GUARARAPES' , 'OLINDA']

    if municipio in cidades_metropolitanas:
        return 'Metropolitana'
    else:
        return 'Interior'


df['regiao'] = df['municipio'].apply(determinar_regiao)


df.head()





