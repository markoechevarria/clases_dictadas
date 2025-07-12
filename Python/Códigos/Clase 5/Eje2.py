# Escribe una función mcd(a, b) que reciba dos números y retorne su máximo común divisor. Si uno de los números es negativo, la función debe convertirlo en positivo antes de calcular el MCD.

# 18 , 12 maximo numero que es divisor de ambos numeros 
# 18 divisores son 1 2 3 6 9 18
# 12 diviores son 1 2 3 4 6 12     se repiten: 1 2 3 6

def menorymayor( a , b ):
    if a > b:
        menor=b
        mayor=a
    else: 
        menor=a
        mayor=b
    return menor, mayor 

def mcd( a,b ): 
    a = abs(a) #funcion abs es valor absoluto 
    b = abs(b)
    menor , mayor = menorymayor(a,b)
    macodi=1
    while( True ):
        contador = 0
        for i in range(1, int(menor)): # 1 2 3 ... menor-1
            if (menor%(i+1)==0 and mayor%(i+1)==0):
                menor = menor/(i+1)
                mayor = mayor/(i+1)
                macodi = macodi * (i+1)
                break # el bucle for encuentra la i 
            else:
                contador= contador + 1 # 11
        if contador == menor-1:
            return macodi

print(mcd(18,36)) 
# en caso no tengan divisor en comun 
# 18 = 1 2 3 6 9 18
# 36 = 1 17

# Escribe una función convertir_segundos(segundos) que reciba una cantidad de segundos y retorne una tupla con la cantidad de horas, minutos y segundos. Si los segundos son negativos, la función debe retornar un mensaje de error.

def convertir_segundos( segundos ):  # horas, minutos y segundos
    if ( segundos < 0):
        return 'Error, la cantidad de segundos no puede ser negativa'
    horas = segundos // 3600
    segundos = segundos - horas * 3600  # deja los segundos restantes
    minutos = segundos // 60 
    segundos = segundos - minutos * 60  # deja los segundos restantes
    return horas, minutos, segundos

cantidad = int( input("Ingrese a cantidad de segundos a convertir: ") )
conversion = convertir_segundos( cantidad )  # ( horas , minutos, segundos )
print(conversion)
horas1, minutos1, segundos1 = convertir_segundos(cantidad)
print(f"La cantidad de segundos {cantidad} equivale a {horas1} horas, {minutos1} minutos y {segundos1} segundos")

# 4350 segundos convertir 
# 1 minuto = 60 segundos 
# 1 hora = 60 minutos
# 1 hora = 3600 segundos
#4350 seg = 1 * 3600 seg + 750 seg  # 4350 // 3600 = 1
#4350 seg = 1 hora + 750 seg
#4350 seg = 1 hora + 750 seg
#4350 seg = 1 hora + 750 seg
#    750 seg = 12 * 60 seg + 30 seg  # 750 // 60 = 12
#    750 seg = 12 * 1 min + 30 seg
#    750 seg = 12 min + 30 seg
#4350 seg = 1 hora + 12 min + 30 seg
