import numpy as np

def Descriptiva(data,columna):
    database = data.groupby( by= [columna]).size().reset_index(name='count')
    media = np.mean(data[columna])
    mediana = np.median(data[columna])
    desviacion_std = np.std(data[columna], ddof=1)
    print(f'Database: media = {media:.2f}, desviación estándar = {desviacion_std:.2f}, mediana = {mediana:.2f}')
    return database