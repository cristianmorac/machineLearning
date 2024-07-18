from modulos.create_data import create_dataframe
from modulos.clean_data import limpiar_datos, filas_Sin_datos
from modulos.datos import replace_letra, type_column


#Estadstica
from modulos.static_data import Descriptiva
import pandas as pd

# mostrar en la web
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt

# regresion lineal
from sklearn.model_selection import train_test_split
from modulos.static_data import no_supervisado, Descriptiva

# KMeans
from sklearn.cluster import KMeans
import numpy as np

st.set_page_config(layout="wide")
st.title("Machine learning")
database_col, prueba = st.columns([20,20])
with database_col:
    data_choice = st.selectbox("Data a validar",('Propina', 'Prueba_saber'))
col1, col2 = st.columns([20,20])
with col1:
    st.title('Sin limpieza de datos')
    data = create_dataframe(f'{data_choice}.xlsx')
    st.write(data.head(3))
    
with col2:
    st.title('limpieza de datos')
    # obtener todas las columnas
    columnas = data.columns.to_list()
    limpiar_datos(data,replace_letra)
    filas_Sin_datos(data,'Sin datos',columnas)
    # elminar datos nulos
    data = data.dropna()    
    st.write(data.head(3))

st.title("Estadistica descriptiva")
valores_col = type_column(data,columnas)
decriptiva_col= st.selectbox("Consulta",(valores_col))

# Estadisica descriptiva
descriptiva = Descriptiva(data,decriptiva_col)
df_descriptiva = pd.DataFrame([descriptiva])
st.write(df_descriptiva)

st.title("Grafico Apilado")
valorx_col, valory_col, valorz_col = st.columns([10,10, 10])
with valorx_col:
    valorx_choice = st.selectbox("Valor en x",(columnas))
with valory_col:
    columnas2 = columnas
    columnas2.remove(valorx_choice)
    valory_choice = st.selectbox("Valor en y",(columnas))
with valorz_col:
    valorz_choice = st.selectbox("Valor en z",([valorx_choice,valory_choice,'COUNT']))

data2 = data.groupby([valorx_choice, valory_choice]).size().reset_index(name='COUNT')
fig = px.bar(data2.head(520),x=valorx_choice,y=valory_choice, color=valorz_choice, text_auto=True)
fig.update_layout(title=f"{valorx_choice} vs. {valory_choice}")
# -- Input the Plotly chart to the Streamlit interface
st.plotly_chart(fig, use_container_width=True)

st.title("Grafico Pastel")

fg2 = px.pie(data2.head(520),names=valorx_choice, values=valory_choice, color=valorz_choice)
fg2.update_layout(title=f"{valorx_choice} vs. {valory_choice}")
# -- Input the Plotly chart to the Streamlit interface
st.plotly_chart(fg2, use_container_width=True)

st.title("Regresión lineal No supervisado")
valx_col, valy_col= st.columns([10,10])

x_col, y_col = st.columns([10,10])
with x_col:
    valorx_choice = st.selectbox("Valor en x",(valores_col))
with y_col:
    columnas3 = valores_col
    columnas3.remove(valorx_choice)
    valory_choice = st.selectbox("Valor en y",(columnas3))

fig3 = px.scatter(data,x=data[valorx_choice],y=data[valory_choice],trendline="ols",color=valorx_choice)
fig3.update_layout(title=f"{valorx_choice} vs. {valory_choice}")
# -- Input the Plotly chart to the Streamlit interface
st.plotly_chart(fig3, use_container_width=True)


# KMeans
""" col_x = 'mesa_cantidad'
col_y = 'total_factura' """
col_x = valorx_choice
col_y = valory_choice

st.title('Kmeans')
datosKemans = data[[valorx_choice, valory_choice]]
kmeans = KMeans(n_clusters=2)
kmeans.fit(datosKemans)
etiquetas = kmeans.labels_
data_group = data.groupby([col_x, col_y]).size().reset_index(name='count')
result = data_group.groupby(col_x).sum().reset_index()
datosKemans2 = result[['count', col_x]]
datosKemans3 = np.array(datosKemans2)

# Aplicar K-means
kmeans = KMeans(n_clusters=2)
kmeans.fit(datosKemans2)
etiquetas = kmeans.labels_

# Mostrar clientes por cluster
cluster0 = {}
for i, mesa in enumerate(datosKemans3[etiquetas == 0]):
    cluster0[f'Valores {i+1}'] = {
        f'frecuencia de {valory_choice}' : mesa[0],
        f'{valorx_choice}': mesa[1]
    }

cluster1 = {}
for i, mesa in enumerate(datosKemans3[etiquetas == 1]):
    cluster1[f'Valores {i+1}'] = {
        f'frecuencia de {valory_choice}' : mesa[0],
        f'{valorx_choice}': mesa[1]
    }

st.title('Clusster 0')
df_cluster0 = pd.DataFrame(cluster0)
st.write(df_cluster0)
st.title('Clusster 1')
df_cluster1 = pd.DataFrame(cluster1)
st.write(df_cluster1)

# Colores para los clusters
colores = ['blue', 'green']

# Visualización de los clusters
plt.figure(figsize=(8, 6))
for etiqueta, color in zip(np.unique(etiquetas), colores):
    puntos = datosKemans3[etiquetas == etiqueta]
    plt.scatter(puntos[:, 0], puntos[:, 1], color=color, label=f'Cluster {etiqueta}')

plt.xlabel(f'{col_y}')
plt.ylabel(f'{col_x}')
plt.title('Clustering de datos con K-means')
plt.legend()
st.pyplot(plt)