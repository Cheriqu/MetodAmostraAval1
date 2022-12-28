import numpy as np
import pandas as pd
import statistics as st
import matplotlib.pyplot as plt
import warnings
from itertools import product, combinations
warnings.simplefilter(action='ignore', category=FutureWarning)

plt.style.use('ggplot')

anos = [21,18,20,21,30,25,11,21,18,29,12,22,25,10,29,23,15,16,18,28]

media = st.mean(anos)
var = round(st.variance(anos),2)

print('Media:', media, '\t Variancia:', var)

i1 , i2, i3, i4, i5, i6, i7, i8, i9, i10 = range(10,12,1), range(12,14,1), range(14,16,1), range(16,18,1), range(18,20,1), \
                                      range(20,22,1), range(22,24,1), range(24,26,1), range(26,28,1), range(28, max(anos), 1)
l1,l2,l3,l4,l5,l6,l7,l8,l9,l10 = ([] for i in range(10))
for i in range(0,len(anos)):
    if anos[i] in i1:
        l1.append(anos[i])
    elif anos[i] in i2:
        l2.append(anos[i])
    elif anos[i] in i3:
        l3.append(anos[i])
    elif anos[i] in i4:
        l4.append(anos[i])
    elif anos[i] in i5:
        l5.append(anos[i])
    elif anos[i] in i6:
        l6.append(anos[i])
    elif anos[i] in i7:
        l7.append(anos[i])
    elif anos[i] in i8:
        l8.append(anos[i])
    elif anos[i] in i9:
        l9.append(anos[i])
    elif anos[i] in i10:
        l10.append(anos[i])

A = pd.DataFrame(list([[l1],[l2],[l3],[l4],[l5],[l6],[l7],[l8],[l9],[l10]]))
lista = []
for i in range(0,A.shape[0]):
    lis = A.iloc[i].to_string()
    lis = lis[6:-1]
    lis = lis.replace(",","")
    lis = lis.replace(" ", "")
    lista.append(int(len(lis)/2))
A['f'] = lista
A['%'] = A['f']/20*100
A.set_axis(['Valores','f','%'], axis='columns', inplace=True)
A.set_axis(['10 |-- 12','12 |-- 14','14 |-- 16','16 |-- 18','18 |-- 20','20 |-- 22','22 |-- 24',
            '24 |-- 26','26 |-- 28','28 ou mais'], axis='rows', inplace=True)
print(A)

n=2
df = pd.DataFrame()
df['Amostra'] = list(combinations(anos, n))
df['Média'] = np.mean(list(combinations(anos, n)), axis=1)
df['Variância'] = np.var(list(combinations(anos, n)), axis=1)
fator_correcao = np.sqrt((190-2)/190)
df['Erro Padrão'] = fator_correcao * (np.sqrt(df['Variância']/2))
df['Int. Inf.'] = df['Média'] - df['Erro Padrão']
df['Int. Sup.'] = df['Média'] + df['Erro Padrão']

num_amostras = len(list(combinations(anos, n)))
media_medias = round(df['Média'].mean(),2)
medias_variancias = round(df['Variância'].mean(),2)
menor_media = round(min(df['Média']),2)
maior_media = round(max(df['Média']),2)
amplitude = round(max(df['Média']) - min(df['Média']),2)
percent_media_pop = round(df[(df['Int. Inf.'] < media) & (df['Int. Sup.'] > media)]['Amostra'].count() / num_amostras *100,2)

print("\nn:", n,"\nNúmero de amostras selecionadas:",num_amostras,"\nMédia das médias:",media_medias,"\nMédia das variâncias:",
      medias_variancias,"\nMenor média:",menor_media,"\nMaior média:",maior_media,"\nAmplitude:",amplitude,
      "\nPercentual de intervalos que contém a média populacional:", percent_media_pop)

n=3
df = pd.DataFrame()
df['Amostra'] = list(combinations(anos, n))
df['Média'] = np.mean(list(combinations(anos, n)), axis=1)
df['Variância'] = np.var(list(combinations(anos, n)), axis=1)
fator_correcao = np.sqrt((190-2)/190)
df['Erro Padrão'] = fator_correcao * (np.sqrt(df['Variância']/2))
df['Int. Inf.'] = df['Média'] - df['Erro Padrão']
df['Int. Sup.'] = df['Média'] + df['Erro Padrão']

num_amostras = len(list(combinations(anos, n)))
media_medias = round(df['Média'].mean(),2)
medias_variancias = round(df['Variância'].mean(),2)
menor_media = round(min(df['Média']),2)
maior_media = round(max(df['Média']),2)
amplitude = round(max(df['Média']) - min(df['Média']),2)
percent_media_pop = round(df[(df['Int. Inf.'] < media) & (df['Int. Sup.'] > media)]['Amostra'].count() / num_amostras *100,2)

print("\nn:", n,"\nNúmero de amostras selecionadas:",num_amostras,"\nMédia das médias:",media_medias,"\nMédia das variâncias:",
      medias_variancias,"\nMenor média:",menor_media,"\nMaior média:",maior_media,"\nAmplitude:",amplitude,
      "\nPercentual de intervalos que contém a média populacional:", percent_media_pop)


n=4
df = pd.DataFrame()
df['Amostra'] = list(combinations(anos, n))
df['Média'] = np.mean(list(combinations(anos, n)), axis=1)
df['Variância'] = np.var(list(combinations(anos, n)), axis=1)
fator_correcao = np.sqrt((190-2)/190)
df['Erro Padrão'] = fator_correcao * (np.sqrt(df['Variância']/2))
df['Int. Inf.'] = df['Média'] - df['Erro Padrão']
df['Int. Sup.'] = df['Média'] + df['Erro Padrão']

num_amostras = len(list(combinations(anos, n)))
media_medias = round(df['Média'].mean(),2)
medias_variancias = round(df['Variância'].mean(),2)
menor_media = round(min(df['Média']),2)
maior_media = round(max(df['Média']),2)
amplitude = round(max(df['Média']) - min(df['Média']),2)
percent_media_pop = round(df[(df['Int. Inf.'] < media) & (df['Int. Sup.'] > media)]['Amostra'].count() / num_amostras *100,2)

print("\nn:", n,"\nNúmero de amostras selecionadas:",num_amostras,"\nMédia das médias:",media_medias,"\nMédia das variâncias:",
      medias_variancias,"\nMenor média:",menor_media,"\nMaior média:",maior_media,"\nAmplitude:",amplitude,
      "\nPercentual de intervalos que contém a média populacional:", percent_media_pop)