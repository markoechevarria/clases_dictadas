#Ejercicios de aplicacion

#Declara variables para tu nombre, edad, altura, y si tienes mascotas (True/False). Imprime estas variables.

nombre = "Marko"
edad = 21
altura = 170
mascota = True

print("Mi nombre es " + nombre)
print("Mi edad es " + str(edad))
print("Mi altura es " + str(altura) + " cm")
print("Tengo mascota " + str(mascota))

#Declara dos números y realiza las operaciones de suma, resta, multiplicación, y división. Imprime los resultados.

n1= 12
n2= 3

print("La suma es "+ str(n1 + n2))
print("La resta es "+ str(n1 - n2))
print("La multiplicacion es "+ str(n1 * n2))
print("La division es "+ str(n1 / n2))

#Declara dos números y usa operadores de comparación para verificar si uno es mayor, menor, igual o diferente al otro. Imprime los resultados.

n1 = 10
n2 = 15
print("El primer numero es mayor al segundo: " + str( n1 > n2 ))
print("El primer numero es menor al segundo: " + str( n1 < n2 ))
print("El primer numero es igual al segundo: " + str( n1 == n2 ))
print("El primer numero es diferente al segundo: " + str( n1 != n2 ))

#Declara tres variables booleanas y usa operadores and, or, y not para combinar y evaluar expresiones lógicas. Imprime los resultados.

var1 = True
var2 = False
var3 = True
print( var1 and var2) # Verdad y Falso = False
print( var1 and var3) # Verdad y Verdad = Verdad
print( var2 or var1) # Falso o Verdad = Verdad
print( var1 or var3) # Verdad o Verdad = Verdad
print( not var1) # no Verdad = Falso 
print( not var2) # no Falso = Verdad

#Pide al usuario que ingrese su nombre y edad, y luego imprime un mensaje con esa información.

nombre = input("Coloque su nombre: ")
edad = input("Coloque su edad: ")
print("Tu nombre es " + nombre + " y tu edad es" + edad )

#Pide al usuario que ingrese dos números, conviértelos a enteros, y muestra la suma de ellos.

n1 = int(input("Ingrese un numero: ")) 
n2 = int(input("Ingrese otro numero: "))
print("La suma de los numeros es "+ str(n1+n2))

#Pide al usuario que ingrese el ancho y el alto de un rectángulo. Calcula e imprime el área.

altura = int(input("Ingrese la altura del rectangulo: "))
ancho = int(input("Ingrese el ancho del rectangulo: "))

print("El area del rectangulo es " + str(altura * ancho))

#Pide al usuario que ingrese tres números. Calcula e imprime el promedio.

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3)/3
print("El promedio de los 3 numeros es: "+ str(promedio) )