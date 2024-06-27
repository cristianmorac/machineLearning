"""
script para obtener el listado de los programas 
"""
import requests
import pandas as pd

# URL de la API
url = "https://www.datos.gov.co/resource/pzt8-ws2b.json?$limit=7019"
# Hacer la solicitud GET
response = requests.get(url)

if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    # Imprimir los datos

    df = pd.DataFrame(data)

    list = df['nombre_del_programa'].str.upper().unique()

    print(list)
