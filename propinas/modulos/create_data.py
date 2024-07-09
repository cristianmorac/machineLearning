import os
import json
import pandas as pd

def create_dataframe(name_file):

    # Especificar la ruta del archivo .xlsx
    #archivo = 'Resultados_Prueba_Saber.xlsx'
    archivo = name_file
    path = os.path.normpath(os.path.abspath(archivo)) # C:\Users\Admin\OneDrive\Documentos\universidad\Machine Learning
    file_path = path
    # Leer el archivo Excel
    data = pd.read_excel(file_path)
    return data

# crear archivo de resultados
arch = 'resultados.txt'
def create_arch(dic, info):
    with open('resultados.txt', 'a') as archivo:
        archivo.write(f"-------------------{info}-------------------\n")
        if dic == '':
            return
        archivo.write(json.dumps(dic,indent=4) + '\n')