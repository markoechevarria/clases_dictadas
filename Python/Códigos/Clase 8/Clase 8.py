# Estructura try, except

# try: Se utiliza para envolver el código que puede generar una excepción.
# except: Captura y maneja la excepción si ocurre.

# Múltiples except

try:
    numero = int(input("Ingrese un numero para dividir a 20: "))
    resultado = 20/numero
    print(f"Este es el resultado {resultado}")
except TypeError:
    print("Ha ocurrido un error, no puedes dividir entre un string")
except ZeroDivisionError:
    print("Ha ocurrido un error, no puedes dividir entre 0")
except ValueError:
    print("Ingresa un numero, no una letra")

# Excepciones Genéricas

try:
    numero = int(input("Ingrese un numero para dividir a 20: "))
    resultado = 20/numero
    print(f"Este es el resultado {resultado}")

except Exception as e:      # crea una variable e y almacena el error Exception
    print(f"Ocurrio un error: {e}")

# Bloque finally

try:
    archivo = open('hola.txt', 'r')
except FileNotFoundError:
    print("No se encontró el archivo 'hola.txt'")
finally:
    archivo.close()