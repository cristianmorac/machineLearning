import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from main import data

columna_x = 'PUNTAJE_GLOBAL'
columna_y = 'EDAD'

# Configurar Pandas para mostrar los números sin notación científica
pd.set_option('display.float_format', '{:.2f}'.format)

# Dividir los datos en conjuntos de entrenamiento y prueba
X = data[[columna_x]]  # Variable independiente
y = data[columna_y]   # Variable dependiente

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Error Cuadrático Medio (MSE): {mse}")
print(f"Coeficiente de Determinación (R^2): {r2}")

""" # Visualizar las predicciones
plt.scatter(X_test, y_test, color='blue', label='Datos Reales')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicciones')
plt.xlabel(f'{columna_x}')
plt.ylabel(f'{columna_y}')
plt.title(f'Predicciones de {columna_x} vs. Datos Reales')
plt.legend()
plt.show() """

# Cargar el conjunto de datos de Iris
iris = load_iris()
X, y = iris.data, iris.target

# Crear y entrenar el modelo de árbol de decisión
tree = DecisionTreeClassifier(random_state=42)
tree.fit(X_train, y_train)

# Realizar predicciones
y_pred = tree.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Exactitud del modelo de árbol de decisión: {accuracy * 100:.2f}%")

# Calcular correlación
correlation = data[columna_x].corr(data[columna_y])

print(f"Correlación entre tamaño y precio de casas: {correlation}")