import requests
import pandas as pd

# URL de la API
url = "https://www.datos.gov.co/resource/pzt8-ws2b.json?$limit=7019"
# Hacer la solicitud GET
response = requests.get(url)

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
    
        print(dfmujer.sort_values(by='count', ascending=False))
        print(dfhombre.sort_values(by='count', ascending=False))

    validar_programa_mayor_genero(df,list_programas)
