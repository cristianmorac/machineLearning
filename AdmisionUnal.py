import requests
import pandas as pd

# URL de la API
url = "https://www.datos.gov.co/resource/mqpd-2jhs.json?$limit=5000"

# Hacer la solicitud GET
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    # Imprimir los datos

    df = pd.DataFrame(data)
    a = df[(df['sexo']=='Mujeres') & (df['admitido'] == 'No')]
    b = df[(df['sexo']=='Hombres') & (df['admitido'] == 'No')]
    c = df[df['admitido'] == 'No']
    # mostrar estas columnas
    #print(b[['nivel','year','admitido', 'dep_nac']])
    # agrupar y contar la cantidad de veces que se repite

    # agrupar .reset_index(name='count' -> funciona para darle nombre a la columna
    print(a.groupby( by= ['nivel','dep_nac', 'admitido']).size().reset_index(name='count'))
    print(b.groupby( by= ['nivel','dep_nac', 'admitido']).size().reset_index(name='count'))
    print(c.groupby( by= ['nivel','dep_nac', 'admitido']).size().reset_index(name='count'))


else:
    print(f"Error: {response.status_code}")