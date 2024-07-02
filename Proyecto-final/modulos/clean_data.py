
# limpiar datos
def limpiar_datos(df,columns, dic):
    df[columns] = df[columns].replace(dic , regex=True)
    return df

#limpiar_datos(data,columnas,replace_letra)

# eliminar filas campo Sin dato
def filas_Sin_datos(df, palabra_drop, columna):
        #df.drop(df[df[columna] == palabra_drop].index, inplace=True)
    for c in columna:
        df.drop(df[df[c] == palabra_drop].index, inplace=True)
    
    # elminar datos nulos
    df = df.dropna()

    return df
