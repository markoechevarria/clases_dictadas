# Apertura y Cierre de Archivos

# open('nombre_archivo', 'modo’)      .close() para cerrar

# Modos: 
# 'r' - Lectura (modo predeterminado).
# 'w' - Escritura (crea un archivo nuevo o sobreescribe uno existente).
# 'a' - Agregar (añade al final del archivo).

# write(): Escribe una cadena en el archivo
# writelines(): Escribe una lista de cadenas en el archivo

archivo = open( 'texto.txt' , 'w' )
archivo.write('Hola, este es un archivo')
archivo.writelines( ['hola\n' , 'soy\n' , 'alumno\n'] )
archivo.close()

# read(): Lee todo el contenido del archivo como una cadena.
# readline(): Lee una línea a la vez.
# readlines(): Lee todas las líneas y devuelve una lista de cadenas

archivo2 = open( 'texto.txt' , 'r' )


texto = archivo2.read()
print(texto)

linea = archivo2.readline()
print(f"Esta es solo una linea: {linea}")

lineas = archivo2.readlines()
for i in lineas:
    print(i.strip())

archivo.close()