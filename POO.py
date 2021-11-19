class Persona(object):

    def __init__(self, dni, nombre, apellido, anioNacimiento, sexo):
        # Constructor de clase Persona
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = str(sexo)
        self.anioNacimiento = int(anioNacimiento)

    def getGenero(self, sexo):
        genero = ('Masculino','Femenino')
        if sexo.upper() == "M":
            return genero[0]
        elif sexo.upper() == "F":
            return genero[1]
        else:
            return "Desconocido"

    def getGeneracion(self, anioNacimiento):
        generacion = ''
        if(anioNacimiento >= 1930 and anioNacimiento <= 1948):
            generacion = 'Silent Generation'
        elif(anioNacimiento >= 1949 and anioNacimiento <= 1968):
            generacion = 'Baby Boom'
        elif(anioNacimiento >= 1969 and anioNacimiento <= 1980):
            generacion = "Generacion X"
        elif(anioNacimiento >= 1981 and anioNacimiento <= 1993):
            generacion = "Generacion Y: Millenials"
        elif(anioNacimiento >= 1994 and anioNacimiento <= 2010):
            generacion = "Generacion Z"
        else:
            generacion = 'Geneacion desconocida'
        return generacion

class estudiante(Persona):
    # Clase que representa a un estudiante

    def __init__(self, nombre, apellido, dni, anioNacimiento, sexo, carrera, lugarDeEstudio):

        # Invoco al constructor de clase Persona
        Persona.__init__(self, dni, nombre, apellido, anioNacimiento, sexo)

        # Nuevos atributos
        self.carrera = carrera
        self.lugarDeEstudio = lugarDeEstudio

    def mostrarDatos(self):
        return "Estudiante: " + self.nombre + " " + self.apellido + "\nCarrera: " + self.carrera + "\nLugar De Estudio: " + self.lugarDeEstudio +"."


def cargarEstudiante():
    print("Carga de datos del estudiante")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    sexo = input("Sexo: ")
    dni = input("DNI: ")
    anioNacimiento = int(input("Año de nacimiento: "))
    carrera = input("Carrera: ")
    lugarDeEstudio = input("Lugar de estudio: ")    
    print("-----------------------------")
    return estudiante(nombre, apellido, dni, anioNacimiento, sexo, carrera, lugarDeEstudio)

def ejecutarOpciones(estudiante2):    
    opcion = int(input("Que desea realizar?\n1- Ver a que generacion pertenece el estudiante.\n2- Ver los datos del estudiante.\n"))
    while opcion == 1 or opcion == 2 or opcion == 3:
        if (opcion == 1):
            print(estudiante2.getGeneracion(estudiante2.anioNacimiento))
        elif (opcion == 2):
            print(estudiante2.mostrarDatos())
        elif (opcion == 3):
            cargarEstudiante()
        print("-----------------------------")
        opcion = int(input("Desea realizar algo mas?\n1- Ver a que generacion pertenece el estudiante.\n2- Ver los datos del estudiante.\n3- Cargar otro estudiante.\n0- Salir\n"))

estudiante2 = cargarEstudiante()
ejecutarOpciones(estudiante2)

# persona1 = Persona(12345678, "Leonardo", "Caballero", 1965, "m")

# print(persona1.getGenero(persona1.sexo))

# estudiante1 = estudiante("11234567", "Jen", "Paz", 1968, "M", "compu", "ispc")

# print(estudiante1.getGeneracion(estudiante1.anioNacimiento))

# print(estudiante1.mostrarDatos())