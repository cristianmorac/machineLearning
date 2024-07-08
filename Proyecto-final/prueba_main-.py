from modulos import create_data as cd
from modulos.graphics import grafica_barra
from modulos.statistic_data import Descriptiva, regresion_lineal
from modulos.clean_data import limpiar_datos, filas_Sin_datos
from modulos.datos import replace_letra,datos_grafica_barra, datos_tag, estrato
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# nombre del archivo
archivo = 'Prueba_Saber.xlsx'
search_column = 'DEP_NAC'

# Crear dataframe de archivo excel
data = cd.create_dataframe(archivo)

# obtener todas las columnas
columnas = data.columns.to_list()

# reemplazar caracteres especiales
data1 = limpiar_datos(data,columnas, replace_letra)

# eliminar datos nulos y sin datos
data2 = filas_Sin_datos(data1,'Sin datos',columnas)

# cambiar el formato de
data2[search_column] = data2[search_column].astype("category")


codificar = OneHotEncoder()
codificacion = codificar.fit_transform(data2[[search_column]])

colum_new = pd.DataFrame(codificacion.toarray(),columns=codificar.categories_)
#print(colum_new)

data_final = pd.concat([data2, colum_new], axis="columns")

data_final.drop(search_column, axis="columns",inplace=True)


""" print(data_final['PUNTAJE_GLOBAL'].info())
print(data_final.info()) """

data_final = data_final.dropna()

data_final.columns = data_final.columns.astype(str)

#columna_x = 'DEP_NAC'
columna_y = 'PUNTAJE_GLOBAL'

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data_final, data_final[columna_y], test_size=0.2, random_state=42)

# Ajustar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print(f'Error Cuadrático Medio: {mse}')
print(f'mse: {mse}')