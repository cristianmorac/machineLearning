import pandas as pd

# Especificar la ruta del archivo .xlsx
file_path = 'C:\\Users\\Cristian\\Documents\\CUN\\MachineLearning\\Resultados_Prueba_Saber_Pro.xlsx'

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

# eliminar las filas que esten sin datos

limpiar_datos(data,columnas,replace_letra)
# filas_Sin_datos(data,'Sin datos',columnas )

print(data['CIU_NAC'].unique())

"""
# eliminar las filas que esten sin datos
def filas_Sin_datos(df, palabra_drop, columna):
    df.drop(df[df[columna] == palabra_drop].index, inplace=True)
    print(df[columna].unique())

filas_Sin_datos(data,'Sin datos','DEP_NAC')
filas_Sin_datos(data,'Sin datos','CIU_NAC')
 """

