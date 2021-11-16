class Persona(object):    

    def __init__(self, dni, nombre, apellido, anioNacimiento, sexo):
        # Constructor de clase Persona
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
        self.anioNacimiento = anioNacimiento

    def __str__(self):
        # Devuelve una cadena representativa de Persona
        return "%s: %s, %s %s, %s, %s." % (
            self.__doc__[25:34], str(self.dni), self.nombre, 
            self.apellido, str(self.anioNacimiento), self.getGenero(self.sexo))

    def getGenero(self, sexo):        
        genero = ('Masculino','Femenino')
        if sexo == "M":
            return genero[0]
        elif sexo == "F":
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

    def __init__(self, dni, nombre, apellido, anioNacimiento, sexo, carrera, lugarDeEstudio):

        # Invoca al constructor de clase Persona
        Persona.__init__(self, dni, nombre, apellido, anioNacimiento, sexo)

        # Nuevos atributos
        self.carrera = carrera
        self.lugarDeEstudio = lugarDeEstudio


    def mostrarDatos(self):
        return "Estudiante:" +self.nombre+", "+self.apellido+", carrera:" +self.carrera+", lugar De Estudio:" +self.lugarDeEstudio+"."

persona1 = Persona(12345678, "Leonardo", "Caballero", 1992, "M")

print(persona1.getGenero(persona1.sexo))

estudiante1 = estudiante("11234567", "Jen", "Paz", 1968, "M", "compu", "ispc")

print(estudiante1.getGeneracion(estudiante1.anioNacimiento))

print(estudiante1.mostrarDatos())