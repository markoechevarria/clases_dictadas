#Este es un comentario de python

#Asignaciones y variables
#Los nombres de las variables no pueden empezar por numero
#Los nombres de las variables no pueden contener caracteres especiales, salvo el guion bajo "_"
nombre = 10
manzana = True
manzana = 5
Mundo = "Tierra"
Mundo = "Mercurio"
nombredealumno = "Juan"
nombreDeAlumno = "Luis"
nombre_de_alumno = "pedro"

#Tipo de dato "int"
#int viene de integer
entero = 10
print(entero)
print(type(entero))

#Tipo de dato "float"
#float viene de flotante
flotante = 1.5
print(flotante)
print(type(flotante))

#Tipo de dato "str"
#str viene de string (cadena)
cadena = "marko"
print(cadena)
print(type(cadena))

#Tipo de dato "bool"
#bool viene de booleano   Falso y Verdadero
booleano1 = False
booleano2 = True
print(booleano1)
print(booleano2)
print(type(booleano1))


#Operaciones aritmeticas

suma = 4 + 4 
resta = 10 - 1 
multiplicacion = 7 * 10 
division = 100 / 5
potenciacion = 10 ** 2
modulo =  50 % 6 # modulo es el residuo
# 11 = 2 * 5 + 1
# 30 = 7 * 4 + 2
# 50 = 6 * 8 + 2 

parte_entera = 25 // 7
# 40 = 6 * 6 + 4
# 50 = 7 * 7 + 1
# 25 = 7 * 3 + 4


#Operadores de comparacion
# < , > , >= , <= , != , ==

print( 15 < 10 )
print( 15 > 10 )

print( 10 >= 10 )
print( 15 <= 15 )

print( 10 == 11 )
print( 10 != 11 )

#Operaciones logicas
# and , or  , not
#  y  , o   , no

# El operador and significa "y"

e1 = " limpio mi casa "
e2 = " estudio "
# Tabla and
# V y V = V
# V y F = F
# F y V = F
# F y F = F 

# El operador or significa "o"

e1 = " limpio mi casa "
e2 = " estudio "

# Tabla or
# V y V = V
# V y F = V
# F y V = V
# F y F = F 

# El operador not significa "no"

e1 = "no limpio mi casa"

#Tabla not
# not V = F
# not F = V

# Funcion de input y output (entrada y salida)
# Funcion de salida: print
#Salto de linea con \n
print("este es un print \neste es un print en otra linea \neste esta mas abajo ")

# Funcion de entrada: input
nombre = input("Escribe tu nombre: ")

#Concatenacion
print("Tu nombre es " + nombre + " y eres bienvenido")