from modulos.graphics import grafico_apilado
from modulos.static_data import no_supervisado, supervisado
import modulos.create_data as cd
from modulos.clean_data import limpiar_datos
from modulos.datos import replace_letra

import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# nombre del archivo
archivo = 'Propina.xlsx'

# Crear dataframe de archivo excel
data = cd.create_dataframe(archivo)

# Formateo de datos
# reemplazar caracteres especiales
data_clean = limpiar_datos(data, replace_letra)

st.title('Grafico Aplanado')
# graficos Apilado
momento_dia = ['Dinner', 'Lunch', 'momento_dia']
fumadores = ['Yes', 'No','fumadores']

# crear grafico
grafico_apilado(data_clean,'dia',fumadores)

st.title('Regresión lineal')
# Regresión lineal
no_supervisado(data_clean,'total_factura','Propina') # funciona mejor

promedio_dia = data_clean.groupby('dia')['total_factura'].sum().reset_index()
explode = (0,0,0,0.1)

st.title('Gráfico de pastel')
#Gráfico de pastel
plt.figure(figsize=(8, 8))  # Tamaño de la figura
plt.pie(promedio_dia['total_factura'], labels=promedio_dia['dia'], autopct='%1.1f%%', explode=explode)
plt.title('Venta por dia')
st.pyplot(plt)



