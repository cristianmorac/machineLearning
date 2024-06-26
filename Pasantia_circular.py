import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# URL de la API
url = "https://www.datos.gov.co/resource/pzt8-ws2b.json?$limit=7019"
# Hacer la solicitud GET
response = requests.get(url)


def grafica_cirfular(datframe):
    
    #print(def_sorted)
    # crear el grafico circular
    plt.figure(figsize=(8, 8))
    plt.pie(datframe['count'], labels=datframe['nombre_del_programa'], autopct='%1.f%%', startangle=140, colors=plt.cm.Paired.colors)

    plt.title('Pasantias por programas')
    plt.show()

if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    df = pd.DataFrame(data)

    # agrupar por genero
    df2 = df.groupby( by= ['nombre_del_programa']).size().reset_index(name='count')

    # De mayor a menor
    def_stored = df2.sort_values(by='count', ascending=False)

    unique_value = def_stored['nombre_del_programa'].unique()

    programa = {unique_value[0]: unique_value[0][0:3]}
    #print(programa)

    # convertir todo a mayuscula y remplazar por su abreviatura
    """ def_stored['nombre_del_programa'] = def_stored['nombre_del_programa'].str.upper().replace({
        'LICENCIATURA': 'LIC',
        'INGENIERIA': 'ING',
        'ESPECIALIZACION': 'ESP',
        'TECNOLOGIA': 'TCG',
        'ADMINISTRACION': 'ADMN',
        'ENFERMERÍA': 'ENF',
        'DOCTORADO': 'DOC'

    }, regex=True) """

    # primeros 10 programas
    grafica_cirfular(def_stored.head(10))

    # ultimos 10 programas
    #grafica_cirfular(def_stored.tail(10))
