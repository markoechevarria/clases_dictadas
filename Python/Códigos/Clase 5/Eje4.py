#Escribe una función caracteres_unicos(cadena) que reciba una cadena y determine si todos sus caracteres son únicos. La función debe ignorar espacios y ser sensible a mayúsculas y minúsculas.

# Hola a todos
# cesar
# sensible a mayusculas y minusculas: A no es lo mismo que a 

alumno = 'MARKO'
def caracteres_unicos( cadena ): 
    cadena_nueva = cadena.replace( " " , "" )
    lista = []
    for letra in cadena_nueva:
        if letra in lista:
            return False
        else:
            lista.append( letra )
    return True


caracteres = input("Ingrese una cadena para verificar si todos sus caracteres son unicos: ")
print( caracteres_unicos( caracteres ) )

# Escribe una función suma_digitos(numero) que reciba un número entero positivo y retorne la suma de sus dígitos. La función debe verificar que el número es positivo; en caso contrario, debe retornar un mensaje de error.

def suma_digitos( numero ):
    numero_auxiliar= numero
    if (numero<0):
        print("Error, el numero es negativo.")

    suma = 0
    while ( numero>0 ):  # 1245
        digito = numero % 10  # 1245 = 10 * 124 + 5
        numero = (numero - digito)/10 # 1245 - 5 = 1240 
        suma = suma + digito  

    print(f"La suma de los digitos de {numero_auxiliar} es igual a {suma}")

numero = int(input("Ingresa el numero para sumar sus digitos: "))
suma_digitos( numero )