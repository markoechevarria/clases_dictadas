# Crea una clase Persona con atributos nombre y edad. Define un método saludar() que imprima un mensaje de saludo.
# Crea una clase Estudiante que herede de Persona y tenga un atributo adicional curso.
# Instancia objetos de Estudiante y muestra un mensaje de saludo que incluya el nombre y el curso

class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola soy {self.nombre}, y tengo {self.edad} anios")

class estudiante(persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso

    def saludar(self):
        print(f"Hola soy {self.nombre}, estudio {self.curso} y tengo {self.edad} anios")

juan = persona('juan', 30)
luis = estudiante( 'luis', 22, 'fisica')

juan.saludar()
luis.saludar()


# Diseña una clase Banco que gestione cuentas bancarias. Cada cuenta debe tener un titular, un balance y métodos para depositar y retirar dinero.
# Implementa un método que permita transferir dinero entre dos cuentas.

class cuenta:
    def __init__(self, titular, balance):
        self.titular = titular
        self.balance = balance

    def depositar(self, monto):
        self.balance = self.balance + monto
        print(f"Deposito exitoso. Balance actual de {self.balance}")

    def retirar(self, monto):
        if ( monto > self.balance ):
            print(f"Fondos insuficientes. Balance actual de {self.balance}")
        else: 
            self.balance = self.balance - monto
            print(f"Retiro exitoso. Balanace actual de {self.balance}") 

    

class banco:
    def __init__(self, nombre_banco):
        self.nombre_banco = nombre_banco

    def transferir(self, cuenta_origen, cuenta_destino , monto ):
        if cuenta_origen.balance < monto:
            print("Monto insuficiente. No puedes realizar la transaccion.")
        else: 
            cuenta_origen.retirar(monto)
            cuenta_destino.depositar(monto)
            print(f"Transferencia exitosa de {monto} soles del usuario {cuenta_origen.titular} al usuario {cuenta_destino.titular}.")

cuenta_marko =  cuenta('Marko', 200)
cuenta_luis = cuenta('Luis', 100)

bcp =  banco('BCP')
bcp.transferir(cuenta_marko, cuenta_luis, 10)

print( f"Marko ahora tiene {cuenta_marko.balance} soles" )
print( f"Luis ahora tiene {cuenta_luis.balance} soles" )

bcp.transferir(cuenta_marko, cuenta_luis, 190)

print( f"Marko ahora tiene {cuenta_marko.balance} soles" )
print( f"Luis ahora tiene {cuenta_luis.balance} soles" )

# Implementa una clase base Vehiculo con atributos marca y modelo, y métodos para acelerar() y frenar().
# Crea subclases Coche y Moto que hereden de Vehiculo. Añade métodos específicos como abrir_maletero() en Coche y hacer_caballito() en Moto.

class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print("El vehiculo esta acelerando")

    def frenar(self):
        print("El vehiculo esta frenando")

class coche(vehiculo):
    def __init__(self, marca, modelo, maletero):
        super().__init__(marca, modelo)
        self.maletero = maletero # si el maletero esta abierto o cerrado ( False o True)

    def abrir_maletero(self):
        if self.maletero == True:
            print("El maletero ya esta abierto, no hace falta abrir")
        else:
            self.maletero = True
            print("Abriendo maletero")

class moto(vehiculo):
    def __init__(self, marca, modelo, estado):
        super().__init__(marca, modelo)
        self.estado = estado 

    def hacer_caballito(self):
        if self.estado == True:
            print("Haciendo caballito")
        else:
            print("No puede hacer trucos")

moto_marko = moto('marcamoto', 'modelo1', False)
coche_marko = coche('toyota', 'modelo2024', True)

moto_marko.hacer_caballito()
coche_marko.abrir_maletero()