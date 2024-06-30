import pandas as pd
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

limpiar_datos(data,columnas,replace_letra)

def filas_nulas(df, palabra_drop, columna):
        #df.drop(df[df[columna] == palabra_drop].index, inplace=True)
    for c in columna:
        df.drop(df[df[c] == palabra_drop].index, inplace=True)

filas_nulas(data,'Sin datos',columnas)
filas_nulas(data,0,columnas)

print(data['CIU_NAC'].unique())
