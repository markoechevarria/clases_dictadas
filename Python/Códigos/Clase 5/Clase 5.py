# Definición y Llamada a Funciones
# Definir
def saludar():
    print("hola")

# Llamar 
saludar()

# Parametros y argumentos

def sumar( a , b ):   # parametros
    print( a + b )

sumar( 1 , 2 )   # argumentos

def saludar_2( nombre ): # nombre = 5
    print("hola " + str(nombre))
saludar_2( "juan" )

# Tipos de Parámetro (obligatorios y por defecto)

def saludar_3( nombre = "desconocido" ):
    print("hola " + nombre)
saludar_3()

def sumar_2( a , b = 3 ):
    print( a + b )

sumar_2( 4 )

# Valores de Retorno

def sumar_3( a , b ):
    return a + b
guardar = sumar_3( 1 , 5 )
print(guardar)

def calcu( a, b ):
    return a*b , a+b 
calculadora = calcu( 2 , 7 )
print(calculadora)

def calcu_2( a, b ):
    return a*b , a+b 
multi, sumi = calcu_2( 2 , 7 ) # 1 , 5 
print(sumi)

def operaciones( a, b ):
    return a+b, a-b, a*b, a/b

sum,res,mul,div = operaciones( 10 , 2 )
print(div)

#Alcance de variables

mul = 2        #variable global
def elevar1( a ):
    return mul * a
guardar1 = elevar1( 5 )
print(guardar1)
         
def elevar2( a ): 
    mul = 2     #variable local
    return mul * a
guardar2 = elevar2( 5 )
print(guardar2)
print(mul)

def funcion(nombre): # nombre = 'luis'
    saludo = ",bienvenido"
    print("hola " + saludo + " " + nombre)

funcion('luis')