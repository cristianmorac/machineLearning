from modulos.static_data import supervisado, modelo_Knn
import modulos.create_data as cd
from modulos.clean_data import limpiar_datos
from modulos.datos import replace_letra

# regresion lineal
from sklearn.model_selection import train_test_split

# nombre del archivo
archivo = 'Propina.xlsx'

# Crear dataframe de archivo excel
data = cd.create_dataframe(archivo)
#print(data)

# Formateo de datos
# reemplazar caracteres especiales
data_clean = limpiar_datos(data, replace_letra)

#Regresión lineal

# no supervidado
col_x = 'Propina'
col_y = 'total_factura'

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(data_clean[[col_x]], data_clean[col_y], test_size=0.2, random_state=42)

# modelo knn
model_knn = modelo_Knn(X_train,y_train, X_test, y_test)

supervisado(data_clean,X_train,y_train,X_test,y_test)

