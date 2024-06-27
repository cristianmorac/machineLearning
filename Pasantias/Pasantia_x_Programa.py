"""
script que genera una tabla con las pasantias realizadas
y las pasantias que menor se realizan y se cambian algunas
palabras por sus abreviaturas  
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt

# URL de la API
url = "https://www.datos.gov.co/resource/pzt8-ws2b.json?$limit=7019"
# Hacer la solicitud GET
response = requests.get(url)

def abreviaturas(dataframe, column):
    unique_value = dataframe[column]

    list = set()
    for program in unique_value:
        p = program.upper().split()
        if len(p) > 2:
            list.add(p[0])
    
    # crear diccionario de programas
    programas = {}
    for l in list:
        programas[l] = l[0:3]

    dataframe[column] = dataframe[column].str.upper().replace(
        programas, regex=True)
    
    return programas

def descendenteData(dataframe,column):
    # agrupar por genero
    df2 = dataframe.groupby( by= [column]).size().reset_index(name='count')

    # Dataframe de mayor a menor
    def_stored = df2.sort_values(by='count', ascending=False)
    return def_stored

def grafica_circular(datframe):
    
    # crear el grafico circular
    plt.figure(figsize=(8, 8))
    plt.pie(datframe['count'], labels=datframe['nombre_del_programa'], autopct='%1.f%%', startangle=140, colors=plt.cm.Paired.colors)

    plt.title('Pasantias por programas')
    plt.show()

if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    df = pd.DataFrame(data)

    # Dataframe de mayor a menor
    def_stored = descendenteData(df,'nombre_del_programa')
    
    # crear abreviaturas
    dic = abreviaturas(def_stored, 'nombre_del_programa')

    # primeros 10 programas
    grafica_circular(def_stored.head(10))

    # ultimos 10 programas
    #grafica_cirfular(def_stored.tail(10))
