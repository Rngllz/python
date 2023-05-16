import pandas as pd    #
import numpy as np     # pip intsall seaborn
import seaborn as sns  #
import matplotlib.pyplot as plt # pip install matplotlib
import plotly.express as px     # pip install plotly
base_credit = pd.read_csv('csv\credit_data.csv')

#print(np.unique(base_credit['default'], return_counts=True))
#               Trás todos os formatos       Aqui conseguimos ver
#               desse tipo de informação.    quanto de casa informação
#               No caso: 0 e 1               temos: 1717 e 283


#sns.countplot(x = base_credit['default']) 
# Faz o gráfico de acordo com as informações escolhidas
#plt.show()
# Abre uma tela com o gráfico

#plt.hist(x = base_credit['age'])
# Gráfico de intervalos 
#plt.show()

#plt.hist(x = base_credit['income'])
#plt.show()

#plt.hist(x = base_credit['loan'])
#plt.show()

grafico = px.scatter_matrix(base_credit, dimensions=['age'])
grafico.show()