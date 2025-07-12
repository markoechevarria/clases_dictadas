# Contar caracteres de un archivo

def contar_caracteres( nombre_archivo ):
    archivo = open( nombre_archivo , 'r' )
    contenido = archivo.read()
    archivo.close()
    return( len(contenido) )

print(contar_caracteres('texto.txt'))

#Buscar y reemplazar texto

def buscar_reemplazar (archivo , palabra, palabra_nueva, archivo_nuevo):
    archivo = open(archivo, 'r')
    contenido = archivo.read()
    archivo.close()

    contenido_nuevo = contenido.replace( palabra , palabra_nueva )

    archivo2 = open(archivo_nuevo , 'w' )
    archivo2.write(contenido_nuevo)
    archivo2.close()

buscar_reemplazar('texto.txt', 'alumno', 'profesor', 'texto_nuevo.txt')

# Concatenar archivos

def concatenar_archivos(archivo1, archivo2, archivo_nuevo):
    archi1 = open(archivo1 , 'r')
    contenido1= archi1.read()
    archi1.close()

    archi2 = open(archivo2 , 'r')
    contenido2= archi2.read()
    archi2.close()

    archi_nuevo = open(archivo_nuevo , 'w')
    archi_nuevo.write( contenido1 + contenido2)
    archi_nuevo.close()

concatenar_archivos( 'texto.txt' , 'texto_nuevo.txt', 'texto_nuevo2.txt' )