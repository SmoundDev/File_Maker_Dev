import os
from ContentFile import File_Content as fc


def crear_archivo(ruta_destino, nombre_archivo, extension_archivo):
    


    _fileContent, _nombre_archivo = fc.ReturnContentByExtension(
        nombre_archivo, extension_archivo)
    
    if extension_archivo == 'partial':
        extension_archivo = 'cshtml'
        
    extension_archivo = '.'+extension_archivo
    ruta_completa = os.path.join(
        ruta_destino, _nombre_archivo+extension_archivo)
    
    newFolder = ''
    if '\\' in _nombre_archivo:
        newFolder = _nombre_archivo.split('\\');
        if not os.path.exists(os.path.join(ruta_destino,newFolder[0])):
            os.makedirs(os.path.join(ruta_destino,newFolder[0]))

    with open(ruta_completa, 'w') as archivo:
        archivo.write(_fileContent)
        # archivo.write('$(document).ready(function (e){\n});\n')
    print(
        f'Se ha creado el archivo {_nombre_archivo} en la ruta {ruta_destino}')


def main():
    ruta_destino = input('Ingrese la ruta destino: ')

    while True:
        nombre_archivo = input('Ingrese el nombre de archivo: ')
        extencion_archivo = input(
            'Ingrese la extension del archivo (sin punto): ')

        if '.' in extencion_archivo:
            extencion_archivo = extencion_archivo.replace('.', '')

        crear_archivo(ruta_destino, nombre_archivo, extencion_archivo)
        respuesta = input('¿Desea crear otro archivo? (s/n): ')
        if respuesta.lower() != 's':
            break

    while True:
        respuesta = input(
            '¿Desea ingresar una nueva ruta destino? (presione "ctrl + m" para continuar): ')
        if respuesta == '\x0d':
            ruta_destino = input('Ingrese la nueva ruta destino: ')
            nombre_archivo = input('Ingrese el nombre de archivo: ')
            crear_archivo(ruta_destino, nombre_archivo + '.js')
        else:
            break


if __name__ == '__main__':
    main()
