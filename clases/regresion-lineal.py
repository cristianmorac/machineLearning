# Prueba de regresión lineal
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generar datos de ejemplo
np.random.seed(42)
horas_estudio = np.random.rand(100) * 10  # Horas de estudio entre 0 y 10
calificaciones = 2.5 * horas_estudio + np.random.randn(100) * 2 + 50  # Calificaciones con algo de ruido

# Crear un DataFrame con los datos
df = pd.DataFrame({
    'horas_estudio': horas_estudio,
    'calificaciones': calificaciones
})

print(df.head())

#Poner el gráfico

""" plt.scatter(df['horas_estudio'], df['calificaciones'], color='blue')
plt.title('Horas de Estudio vs Calificaciones')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificaciones')
plt.show() """

#Preparar los datos para la regresión

X = df[['horas_estudio']].values  # Variable independiente
y = df['calificaciones'].values   # Variable dependiente

#Crear y entrenar el modelo de regresión

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X, y)

# Obtener los coeficientes del modelo
intercepto = modelo.intercept_ #Linea de rgresión que se cruza con el eje Y, cuando las caracteristicas son 0
pendiente = modelo.coef_[0] # Es una lista con un solo valor, es la pendiente

print(f'Intercepto: {intercepto:.2f}')
print(f'Pendiente: {pendiente:.2f}')

#Hacer las predicciones
predicciones = modelo.predict(X)

mse = mean_squared_error(y, predicciones)
r2 = r2_score(y, predicciones) # Se acerca a 1 Es un buen ajuste del modelo , se explica bien la variabilidad

print(f'Mean Squared Error (MSE): {mse:.2f}')
print(f'R^2 Score: {r2:.2f}')

#Visualizar el modelo de regresión

plt.scatter(df['horas_estudio'], df['calificaciones'], color='blue', label='Datos')
plt.plot(df['horas_estudio'], predicciones, color='red', linewidth=2, label='Línea de Regresión')
plt.title('Horas de Estudio vs Calificaciones')
plt.xlabel('Horas de Estudio')
plt.ylabel('Calificaciones')
plt.legend()
plt.show()