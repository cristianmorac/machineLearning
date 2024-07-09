# importaciones grafica
import seaborn as sns
import matplotlib.pyplot as plt

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
    plt.show()


def grafico_apilado(data,col_x,filter):
    col_y = filter[2]
    # agrupar fumadores y no por dia de la semana
    data2 = data.groupby([col_x,col_y]).size().reset_index(name='count')
    # valores del grafico de barras
    x = data2[col_x].unique()

    values = {}
    for i,valor in enumerate(filter):
        
        # Crear datos para el grafico
        clave = f'y{i}'
        values[clave] = data2['count'][data2[col_y]== valor]
    
    # grafica apilada
    plt.bar(x,values['y0'], color='r')
    plt.bar(x,values['y1'], bottom=values['y0'], color='b')
    plt.title(f'{col_x} vs {col_y}')
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.legend(filter)
    plt.show()
    
    """ y3 = data2['count'][data2[col_y]== filter1]
    y4 = data2['count'][data2[col_y]== filter2]

    # Crear grafica
    plt.bar(x,y3, color='r')
    plt.bar(x,y4, bottom=y3, color='b')
    plt.legend([filter1,filter2])
    plt.show() """