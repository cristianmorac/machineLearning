from modulos import create_data as cd
from modulos.graphics import grafica_barra
from modulos.statistic_data import Descriptiva
from modulos.clean_data import limpiar_datos, filas_Sin_datos
from modulos.datos import replace_letra,datos_grafica_barra, datos_tag

# Crear dataframe de archivo excel
data = cd.create_dataframe()

# Formateo de datos

# obtener todas las columnas
columnas = data.columns.to_list()

# reemplazar caracteres especiales
data = limpiar_datos(data,columnas, replace_letra)
#print(data['CIU_NAC'].unique())

# eliminar datos nulos y sin datos
data = filas_Sin_datos(data,'Sin datos',columnas)
#print(data.isnull().sum())

# Estadistica descriptiva
data = Descriptiva(data,'EDAD')
# print(data)

# Crear grafica de barras
grafica_barra(data.head(20), datos_grafica_barra, datos_tag)

