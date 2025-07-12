# Escribe una función calcular_promedio(a, b, c) que reciba tres números y retorne su promedio. Si alguno de los valores no es un número, la función debe retornar un mensaje de error.

def calcular_promedio( a , b , c ):
    promedio = ( a + b + c ) / 3
    return promedio
# print( calcular_promedio( 4 , 6 , 2 ) )

# Escribe una función es_palindromo(numero) que reciba un número entero y retorne True si es un palíndromo o False si no lo es. La función debe ignorar los ceros a la izquierda del número.

def cantidad_cifras( numero ): # 12321
    cantidad = 0
    while ( numero > 0 ):
        numero = numero // 10
        cantidad = cantidad + 1
    return cantidad

def es_palindromo( numero ):   # 12321
    cant_cifras = cantidad_cifras(numero)
    palindromo = True
    for i in range( int((cant_cifras-1)/2) ): # 7 veces: 0 1 2 3
        ultimo_digito = numero % 10    # res( 12321 // 10 ) = 12321
        primer_digito = numero // 10**( cant_cifras - 2*i - 1 )

        numero = numero - primer_digito * (10 ** (cant_cifras - 2*i - 1))
        numero = (numero - ultimo_digito)/10

        if (ultimo_digito != primer_digito):
            palindromo = False
    return palindromo
        #funcion que elimina primer y ultimo digito 

# 4123214 3      7 dig  -- 6 ceros
# 12321   2      5 dig  -- 4 ceros
# 232     1      3 dig  -- 2 ceros
# 3       0      1 dig  -- 0 ceros

print( es_palindromo(123321) )