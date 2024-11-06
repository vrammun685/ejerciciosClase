#Iniciamos una lista de estuciantes 
Estudiantes={}

#Creamos una funcion para que introduzca la opción
def perdiropción():
    opcion= int(input("Elige una opción del menú: "))
    return opcion

#Se va a crear un menu con las distintas opciones
def muestramenu():
    print("Elige una opción del menu de opciones")
    print("1. Agregar un Estudiante")
    print("2. Ver Lista de Estudiantes")
    print("3. Buscar Estudiante")
    print("4. Eliminar Estudiante")
    print("5. Cargar datos")
    print("6. Guardar datos")
    print("7. Salir del Programa")

def comprobaropcion(opcion):
    if opcion<1 or opcion>7:
        print("Opcion erronea")
        exit

def añadirAlumno():
    nombre=str(input("Nombre del alumno: "))
    edad=int(input("Dame su edad: "))
    Estudiantes[nombre]=edad
    print("Estudiante añadido")

def verLista():
    for clave, valor in Estudiantes.items():
        print("Nombre: "+clave+ " Edad: "+str(valor))

def buscarAlumno():
    nombre=str(input("Alumno a buscar: "))
    if (nombre in Estudiantes.keys):
        print("Nombre : "+nombre+ " Edad: "+str(Estudiantes[nombre]))
    else:
        print ("Alumno no encontrado")
    
def eliminarAlumno():
    nombre = input("Alumno a eliminar \U0001F480: ")
    try:
        del Estudiantes[nombre]
        print("El alumno " + nombre + " ha sido eliminado.")
        verLista()
    except KeyError:
        print("Error: El alumno " + nombre + " no se encontró en la lista.")

def cargarDatos():
    fichero= open("estudiantes.txt", "r")
    for linea in fichero:
        nombre, edad=linea.strip().split("-")
        Estudiantes[nombre]=edad
    print("EstudianteS Cargados")

def guardarDatos():
    fichero= open("estudiantes.txt", "w")
    for nombre in Estudiantes:
        fichero.write(nombre+" - "+str(Estudiantes[nombre])+"\n")
    fichero.close()


#Programa principal
muestramenu()
opcion=perdiropción()
comprobaropcion(opcion)
while opcion >= 1 and opcion<=7:
    if opcion ==1:
        añadirAlumno()
    elif opcion==2:
        verLista()
    elif opcion==3:
        buscarAlumno()
    elif opcion==4:
        eliminarAlumno()
    elif opcion==5:
        cargarDatos()
    elif opcion==6:
        guardarDatos()
    else:
        print("Saliendo del programa")
        exit()
    muestramenu()
    opcion=perdiropción()
    comprobaropcion(opcion)

