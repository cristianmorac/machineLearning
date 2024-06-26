import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# URL de la API
url = "https://www.datos.gov.co/resource/pzt8-ws2b.json?$limit=7019"
# Hacer la solicitud GET
response = requests.get(url)

def grafica_barra(dataframe, programa):
        # crear grafico de barras
        plt.figure(figsize=(8, 6))
        sns.barplot(x='genero', y='count', data=dataframe)
        plt.title(programa)
        plt.xlabel('Pasantes por genero')
        plt.ylabel('Cantidad')
        plt.show()

def categoria_programa(dataframe, programa, lista_programa):
        
        # filtrar por nombre del programa
        programas = dataframe[dataframe['nombre_del_programa'] == programa]
        # agrupar por genero
        df2 = programas.groupby( by= ['nombre_del_programa','genero']).size().reset_index(name='count')
        grafica_barra(df2,programa)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    # Imprimir los datos

    df = pd.DataFrame(data)
    lista_programa = df['nombre_del_programa'].unique()
    print(lista_programa)

    # Generar grafica por programa
    categoria_programa(df,'LIC. MATEMATICAS', lista_programa)