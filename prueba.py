import json

diccionario1 = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
diccionario2 = {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Barcelona'}
arch = 'prueba.txt'
def create_arch(dic, arch, info):
    with open(arch, 'a') as archivo:
        archivo.write(f"-------------------{info}-------------------\n")
        if dic == '':
            return
        archivo.write(json.dumps(dic,indent=4) + '\n')
        

create_arch(diccionario1,arch, 'Supervisado')
create_arch(diccionario2,arch, 'No supervisado')
create_arch('',arch, 'Cabecera')


