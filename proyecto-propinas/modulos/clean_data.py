# limpiar datos
def limpiar_datos(df, dic):
    # obtener todas las columnas
    columnas = df.columns.to_list()
    df[columnas] = df[columnas].replace(dic , regex=True)
    return df

# eliminar filas campo Sin dato
def filas_Sin_datos(df, palabra_drop, columna):
        #df.drop(df[df[columna] == palabra_drop].index, inplace=True)
    for c in columna:
        df.drop(df[df[c] == palabra_drop].index, inplace=True)
