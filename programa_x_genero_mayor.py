import requests
import pandas as pd
import matplotlib.pyplot as plt

""" 
Script para conocer que programa tiene mayor oferta
si es por hombres o mujeres
"""

# URL de la API
url = "https://www.datos.gov.co/resource/pzt8-ws2b.json?$limit=7019"
# Hacer la solicitud GET
response = requests.get(url)

def grafica_circular(datframe, genero):
    
    # crear el grafico circular
    plt.figure(figsize=(8, 8))
    plt.pie(datframe['count'], labels=datframe['nombre_del_programa'], autopct='%1.f%%', startangle=140, colors=plt.cm.Paired.colors)

    plt.title(f'Pasantias por genero {genero}')
    plt.show()

if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    df = pd.DataFrame(data)

    list_programas = df['nombre_del_programa'].unique()
    #print(list_programas)

    def validar_programa_mayor_genero(df2, list_programas):

        df2 = df.groupby( by= ['nombre_del_programa','genero']).size().reset_index(name='count')

        dfmujer = pd.DataFrame()
        dfhombre = pd.DataFrame()

        for programa in list_programas:
            femenino = df2[(df2['nombre_del_programa']== programa) & (df2['genero'] == 'FEMENINO')]
            masculino = df2[(df2['nombre_del_programa']== programa) & (df2['genero'] == 'MASCULINO')]

            count_masculino = masculino['count'].values
            count_femenino = femenino['count'].values
    
            if count_masculino < count_femenino:
                dfmujer = dfmujer._append(femenino, ignore_index=True)
            else:
                dfhombre = dfhombre._append(masculino, ignore_index=True)
    
        dfmujer = dfmujer.sort_values(by='count', ascending=False)
        dfhombre = dfhombre.sort_values(by='count', ascending=False)

        grafica_circular(dfmujer.head(10), 'Femenino')
        grafica_circular(dfhombre.head(10), 'Masculino')

    validar_programa_mayor_genero(df,list_programas)
