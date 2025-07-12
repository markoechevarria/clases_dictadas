# atributos y métodos 
# Clase animal: 
# atributos (variables): tipo (pez, reptil, anfibio, mamifero), num_extremidades, tipo_alimentacion
# metodos (funciones): desplazarse(depender del num_extremidades) , alimentarse (tipo_alimentacion), dormir

class animal: # al crear una clase tenemos que crear la funcion principal (init)
    def __init__(self, tipo_animal, numero_extremidades, tipo_alimentacion, horas_de_sueno):
        self.tipo = tipo_animal
        self.num_extre = numero_extremidades
        self.alimentacion = tipo_alimentacion
        self.sueno = horas_de_sueno

    def alimentarse(self):
        print("Me estoy alimentando")

    def desplazarse(self, distancia_en_metros):
        print(f"Me estoy desplazando {distancia_en_metros} metros usando mis {self.num_extre} extremidades")

    def dormir(self):
        print(f"Estoy durmiendo {self.sueno} horas")

perro = animal( 'mamifero', 4 , 'carnivoro', 10 )
tortuga = animal( 'reptil', 4 , 'herbivoro' , 15 )
pez_globo = animal ( 'pez', 2, 'omnivoro', 8)

print( perro.sueno )
perro.alimentarse()
perro.desplazarse(20)
perro.dormir()

# Encapsulamiento

class vehiculo:
    def __init__(self ,propietario, medio_de_transporte, capacidad, velocidad):
        self.__propietario = propietario
        self.medio = medio_de_transporte
        self.capacidad = capacidad
        self.velocidad = velocidad

    def mostrar_propietario(self):
        print(f"El propietario es {self.__propietario}")

    def vender_vehiculo(self, nuevo_propietario):
        self.__propietario = nuevo_propietario
        print(f"El vehiculo ahora le pertenece a {self.__propietario}")

    def modificar_velocidad(self, velocidad):
        self.velocidad = velocidad
        print(f"Velocidad modificada a {self.velocidad}")

auto = vehiculo( 'marko', 'suelo', 4, 60 )
auto.velocidad = 80
print( auto.velocidad )
auto.modificar_velocidad(80)
auto.vender_vehiculo('Alex')
auto.mostrar_propietario()

# Herencia

class persona:
    def __init__(self, nombre, pais, edad, sexo):
        self.nombre = nombre
        self.pais= pais
        self.edad = edad
        self.sexo = sexo

    def mostrar_datos(self):
        print(f"Soy {self.nombre} del pais {self.pais}, tengo {self.edad} anios, y soy de sexo {self.sexo}")


class profesor(persona):
    def __init__(self, nombre, pais, edad, sexo, area, grado):
        super().__init__(nombre, pais, edad, sexo)
        self.area = area
        self.grado =  grado

    def mostrar_datos_profesor(self):
        print(f"Soy {self.nombre} y ensenio {self.area} y tengo un grado de {self.grado}")


class alumno(persona):
    def __init__(self, nombre, pais, edad, sexo, carrera, universidad):
        super().__init__(nombre, pais, edad, sexo)
        self.carrera = carrera
        self.universidad =  universidad

class universitario(alumno):
    def __init__(self, nombre, pais, edad, sexo, carrera, universidad, ciclo):
        super().__init__(nombre, pais, edad, sexo, carrera, universidad)
        self.ciclo = ciclo

    def mostrar_datos_universitario(self):
        print(f"Soy {self.nombre}, soy universitario y estoy en el ciclo {self.ciclo}")

class tecnico(alumno):
    def __init__(self, nombre, pais, edad, sexo, carrera, universidad, anio):
        super().__init__(nombre, pais, edad, sexo, carrera, universidad)
        self.anio = anio

    def mostrar_datos_tecnico(self):
        print(f"Soy {self.nombre}, soy tecnico y curso el anio {self.anio}")


juan = profesor( 'Juan', 'Peru', 30, 'Masculino', 'Calculo', 'Doctor')
juan.mostrar_datos()
juan.mostrar_datos_profesor()

luis = universitario( 'Luis', 'Peru', 22, 'Masculino', 'ingenieria', 'Catolica', 5 )
luis.mostrar_datos()
luis.mostrar_datos_universitario()