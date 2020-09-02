# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:12:32 2020

@author: fabio
"""
import pandas as pd
import psycopg2 as pg
import numpy as np
from datetime import datetime
from datetime import date
from matplotlib import pyplot as plt
import seaborn as sns

# ler o dataset e criar o dataframe
boletim_full = pd.read_csv('caso_full.csv')


data_Boletim = boletim_full[(boletim_full.city_ibge_code>99)]
data_Boletim = data_Boletim.astype({"city_ibge_code": int,"new_confirmed": int})
data_Boletim['date'] = pd.to_datetime(data_Boletim['date'], yearfirst = True)
data_Boletim['last_available_date'] = pd.to_datetime(data_Boletim['last_available_date'], yearfirst = True)


cidades = {'Cascavel':'PR','Toledo':'PR','Foz do Iguaçu':'PR','Marechal Cândido Rondon':'PR','Medianeira':'PR'}
data_Boletim = data_Boletim[data_Boletim.city.isin(cidades.keys()) & data_Boletim.state.isin(cidades.values())]

cidade1 = data_Boletim[data_Boletim.city.eq('Medianeira')] 
cidade2 = data_Boletim[data_Boletim.city.eq('Marechal Cândido Rondon')] 
cidade3 = data_Boletim[data_Boletim.city.eq('Foz do Iguaçu')] 
cidade4 = data_Boletim[data_Boletim.city.eq('Cascavel')] 
cidade5 = data_Boletim[data_Boletim.city.eq('Toledo')] 

fig = plt.figure(figsize=(16,8))
ax1 = plt.subplot(111)
ax1.plot(cidade1['last_available_date'],cidade1['last_available_confirmed'],label='Medianeira',color='blue')
ax1.plot(cidade2['last_available_date'],cidade2['last_available_confirmed'],label='Marechal',color='orange')
ax1.plot(cidade3['last_available_date'],cidade3['last_available_confirmed'],label='Foz do Iguaçu',color='green')
ax1.plot(cidade4['last_available_date'],cidade4['last_available_confirmed'],label='Cascavel',color='red')
ax1.plot(cidade5['last_available_date'],cidade5['last_available_confirmed'],label='Toledo',color='purple')

ax1.legend()

plt.title('Total de casos confirmados por dia. Fonte:https://brasil.io/dataset/covid19/boletim/',fontsize=16,color="black",alpha=2)
plt.xlabel('Mês em 2020',size = 14,color="black")
plt.ylabel('Acumulado de casos confirmados',size = 14,color="black")
plt.grid()
plt.show