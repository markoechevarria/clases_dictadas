#Escribe una función raiz_cuadrada_entera(numero) que reciba un número y retorne su raíz cuadrada entera utilizando un bucle. Si el número es negativo, la función debe retornar un mensaje indicando que no existe una raíz cuadrada real para números negativos.

def raiz_cuadrada_entera( numero ):

    if ( numero < 0 ):
        return 'No existe una raíz cuadrada real para números negativos.'

    i = 1
    while ( i**2 < numero ):
        i = i + 1 

    i = i - 1
    return i

numero = int(input("Ingrese un numero para extraer la raiz entera: "))
print( raiz_cuadrada_entera( numero ) )

# Escribe una función tabla_multiplicar(n, limite) que reciba un número n y un límite limite, y retorne la tabla de multiplicar de n hasta limite. La función debe validar que ambos argumentos sean números enteros positivos, de lo contrario debe retornar un mensaje de error.

def tabla_multiplicar( n , limite ):
    if ( n<0 or limite<0 ):
        print( 'Error: los valores tienen que ser positivos' )
    for i in range( limite ): # 0 1 2 3 4 5 6 ... limite-1
        print(f" {n} x {i+1} = {n*(i+1)}")
    
valor = int(input("Ingrese un numero para generar su tabla de multiplicar: "))
limite = int(input("Ingrese el limite de esa tabla de multiplicar: "))

tabla_multiplicar( valor , limite )
# n = 6
# limite = 20 

# 6 x 1 = 6
# 6 x 2 = 12
# 6 x 3 = 18
# 6 x 4 = 24
#   ....
# 6 x 20 = ...