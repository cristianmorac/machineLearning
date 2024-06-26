import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# URL de la API
url = "https://www.datos.gov.co/resource/pzt8-ws2b.json?$limit=7019"

# Hacer la solicitud GET
response = requests.get(url)
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    # Imprimir los datos

    df = pd.DataFrame(data)

    # agrupar por genero
    df2 = df.groupby( by= ['nombre_del_programa']).size().reset_index(name='count')
    # De maroy a menor
    def_sorted = df2.sort_values(by='count', ascending=False).head(10)
    #print(def_sorted)
    # crear el grafico circular
    plt.figure(figsize=(8, 8))
    plt.pie(def_sorted['count'], labels=def_sorted['nombre_del_programa'], autopct='%1.f%%', startangle=140, colors=plt.cm.Paired.colors)

    plt.title('Pasantias por programas')
    plt.show()