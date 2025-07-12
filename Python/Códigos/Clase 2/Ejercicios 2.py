# 1. Usa un bucle for para contar cuántas veces aparece un carácter específico en una cadena ingresada por el usuario.

cadena = input("Ingresa un texto: ")
caracter_buscado = input("Ingresa el caracter que buscas: ") # a
contador = 0

# feliz aniversario
# a
for letra in cadena: # letra = a
    if ( caracter_buscado == letra ):
        contador =  contador + 1
        #contador =     0  +  1
        #contador =     1 

        #contador =     1  +  1
        #contador =     2
             
print("El caracter " + caracter_buscado + " aparece "+ str(contador) + " veces en la cadena " + cadena)



# 2. Usa un bucle for para imprimir la tabla de multiplicar de un número dado por el usuario, del 1 al 10.

numero = int(input("Ingresa un numero para imprimir su tabla: "))
for i in range(1,11): # 1 2 3 4 5 6 7 8 9 10
    print( str(numero) + " x " + str(i) + " = " + str( numero * i ))

# 3 x 1 = 3
# 3 x 2 = 6
# 3 x 3 = 9
# 3 x 4 = 12


# 3. Calcula el factorial de un número entero positivo ingresado por el usuario. El factorial de n (denotado como n!) es el producto de todos los enteros positivos desde 1 hasta n.

# 5! = 1 * 2 * 3 * 4 * 5

numero=int(input("Ingrese el numero del que quieres calcular su factorial: "))
resultado = 1
# numero = 4

for i in range (numero): # 0 1 2 3
    resultado = resultado * (i+1)
#   resultado =     6     * (3+1)
#   resultado =     6 * 4
#   resultado =     24

print("El factorial de " + str(numero) + " es " + str(resultado))

# 1. resultado = 1
# 2. resultado = 2
# 3. resultado = 6
# 4. resultado = 24

# 4. Determina si un número ingresado por el usuario es primo. Un número primo es aquel que solo es divisible por 1 y él mismo.

# numero primo tiene 2 divisores ( 1 y el mismo)
# 7 = 1,7  2 divisores
# 8 = 1,2,4,8  4 divisores

numero=int(input("Ingrese un numero para ver si es primo: "))
contador_divisores = 0
# numero = 6
for i in range(numero): # 0 1 2 3 4 5  /  1 2 3 4 5 6
    if ( numero % ( i + 1 ) == 0 ):
        contador_divisores = contador_divisores + 1

#       6 % 1 == 0: ejecuta   contador = 1
#       6 % 2 == 0: ejecuta   contador = 2
#       6 % 3 == 0: ejecuta   contador = 3
#       6 % 4 == 0: no ejecuta
#       6 % 5 == 0: no ejecuta
#       6 % 6 == 0: ejecuta   contador = 4


if (contador_divisores == 2):
    print("El numero " + str(numero) + " es primo.")
else:
    print("El numero "+ str(numero) + " no es primo.")