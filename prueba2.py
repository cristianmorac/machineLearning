from propinas.modulos.create_data import create_dataframe
from propinas.modulos.clean_data import limpiar_datos
from propinas.modulos.datos import replace_letra
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
from propinas.modulos.graphics import grafico_apilado

# Datframe
# nombre del archivo
#archivo = 'Propina.xlsx'
archivo = 'Propina'
# Crear dataframe de archivo excel
data = create_dataframe(f'{archivo}.xlsx')
#print(data)

# Formateo de datos

# reemplazar caracteres especiales
data_clean = limpiar_datos(data, replace_letra)
col = []
columns = data_clean['dia'].unique()
for c in columns:
    col.append(c)
col.append('All')
columna = tuple(columns)
st.set_page_config(layout="wide")
# -- Create three columns
col1, col2, col3 = st.columns([5, 5, 20])
with col3:
    st.title("Streamlit Demo")

dia_col, table_col, log_x_col = st.columns([5, 5, 5])
with dia_col:
    mesa_choice = st.slider(
        "Cantidad por mesa?",
        min_value=1,
        max_value=8,
        step=1,
        value=8,
    )
with table_col:
    table_choice = st.selectbox("Opciones",col)

filtered_df = data_clean[(data_clean['mesa_cantidad'].astype(int) == mesa_choice)]

if table_choice != 'All':
    filtered_df = filtered_df[(filtered_df['dia'] == table_choice)]

momento_dia = ['Dinner', 'Lunch', 'momento_dia']
fumadores = ['Yes', 'No','fumadores']

fig = px.bar(
    filtered_df,
    x='genero_pago',
    y="total_factura",
    color="total_factura",
    barmode="group",
)
fig.update_layout(title="Personas por mesa por dia de la semana")
# -- Input the Plotly chart to the Streamlit interface
st.plotly_chart(fig, use_container_width=True)

st.write(grafico_apilado(data_clean,'dia',fumadores))


promedio_dia = data_clean.groupby('dia')['total_factura'].sum().reset_index()
fig = px.pie(promedio_dia, values='total_factura', names='dia', hole=.3)

fig.update_layout(title="Personas por mesa por dia de la semana")
# -- Input the Plotly chart to the Streamlit interface
st.plotly_chart(fig, use_container_width=True)