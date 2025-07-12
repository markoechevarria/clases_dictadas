# Funcion para calcular area y perimetro de un circulo

# area de un circulo = pi * radio al cuadrado
# perimetor del circulo = 2 * pi * radio

import math

def area_perimetro_circulo( radio ):
    area = math.pi * (radio**2)
    perimetro = 2 * math.pi * radio
    print(f"El perimetro es {perimetro} y el area es {area}")

area_perimetro_circulo(5)

# Generador de numeros aleatorios en un rango

import random

def generar_aleatorio( minimo, maximo ):
    numero = random.randint( minimo, maximo )
    return numero

print(f"El numero aleatorio es {generar_aleatorio(1 , 10)}")

# Contador de palabras en un texto

from collections import Counter

def contador( texto ):
    palabras = texto.split()
    return Counter(palabras)

print( contador( "el dia es muy lindo el dia" ) )

# Generador de contraseñas

import random
import string

def generar_contra( longitud ):
    caracteres = string.ascii_letters  + string.digits + string.punctuation
    contra = ''.join(    random.choice(caracteres) for i in range(longitud)   )
    return contra

print(generar_contra( 20 ))