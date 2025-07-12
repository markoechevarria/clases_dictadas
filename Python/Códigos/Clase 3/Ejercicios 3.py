#Usa un bucle while para contar el número de valores positivos que ingrese el usuario

numero = int(input("Usuario, ingrese la cantidad de numeros totales: "))
n=10
cantpotitivos=0

while ( n < numero ): # sabemos que n=0 es menor a 3
    valor = int(input("Ingrese un numero: "))
    if ( valor > 0 ):
        cantpotitivos = cantpotitivos + 1
    n = n + 1

print("Has ingresado " + str(cantpotitivos) + " numeros positivos.")

# Pedir al usuario que ingrese su edad

edad = int(input("Ingresa tu edad: "))

while ( edad > 0 ):
    if ( edad < 18 ):
        print("Es menor de edad")
    else:
        print("Bienvenido.")

print("Finalizado")

# Pedir al usuario que ingrese numeros hasta que uno sea negativo

num = int(input("Ingrese un numero, programa acaba cuando sea negativo: "))
#10

while ( num > 0 ):
    num = int(input("Ingrese un numero, programa acaba cuando sea negativo: "))
    # 6 , 1000 , 800000000000 , -5

print("Finalizado")