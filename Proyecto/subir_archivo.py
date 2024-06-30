import pandas as pd
import numpy as np
import os

# Especificar la ruta del archivo .xlsx
archivo = 'Resultados_Prueba_Saber.xlsx'
path = os.path.normpath(os.path.abspath(archivo))
file_path = path

# Leer el archivo Excel
data = pd.read_excel(file_path)

# limpiar datos
replace_letra = {
    'Ã\x81': 'A',
    'Ã“': 'O',
    'Ã‘': 'Ñ',
    'Ã\x8d': 'I',
    'Ã‰': 'E',
    'Ãœ': 'U',
    'Ãš': 'U'
}

# obtener todas las columnas
columnas = data.columns.to_list()

def limpiar_datos(df,columns, dic):
    df[columns] = df[columns].replace(dic , regex=True)

#limpiar_datos(data,columnas,replace_letra)

def formateo_texto(df,palabra, columna):
        #df.drop(df[df[columna] ==palabra].index, inplace=True)
    for c in columna:
        df.drop(df[df[c] ==palabra].index, inplace=True)

formateo_texto(data,'Sin datos',columnas)

# elminar datos nulos
data = data.dropna()
print(data.value_counts())
