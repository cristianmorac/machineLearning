""" from modulos.create_data import data """

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

estrato = {
    'Estrato 6': 6,
    'Estrato 5': 5,
    'Estrato 4': 4,
    'Estrato 3': 3,
    'Estrato 2': 2,
    'Estrato 1': 1,
}

datos_grafica = {
    'columna_x' : '',
    'columna_y' : '',
    'title' : '',
    'xlabel' : '',
    'ylabel' : '',
}

datos_grafica_barra = {
    'columna_x' : '',
    'columna_y' : '',
    'title' : '',
    'xlabel' : '',
    'ylabel' : '',
}

# datos grafico de barras
datos_tag = ['EDAD', 'count', 'Edades de presentación del examen', 'Edad', 'Cantidad']
