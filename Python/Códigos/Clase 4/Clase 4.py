# Estructuras de datos: Listas 
# Declaración de listas: [] y list()

lista_vacia1 = []
lista_vacia2 = list()

variable1 = 10
variable2 = 12
variable3 = 50
variable = [10, 12, 50]
lista_mascotas = ['perro','gato','loro']
lista_flot = [14.5 , 12.0 , 16.5]
lista_numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

# Obtener elemento de una lista 
# indices

lista_num=[1,2,3,4,5,6,7,8,9,10]
# indices: 1 2 3 4 5 6 7 8 9
# indices: 0 1 2 3 4 5 6 7 8

variable = [10, 12, 50]
print( variable[2] )
print( variable )
print( variable.index(12) )

lista_variable = variable
print(lista_variable)

variable = [10, 12, 40, 50 , 60, 70]
           # 0   1   2   3   4   5
lista_corta = variable[2:5]
print(lista_corta)

variable = [10, 12, 40, 50 , 60, 70]
           #-6  -5  -4  -3   -2  -1
lista_corta2 = variable[-4]
print(lista_corta2)

variable = [10, 12, 40, 50 , 60, 70]
variable[2] = 10
print(variable)


# Recorrer listas

lista_num = [1 , 3 , 5 , 7 , 9]
        #    0   1   2   3   4 
for i in lista_num:
    print(i)

longitud = len(lista_num)  # len = lenght

n=0
while ( n<longitud ):
    print(lista_num[n])
    n=n+1

lista1=[2 , 3]
lista2=[1 , 2]
print( lista1[0] == lista2[1] )

# Agregar y remover elementos: append(), + , pop() , remove()

prom = [15, 14, 16, 20, 10]
prom.append(11) # agregar elementos
print(prom)

prom = [15, 14, 16, 20, 10]
prom.pop(2) # eliminar elementos por indice
print(prom)

prom = [15, 14, 16, 20, 10]
prom.remove(14) # eliminar elementos por valor
print(prom)



# Tuplas
# Son inmutables: no pueden ser alteradas, no varian

tupla = (2,4,6,8)
print(tupla)

print(tupla[0])
longitud = len(tupla)
for i in tupla:
    print(i)

# tupla[0] = 3         esto no se puede pq es inmutable
print(tupla)



# Diccionarios
# Creación: {}, {“”:’’,}
# key : value

diccionario = {
    'nombre' : 'marko',
    'edad' : 21,
    'pais' : 'peru',
}

# Obtención de valores

print( diccionario['nombre'] )
print( diccionario['edad'] )
print( diccionario['pais'] )

# Recorrer diccionario

for i in diccionario.keys():
    print(i)

for i in diccionario.values():
    print(i)

diccionario['nombre'] = 'juan'
print(diccionario)


# Manipulación de Cadenas de Caracteres
# Metodo strip()

cadena = '      hola a todos           '
print(cadena)
cadena_nueva = cadena.strip()
print(cadena_nueva)

# Metodo split()
# Separa una cadena y lo guarda en una lista
cadena = "hola a todos"
lista_nueva = cadena.split()
print(lista_nueva)

# Metodo join()
# Agarra una lista y une una cadena
lista = ['hola', 'a', 'todos']
cadena = " ".join(lista)
print(cadena)

# Metodo format()
palabra = 'mundo'
cadena_nueva = "Hola {}".format('juan')
print(cadena_nueva)

# Metodo lower y upper
palabrota = "VOLAR"
palabrita = palabrota.lower()
print(palabrita)

palabrita = "jugar"
palabrota = palabrita.upper()
print(palabrota)

palabra = 'ESTE ES UN TEXTO'
oracion = palabra.capitalize()
print(oracion)

cadena = 'hola a todos'
cadena_nueva =  cadena.replace('todos', 'ustedes')
print(cadena_nueva)