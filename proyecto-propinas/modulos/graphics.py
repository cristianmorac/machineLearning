import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def grafico_regresion(data, column_x,column_y, predicciones, supervisado):

    # Si es supervisado
    if supervisado == 'no':
        columna_x = data[column_x]
        columna_y = data[column_y]
    else:
        columna_x = column_x
        columna_y = column_y

    #Visualizar el modelo de regresión
    plt.scatter(columna_x, columna_y, color='blue', label='Datos')
    plt.plot(columna_x, predicciones, color='red', linewidth=2, label='Línea de Regresión')
    if supervisado == 'no':
        plt.title(f'{column_x} vs {column_y}')
        plt.xlabel(f'{column_x}')
        plt.ylabel(f'{column_y}')
    plt.legend()
    if supervisado == 'no':
        st.pyplot(plt)
    else:    
        plt.show()