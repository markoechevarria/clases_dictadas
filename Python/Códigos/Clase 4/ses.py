# Crea una lista con 7 números enteros. Elimina el tercer y quinto elemento. Luego, ordena la lista en orden descendente y muestra el resultado.

lista = [9,15,20,4,2,80,5]
lista.pop(2)
lista.remove(2)
print(lista)
lista.sort(reverse=True)
print(lista)

# Crea una tupla con 5 elementos. Intenta cambiar el segundo elemento (esto debería fallar) y después muestra cómo crear una nueva tupla con ese elemento modificado.

tupla = (1, 5)
nueva_tupla=(tupla[0] , 3)

print(tupla)
print(nueva_tupla)

# Crea un diccionario donde las claves sean los nombres de 4 estudiantes y los valores sean sus calificaciones. Calcula la calificación promedio.

diccionario = {
    'luis': 15,
    'juan': 20,
}
for i in diccionario.keys():
    print(i)

# Pide al usuario que ingrese una cadena y cuenta cuántas vocales contiene.

cadena='fidel es f'
vocales=['a','e','i','o','u']
voc=0

for i in cadena:
    if i in vocales: voc = voc + 1

print(voc)

# Escribe un programa que pida al usuario que ingrese una palabra y la muestre al revés.

palabra='capaz'
invertido=palabra[::-1]
print(invertido)

# Pide al usuario que ingrese una frase y determina cuál es la palabra más larga.

frase="fidel es muy feoffs"
lista=frase.split()
print(lista)

mayor=max(lista, key=len)
print(mayor)

# Crea una lista con números repetidos. Elimina los duplicados sin cambiar el orden de los elementos.

lista=[1,5,4,8,9,5,6,1,2,3,7,4,8,5,9,6]
repetidos=[]
for i in lista:
    if i not in repetidos:
        repetidos.append(i)
print(repetidos)

# Crea un diccionario con 5 elementos. Pide al usuario que ingrese una clave y muestra el valor correspondiente.

diccionario = {
    'nombre':[],
    'contra':[],
    'edad':[],
}
usuario='juan'
contra='juan123'
edad=25
diccionario['nombre'].append(usuario)
diccionario['contra'].append(contra)
diccionario['edad'].append(edad)

contrase='juan123'
if contrase in diccionario['contra']:
    print(diccionario['contra'].index(contrase)) 
print(diccionario)

# Pide al usuario que ingrese dos cadenas y muestra la concatenación de ambas con un guion (-) entre ellas.

cadena1 = input("Ingrese la primera cadena: ")
cadena2 = input("Ingrese la segunda cadena: ")

cadena_nueva = cadena1 + " - " +  cadena2
print(cadena_nueva)

# Pide al usuario que ingrese una frase y una palabra a reemplazar en la frase. Luego, pide una nueva palabra e imprime la frase con el reemplazo hecho.

frase = input("Ingrese una frase: ")
palabra = input("Ingrese la palabra a reemplazar: ")
sustituto = input("Ingrese un sustituto: ")

frase_nueva = frase.replace( palabra , sustituto )
print(frase_nueva)