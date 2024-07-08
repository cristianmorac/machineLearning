from modulos import create_data as cd
from modulos.graphics import grafica_barra
from modulos.statistic_data import Descriptiva, regresion_lineal
from modulos.clean_data import limpiar_datos, filas_Sin_datos
from modulos.datos import replace_letra,datos_grafica_barra, datos_tag, estrato
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# nombre del archivo
archivo = 'Prueba_Saber.xlsx'
search_column = 'DEP_NAC'
# Crear dataframe de archivo excel
data = cd.create_dataframe(archivo)

# Formateo de datos

# obtener todas las columnas
columnas = data.columns.to_list()

# reemplazar caracteres especiales
data = limpiar_datos(data,columnas, replace_letra)
#print(data['CIU_NAC'].unique())

# eliminar datos nulos y sin datos
data = filas_Sin_datos(data,'Sin datos',columnas)
#print(data.isnull().sum())

codificar = OneHotEncoder()
codificacion = codificar.fit_transform(data[[search_column]])
#print(codificacion)

colum_new = pd.DataFrame(codificacion.toarray(),columns=codificar.categories_)
#print(colum_new)

data_final = pd.concat([data, colum_new], axis="columns")

data_final = data_final.dropna()
data = data.dropna()

#print(data_final.info())
#data_final.columns = data_final.columns.astype(str)

column_y = 'PUNTAJE_GLOBAL'
#data_final.columns = data_final.columns.astype(str)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data_final, data[column_y], test_size=0.2, random_state=42)



""" print("X_train:\n", X_train.head())
print("X_test:\n", X_test.head())
print("y_train:\n", y_train.head())
print("y_test:\n", y_test.head()) """

model = LinearRegression()
model.fit(X_train, y_train)

# Mostrar los coeficientes del modelo
print("Coeficiente (pendiente):", model.coef_[0])
print("Intercepción:", model.intercept_)


