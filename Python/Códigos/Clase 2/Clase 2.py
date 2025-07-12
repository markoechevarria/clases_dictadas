# Estructuras de control condicionales (if, elif, else)

#Instruccion:
# Si la nota es menor a 10 desaprobado
# Si la nota es mayor a 10, pero menor a 17 aprobado
# Si la nota es mayor a 17 excelente

nota = 20

if ( nota < 10 ):
    print("Desaprobado")  # 0 1 2 3 4 5 6 7 8 9 
elif ( nota < 14 ):   # solamente pasarian los valores de 10 11 12 13 ... 20 
    print("Aprobado")  # 10 11 12 13 14 15 16
elif (nota < 17):
    print("Casi excelente")
else: 
    print("Excelente")


print("El programa termino")

#Estructuras de control bucles ( for , while )
# El bucle "for"

for i in range(0,10): # 0 1 2 3 4 5 6 7 8 9
    print(i)
print("el programa termino")
# i = 0
# i = 1
# i = 2
#  ...
# i = 8 
# i = 8 

for numero in range (5): # 0 1 2 3 4
    print(numero)
# numero = 0 

cadena = "programacion"
for letra in cadena:
    print(letra)
print("termino")
