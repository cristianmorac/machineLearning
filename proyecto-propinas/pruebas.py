import modulos.create_data as cd
from modulos.clean_data import limpiar_datos
from modulos.datos import replace_letra, type_column

# nombre del archivo
archivo = 'Prueba_Saber.xlsx'

# Crear dataframe de archivo excel
data = cd.create_dataframe(archivo)

# reemplazar caracteres especiales
data_clean = limpiar_datos(data, replace_letra)

columnas = data_clean.columns.to_list()

# lista de columnas con numeros
lista = type_column(data_clean, columnas)
print(lista)