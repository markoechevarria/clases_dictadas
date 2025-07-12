# Escribe un programa que invierta los dígitos de un número entero ingresado por el usuario. Por ejemplo, si el usuario ingresa 12345, el programa debe devolver 54321.

num = 1#float(input("Ingrese un numero para invertirlo: "))
numero = num
invertido=0

while ( num > 0 ): # 0
    dig = num % 10 # 1
    invertido = invertido * 10 + dig # 54321
    num = num // 10

print(f"El numero inverso de {numero} es {invertido}")

# Escribe un programa que convierta una calificación numérica en una calificación de letra (A, B, C, D, F) según la escala estándar.
# A 16 - 20
# B 11 - 15
# C 6 - 10
# D 1 - 5
# F 0 

nota = int(input("Usuario, ingrese la nota: "))

while ( (nota < 0) or (nota > 20) ):
    print("Esa nota no existe, respete los limites. ")
    nota = int(input("Usuario, ingrese la nota: "))
    
if ( nota >= 16 ):
    print("Su calificacion es A")
elif ( nota >= 11 ):
    print("Su calificacion es B")
elif ( nota >= 6 ):
    print("Su calificacion es C")
elif ( nota >= 1 ):
    print("Su calificacion es D")
else: 
    print("Su calificacion es F")