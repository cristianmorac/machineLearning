import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# URL de la API
url = "https://www.datos.gov.co/resource/pzt8-ws2b.json?$limit=7019"

# Hacer la solicitud GET
response = requests.get(url)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    # Obtener los datos en formato JSON
    data = response.json()
    # Imprimir los datos

    df = pd.DataFrame(data)
    print(df)
    # filtrar por Admin de negocios
    admin_negocios = df[df['nombre_del_programa'] == 'MEDICINA']
    #print(admin_negocios)

    # agrupar por genero
    df2 = df.groupby( by= ['nombre_del_programa','genero']).size().reset_index(name='count')
    #rint(df2)

    # filtrar por programa y femenino
    femenino = df2[(df2['genero']=='FEMENINO')]
    masculino = df2[(df2['genero']=='MASCULINO')]
    #print(femenino)

    # Configuración para mostrar gráficos en Colab
    #%matplotlib inline
    # Visualización: Gráfico de barras de los programas genero femenino
    plt.figure(figsize=(8, 6))
    sns.barplot(x='count', y='nombre_del_programa', data=femenino, palette='viridis')
    plt.title('Pasantias genero femenino')
    plt.xlabel('Cantidad')
    plt.ylabel('Programa')
    plt.grid(True)
    plt.show()

    # Visualización: Gráfico de barras de los programas genero masculino
    plt.figure(figsize=(8, 6))
    sns.barplot(x='count', y='nombre_del_programa', data=masculino, palette='viridis')
    plt.title('Pasantias genero masculino')
    plt.xlabel('Cantidad')
    plt.ylabel('Programa')
    plt.grid(True)
    plt.show()
else:
    print(f"Error: {response.status_code}")
