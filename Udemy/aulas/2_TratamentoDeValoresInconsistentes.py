import pandas as pd    #
import numpy as np     # pip intsall seaborn
import seaborn as sns  #
import matplotlib.pyplot as plt # pip install matplotlib
import plotly.express as px     # pip install plotly
base_credit = pd.read_csv('csv\credit_data.csv')

#print(base_credit.loc[base_credit['age'] < 0])
#                  localizada

#print(base_credit[base_credit['age'] < 0])
# faz a mesma coisa que o .loc


# 1ª técnica
# Apagar a coluna inteira
# (de todos os registros da base de dados)

#base_credit2 = base_credit.drop('age',axis= 1)
#                          dropa       1=coluna 0=linha
#print(base_credit2.head(30))


# 2ª técnica
# Apagar as linhas com conteúdo inválido

#base_credit3 = base_credit.drop(base_credit[base_credit#['age'] < 0].index)
#print(base_credit3.head(30))


# 3ª técnica
# Arrumar os dados manualmente, o mais confiável.
# Entrar em contato com o dono dos dados.


# 4ª técnica
# preencher os valores errados com uma média dos outros valores

#print(base_credit.mean())
# trás a media de todos os valores

#print(base_credit['age'].mean())
# trás a média de uma informação mais 
# específica

#print(base_credit['age'][base_credit['age'] > 0].mean())
# média apenas com os valores válidos

base_credit.loc[base_credit['age'] < 0,'age'] = 40.92
#                   condição            local    valor
#print(base_credit.head(30))
grafico = px.scatter_matrix(base_credit, dimensions=['age','income','loan'],color = 'default')
grafico.show()