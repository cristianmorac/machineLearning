import matplotlib.pyplot as plt
import seaborn as sns

datos_grafica = {
    'columna_x' : '',
    'columna_y' : '',
    'title' : '',
    'xlabel' : '',
    'ylabel' : '',
}

def grafica_barra(dataframe, dic):
        # crear grafico de barras
        plt.figure(figsize=(8, 6))
        sns.barplot(x=dic['columna_x'], y=dic['columna_y'], data=dataframe)
        plt.title(dic['title'])
        plt.xlabel(dic['xlabel'])
        plt.ylabel(dic['ylabel'])
        plt.show()