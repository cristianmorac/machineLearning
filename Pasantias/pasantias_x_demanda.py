import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# URL de la API
url = "https://www.datos.gov.co/resource/pzt8-ws2b.json?$limit=7019"
# Hacer la solicitud GET
response = requests.get(url)

def grafica_barra(dataframe):
        # crear grafico de barras
        plt.figure(figsize=(8, 6))
        sns.barplot(x='count', y='nombre_del_programa', data=dataframe)
        plt.title("Programas con mayor cantidad de pasantes")
        plt.xlabel('Pasantes por genero')
        plt.ylabel('Cantidad')
        plt.show()


# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    # Imprimir los datos

    df = pd.DataFrame(data)
    df2 = df.groupby( by= ['nombre_del_programa']).size().reset_index(name='count').sort_values(by='count', ascending=False)
    print(df2[['nombre_del_programa','count']].head(10))

    grafica_barra(df2[['nombre_del_programa','count']].head(10))


    