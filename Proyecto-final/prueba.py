from main import data
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# convertir a float

columna_x = 'DEP_NAC'
columna_y = 'PUNTAJE_GLOBAL'

""" data[columna_x] = data[columna_x].astype(float) """
data[columna_y] = data[columna_y].astype(float)

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data[[columna_x]], data[columna_y], test_size=0.2, random_state=20000)

""" print("X_train:\n", X_train.head())
print("X_test:\n", X_test.head())
print("y_train:\n", y_train.head())
print("y_test:\n", y_test.head()) """

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Mostrar los coeficientes del modelo
print("Coeficiente (pendiente):", model.coef_[0])
print("Intercepción:", model.intercept_)

# Realizar predicciones
y_pred = model.predict(X_test)
# Comparar algunas predicciones con los valores reales
comparison = pd.DataFrame({'Real': y_test, 'Predicción': y_pred})
print(comparison.head())

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Error Cuadrático Medio (MSE): {mse}")
print(f"Coeficiente de Determinación (R^2): {r2}")

# Calcular correlación
correlation = data[columna_x].corr(data[columna_y])
print(f"Correlación entre PUNTAJE_GLOBAL y EDAD: {correlation}")

# Cargar el conjunto de datos
iris = load_iris()
#Separar las caracteristicas y las etiquetas
X, y = iris.data, iris.target
# Convertir X y y en un DataFrame de Pandas
df_X = pd.DataFrame(X, columns=iris.feature_names)
df_y = pd.DataFrame(y, columns=['species'])

# Imprimir las primeras filas de X y las primeras etiquetas de y
print("Características (X):")
print(df_X.head())   # Imprimir las primeras 5 filas de X
print("\nEtiquetas (y):")
print(df_y.head())  # Imprimir las primeras 5 etiquetas de y

# Crear y entrenar el modelo Kneighborsclassifier (Modelo KNN)
# Crear un modelo KNN con 3 vecinos
knn = KNeighborsClassifier(n_neighbors=3)
# Entrenar el modelo KNN utilizando los datos de entrenamiento
knn.fit(X_train, y_train)

#Realizar la predicción del modelo
y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Exactitud del modelo: {accuracy * 100:.2f}%")

""" # Visualización: Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data[columna_x], data[columna_y], color='blue')
plt.title(f'Correlación entre {columna_x} y {columna_y}')
plt.xlabel(f'{columna_x}')
plt.ylabel(f'{columna_y}')
plt.grid(True)
plt.show() """


# Visualizar las predicciones
plt.scatter(X_test, y_test, color='blue', label='Datos Reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicciones')
plt.xlabel(f'{columna_x}')
plt.ylabel(f'{columna_y}')
plt.title('Predicciones vs. Datos Reales')
plt.legend()
plt.show()

""" # Visualizar los datos
plt.scatter(data['PUNTAJE_GLOBAL'], data['EDAD'])
plt.xlabel('PUNTAJE_GLOBAL')
plt.ylabel('EDAD')
plt.title('PUNTAJE_GLOBAL en función de la EDAD')
plt.show() """