import pandas as pd
import seaborn as sns
from modulos.statistic_data import Descriptiva, regresion_lineal
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier

tips = sns.load_dataset("tips")

tips.to_csv('propinas.csv', sep=',', index=False, encoding='utf-8')

#print(tips)

columna_x ='total_bill'
columna_y = 'tip'

regresion_lineal(tips,columna_x,columna_y)

# Calcular correlación
correlation = tips[columna_x].corr(tips[columna_y])
print(f"Correlación entre {columna_x} y {columna_y}: {correlation}")


tips[columna_x] = tips[columna_x].astype(int)
tips[columna_y] = tips[columna_y].astype(int)

X_train, X_test, y_train, y_test = train_test_split(tips[[columna_x]], tips[columna_y], test_size=0.3, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Mostrar los coeficientes del modelo
print("Coeficiente (pendiente):", model.coef_[0])
print("Intercepción:", model.intercept_)

# Realizar predicciones
prediccion = model.predict(X_test)
# Comparar algunas predicciones con los valores reales
comparison = pd.DataFrame({'Real': y_test, 'Predicción': prediccion})
print(comparison.head())

# Evaluar el modelo
mse = mean_squared_error(y_test, prediccion)
r2 = r2_score(y_test, prediccion)
print(f"Error Cuadrático Medio (MSE): {mse}")
print(f"Coeficiente de Determinación (R^2): {r2}")

# Calcular correlación
correlation = tips[columna_x].corr(tips[columna_y])
print(f"Correlación entre {columna_x} y {columna_y}: {correlation}")

# Cargar el conjunto de datos
iris = load_iris()

#Separar las caracteristicas y las etiquetas
X, y = iris.data, iris.target

df_X = pd.DataFrame(X, columns=iris.feature_names)
df_y = pd.DataFrame(y, columns=['species'])

# Imprimir las primeras filas de X y las primeras etiquetas de y
print("Características (X):")
print(df_X.head())   # Imprimir las primeras 5 filas de X
print("\nEtiquetas (y):")
print(df_y.head())  # Imprimir las primeras 5 etiquetas de y

knn = KNeighborsClassifier(n_neighbors=3)
# Entrenar el modelo KNN utilizando los datos de entrenamiento
knn.fit(X_train, y_train)

#Realizar la predicción del modelo
y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Exactitud del modelo: {accuracy * 100:.2f}%")

# Crear y entrenar el modelo de Random Forest
forest = RandomForestClassifier(n_estimators=100, random_state=42)
forest.fit(X_train, y_train)

# Realizar predicciones
y_pred = forest.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
print(f"Exactitud del modelo de Random Forest: {accuracy * 100:.2f}%")