from modulos import create_data as cd
from modulos.clean_data import limpiar_datos
from modulos.datos import replace_letra, datos_grafica_barra
from modulos.statistic_data import Descriptiva
from modulos.graphics import grafica_barra
import numpy as np

# importaciones grafica
import seaborn as sns
import matplotlib.pyplot as plt


# nombre del archivo
archivo = 'Propina.xlsx'

# Crear dataframe de archivo excel
data = cd.create_dataframe(archivo)
#print(data)

# Formateo de datos

# obtener todas las columnas
columnas = data.columns.to_list()

# reemplazar caracteres especiales
data_clean = limpiar_datos(data,columnas, replace_letra)
#print(data_clean)

# Estadistica descriptiva
database = Descriptiva(data_clean,'mesa_cantidad')
#print(data)

# Cantidad de personas por dia

# agrupar fumadores y no por dia de la semana
data2 = data.groupby(['dia','fumadores']).size().reset_index(name='count')
# valores del grafico de barras
x = data2['dia'].unique()
y3 = data2['count'][data2['fumadores']== 'Yes']
y4 = data2['count'][data2['fumadores']== 'No']

# Crear grafica
plt.bar(x,y3, color='r')
plt.bar(x,y4, bottom=y3, color='b')
plt.legend(["Yes","No"])
plt.show()