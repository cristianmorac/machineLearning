replace_letra = {
    'Ã\x81': 'A',
    'Ã¡': 'a',
    'Ã‰': 'E',
    'Ã©': 'e',
    'Ã\x8d': 'I',
    'Ã\xad': 'i',
    'Ã“': 'O',
    'Ã³': 'o',
    'Ã¼': 'u',
    'Ãœ': 'U',
    'Ãš': 'U',
    'Ãº': 'u',
    'Ã¼': 'u',
    'Ã‘': 'Ñ',
    'Ã±': 'ñ'
}

# buscar columnas con numeros
def type_column(data, columns):
    tipo_datos = []
    for c in columns:
        data_type = data[c].dtypes
        if data_type == 'int64':
            tipo_datos.append(c)
    
    return tipo_datos