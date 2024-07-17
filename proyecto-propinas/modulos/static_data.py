import numpy as np
import pandas as pd
from modulos.graphics import grafico_regresion
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from modulos.create_data import create_arch

def modelo_Knn(X_train,y_train, X_test, y_test):
    dic = {'Exactitud del modelo': ''}

    knn = KNeighborsClassifier(n_neighbors=3)
    # Crear un modelo KNN con 3 vecinos
    knn = KNeighborsClassifier(n_neighbors=3)
    # Entrenar el modelo KNN utilizando los datos de entrenamiento
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    #Evaluar el modelo
    accuracy = accuracy_score(y_test, y_pred)
    dic['Exactitud del modelo'] = f'{accuracy * 100:.2f}%'
    create_arch(dic,'Modelo Knn')

def modelo(X_train,y_train, supervisado):
    dic = {
        'Modelo': f'{supervisado}',
        'Coeficiente (pendiente)': '',
        'Intercepcion': ''
    }
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Mostrar los coeficientes del modelo
    dic['Coeficiente (pendiente)'] = model.coef_[0]
    dic['Intercepcion'] = model.intercept_

    create_arch(dic,dic['Modelo'])
    return model

def prediccion(model, X_test):
    # Realizar predicciones
    y_pred = model.predict(X_test)
    return y_pred
# Regresion lineal

def mse_r2(valor,prediccion, info):
    dic = {
        'Medicion': f'mse y r^2 {info}',
        'mse' : '',
        'r2' : ''
    }
    dic['mse'] = mean_squared_error(valor, prediccion)
    dic['r2'] = r2_score(valor, prediccion)

    create_arch(dic,dic['Medicion'])



def supervisado(data,X_train, y_train,X_test,y_test):

    dic = {
        'Modelo': 'Supervisado',
        'comparison': ''
    }
    # Crear y entrenar el modelo de regresión lineal
    model = modelo(X_train,y_train,'Supervisado')
    predicciones = prediccion(model,X_test)
    
    # Comparar algunas predicciones con los valores reales
    comparison = pd.DataFrame({'Real': y_test, 'Prediccion': predicciones})
    
    # converdir dataframe a JSON
    data_dic = comparison.head().to_dict(orient='records')
    # guardar en el diccionario
    dic['comparison'] = data_dic

    create_arch(dic,dic['Modelo'])
    mse_r2(y_test,predicciones, 'Supervisado')

    # crear grafico de regresión
    grafico_regresion(data, X_test,y_test, predicciones,'si')


def no_supervisado(data,column_x,column_y):
    
    X = data[[column_x]].values
    y = data[column_y].values

    model = modelo(X,y,'No supervisado')
    predicciones = prediccion(model,X)
    mse_r2(y,predicciones, 'No supervisado')
    # crear grafico de regresión
    grafico_regresion(data, column_x,column_y, predicciones,'no')

def Descriptiva(data,columna):
    dic = {
        'media': '',
        'mediana': '',
        'desviacion_std': ''
    }
    # Descriptiva(dataframe,'EDAD')
    database = data.groupby( by= [columna]).size().reset_index(name='count')
    dic['media'] = np.mean(data[columna]) # dataframe['EDAD']
    dic['mediana'] = np.median(data[columna]) # dataframe['EDAD']
    dic['desviacion_std'] = np.std(data[columna], ddof=1) # dataframe['EDAD']
    create_arch(dic,'Estadistica Descriptiva')
    return dic