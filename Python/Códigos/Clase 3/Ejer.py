# Usa un bucle while para contar el número de dígitos en un número entero positivo ingresado por el usuario.

num = float(input("Ingrese un numero: "))
cantdigitos=0
# Operador parte entera = //
# 12 // 10 = 1
# Operador modulo = %
# 12 % 10 = 2
# 5 % 2 = 1

while ( num > 0 ): # 0

    dig = num % 10  # 1
    cantdigitos = cantdigitos + 1

    num = num // 10  # 1//10=0.1

print("Tiene " + str(cantdigitos) + " digitos")

#Escribe un programa que pida al usuario un número entero positivo y calcule la suma de todos los números desde 1 hasta ese número.
# 4 = 1 + 2 + 3 + 4

n = int(input("Ingrese un numero: "))
suma=0

for i in range (n):
    suma = suma + (i+1)

print("La suma de los numeros hasta el " + str(n) + " es " + str(suma))
print(f"La suma de los numeros hasta el {n} es {suma}")

