import os
import pandas as pd

def create_dataframe():

    # Especificar la ruta del archivo .xlsx
    archivo = 'Resultados_Prueba_Saber.xlsx'
    path = os.path.normpath(os.path.abspath(archivo))
    file_path = path
    # Leer el archivo Excel
    data = pd.read_excel(file_path)
    return data
