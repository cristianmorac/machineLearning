import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def Descriptiva(data,columna):
    # Descriptiva(dataframe,'EDAD')
    database = data.groupby( by= [columna]).size().reset_index(name='count')
    media = np.mean(data[columna]) # dataframe['EDAD']
    mediana = np.median(data[columna]) # dataframe['EDAD']
    desviacion_std = np.std(data[columna], ddof=1) # dataframe['EDAD']
    print(f'Database: media = {media:.2f}, desviación estándar = {desviacion_std:.2f}, mediana = {mediana:.2f}')
    return database

def regresion_lineal(data,column_x,column_y):
    
    X = data[[column_x]].values
    y = data[column_y].values

    # modelo de regresion lineal
    modelo = LinearRegression()

    # entrenar modelo
    modelo.fit(X,y)
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

    plt.scatter(data[column_x], data[column_y], color='blue', label='Datos')
    plt.plot(data[column_x], predicciones, color='red', linewidth=2, label='Línea de Regresión')
    plt.title(f'{column_x} vs {column_y}')
    plt.xlabel(f'{column_x}')
    plt.ylabel(f'{column_y}')
    plt.legend()
    plt.show()
