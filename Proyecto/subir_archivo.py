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
# filas_Sin_datos(data,'Sin datos',columnas )

print(data['CIU_NAC'].unique())

def eliminar_filas():
    pass

"""
# eliminar las filas que esten sin datos
def filas_Sin_datos(df, palabra_drop, columna):
    df.drop(df[df[columna] == palabra_drop].index, inplace=True)
    print(df[columna].unique())

filas_Sin_datos(data,'Sin datos','DEP_NAC')
filas_Sin_datos(data,'Sin datos','CIU_NAC')
 """

