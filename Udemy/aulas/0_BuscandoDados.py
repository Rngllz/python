import pandas as pd    #
import numpy as np     # pip intsall seaborn
import seaborn as sns  #
import matplotlib.pyplot as plt # pip install matplotlib
import plotly.express as px     # pip install plotly
base_credit = pd.read_csv('csv\credit_data.csv')

print(base_credit)

print(base_credit.head(10))  
# Mostra os 10 primeiros

print(base_credit.tail(10))  
# Mostra os 10 últimos

print(base_credit.describe()) 
# Trás diversas informações como a média, max, min, etc, dos valores

print(base_credit[base_credit['age'] > 21]) 
# Consigo fazer buscas mais específicas
