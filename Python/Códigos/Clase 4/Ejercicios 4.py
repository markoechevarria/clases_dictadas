#Crea una lista con 7 números enteros. Elimina el tercer y quinto elemento. Luego, ordena la lista en orden descendente y muestra el resultado.
        #0   1   2    3   4   5   6
lista = [1 , 2 , 10 , 5 , 8 , 2 , 6 ]
lista.pop(2)
lista.pop(3)
print(lista)

lista = [1 , 2 , 10 , 5 , 8 , 2 , 6 ]
lista.sort( reverse=True )
print(lista)



#Crea una tupla con 5 elementos. Cambiar el segundo elemento por un 10

tupla = (1 , 2 , 3 , 4 , 5)

lista = []
for i in tupla:  # 5
    if (i != 2): 
        lista.append(i)
    else: 
        lista.append(10)

tupla_nueva = tuple(lista)
print(tupla_nueva)

#Pide al usuario que ingrese una cadena y cuenta cuántas vocales contiene.

cadena = input("Ingrese una palabra: ")
cadena_minuscula = cadena.lower()
lista = ['a', 'e', 'i', 'o', 'u']
contador=0

for letra in cadena_minuscula:
    if letra in lista:
        contador = contador + 1

print(f"La cadena '{cadena}' tiene {contador} vocales.")