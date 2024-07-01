import matplotlib.pyplot as plt
import seaborn as sns

def grafica_barra(dataframe, datos_grafica_barra, datos_tag):
        
        for clave, valor in zip(datos_grafica_barra, datos_tag):
            datos_grafica_barra[clave] = valor
        # crear grafico de barras
        plt.figure(figsize=(8, 6))
        sns.barplot(x=datos_grafica_barra['columna_x'], y=datos_grafica_barra['columna_y'], data=dataframe)
        plt.title(datos_grafica_barra['title'])
        plt.xlabel(datos_grafica_barra['xlabel'])
        plt.ylabel(datos_grafica_barra['ylabel'])
        plt.show()