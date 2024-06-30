from clean_data import data
from graficas import grafica_barra, datos_grafica
import numpy as np

# Estadistica descriptiva

# Datos por genero masculino
def Genero(data,genero):
    genero = data[(data['SEXO'] == genero)]
    genero = genero.groupby( by= ['EDAD','SEXO']).size().reset_index(name='count')
    return genero

def Descriptiva(data,columna):
    media = np.mean(data[columna])
    mediana = np.median(data[columna])
    desviacion_std = np.std(data[columna], ddof=1)
    print(f'Database: media = {media:.2f}, desviación estándar = {desviacion_std:.2f}, mediana = {mediana:.2f}')

# filtrar por genero masculino
hombre = Genero(data,'Hombres')

# Encontrar la media, mediana y desviacion
Descriptiva(hombre,'EDAD')

# Agregar datos al diccionario
datos_tag = ['EDAD', 'count', 'Edades de presentación del examen', 'Edad', 'Cantidad']
for clave, valor in zip(datos_grafica, datos_tag):
    datos_grafica[clave] = valor

# Crear grafica de barras
grafica_barra(hombre.head(20), datos_grafica) 
