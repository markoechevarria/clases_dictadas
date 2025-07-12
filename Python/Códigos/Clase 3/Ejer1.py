# Cuenta la cantidad de dígitos pares e impares en un número entero positivo ingresado por el usuario.

num = 1 #float(input("Ingrese un numero: "))
numero = num
pares=0
impares=0

while ( num > 0 ): # 12345
    dig = num % 10 # 5 
    if ( dig % 2 == 0 ):
        pares = pares + 1
    else: 
        impares = impares + 1
    num = num // 10  # 12345//10=123.4

print(f"El numero {numero} tiene {pares} digitos pares y {impares} digitos impares")

# Escribe un programa en el que el usuario intente adivinar un número secreto (predefinido en el código) entre 1 y 10. El programa debe dar pistas si el número es mayor o menor.

secreto = 5
usuario = -1
lim_min = 1
lim_max = 10

while( usuario != secreto ):
    usuario=int(input(f"Adivina el numero (el numero está entre {lim_min} y {lim_max}): "))
    
    while ( (usuario < lim_min) or (usuario > lim_max) ):
        print("Cuidado, te estas pasando de los limites, intantalo de nuevo.")
        usuario=int(input(f"Adivina el numero (el numero está entre {lim_min} y {lim_max}): "))

    if ( usuario > secreto ):
        print("Te pasaste")
        lim_max=usuario
    elif ( usuario < secreto ):
        print("Estas muy bajo")
        lim_min=usuario
    else :
        print(f"Encontraste el numero secreto {secreto}")

print("Juego finalizado")