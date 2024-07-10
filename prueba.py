import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Datos de ejemplo
data = {
    'columna_x': ['A', 'B', 'C', 'D'],
    'columna_y': [10, 20, 15, 25],
    'title': 'Título del Gráfico',
    'xlabel': 'Eje X',
    'ylabel': 'Eje Y'
}

dataframe = pd.DataFrame(data)

# Configuración de los datos del gráfico
datos_grafica_barra = {
    'columna_x': 'columna_x',
    'columna_y': 'columna_y',
    'title': data['title'],
    'xlabel': data['xlabel'],
    'ylabel': data['ylabel']
}

# Creación del gráfico
plt.figure(figsize=(8, 6))
sns.barplot(x=datos_grafica_barra['columna_x'], y=datos_grafica_barra['columna_y'], data=dataframe)
plt.title(datos_grafica_barra['title'])
plt.xlabel(datos_grafica_barra['xlabel'])
plt.ylabel(datos_grafica_barra['ylabel'])

# Mostrar el gráfico en Streamlit
st.pyplot(plt)

# Creación del gráfico
plt.figure(figsize=(8, 6))
sns.barplot(x=datos_grafica_barra['columna_x'], y=datos_grafica_barra['columna_y'], data=dataframe)
plt.title(datos_grafica_barra['title'])
plt.xlabel(datos_grafica_barra['xlabel'])
plt.ylabel(datos_grafica_barra['ylabel'])

# Mostrar el gráfico en Streamlit
st.pyplot(plt)