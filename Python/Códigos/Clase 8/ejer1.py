# Intenta abrir un archivo

try:
    open('hola.txt', 'r')
except FileNotFoundError:
    print("No se encontró el archivo")

# Calcular raiz cuadrada

import math
def calcular_raiz_cuadrada():
    try:
        numero = int(input("Ingresa un numero para obtener la raiz cuadrada: "))
        raiz = math.sqrt(numero)
        print(f"La raiz cuadrada de {numero} es igual a {raiz}")
    except ValueError:
        print("No puedes obtener la raiz cuadrada de un negativo")

calcular_raiz_cuadrada()

# Manejar listas vacias
# IndexError

def obtener_primer_elemento( lista ):
    try:
        return lista[0]
    except IndexError:
        print("La lista esta vacia")

lista = [10 , 2 , 50]
print(obtener_primer_elemento(lista))
