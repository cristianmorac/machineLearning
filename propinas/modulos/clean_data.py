def limpiar_datos(df, dic):

    # obtener todas las columnas
    columnas = df.columns.to_list()

    df[columnas] = df[columnas].replace(dic , regex=True)
    return df