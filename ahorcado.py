#Importamos todo lo necesario para crear numeros random
import random
#Creamos una lista de palabras para ver si juegan 1 o 2 personas
listaPalabras=["MARACUYA","SINFONIA","BISIESTO","PANDERO","PROGRAMA","SIESTA","ANARQUIA","SOCIALISMO","TELEFONO","PAJARO","PENDIENTES","MONEDERO","ESPADA","DIAFRAGMA","CAPITALISMO","SUPERMAN","LAMPARA","COMIC","AUTOBUS","DECEPCION"]

#Primero vamos a ver si el numero de jugadires es correcto
jugadores=int(input("Cuantos jugadores sois: "))
while jugadores!=1 and jugadores!=2:
    print("Numero de jugadores incorrecto\nDebe ser un 1 o 2 jugadores")
    jugadores=int(input("Cuantos jugadores sois: "))


#Acontinuación vemos  cuantos son los jugadores si 1 o 2
if jugadores==1:
    #vamos a hacer una seleccion atleatoria de la palabra
    numero = random.randint(0, 20)
    palabra=listaPalabras[numero]
    nletras = len(palabra)
    # Creamos una lista para almacenar el progreso del jugador (guiones bajos al principio)
    progreso = [" _ "] * nletras
    for i in range(nletras):
        print(" _ ",end="")

    # Pedimos la primera letra al usuario
    l = str(input("\nDame una letra: "))
    letra = l.upper()

    #Repetimos la entrada de datos hasta que nos devuelva un 0
    conterrores=0
    contaciertos=0

    while conterrores <8 and contaciertos<nletras:  
        #Creamos un booleano para saber si acerto
        acerto=False
        # Recorremos la palabra para verificar si la letra coincide
        for indice, var in enumerate(palabra):  # Usamos enumerate para obtener tanto el índice como la letra
            if var == letra:
                # Si la letra coincide, la guardamos en la posición correspondiente del progreso y subimos el contador de aciertos
                progreso[indice] = " " + letra + " "
                acerto=True
                contaciertos+=1
                if contaciertos==nletras:
                    print("Acertaste la Palaba, ENHORABUENA")
                    exit()

        if conterrores==0 and acerto==False:
            #Imprimimos el muñeco
            print("Letra equivocada")
            print("|___________")
            conterrores+=1
        elif conterrores==1 and acerto==False:
            print("Letra equivocada")
            print("|       ")
            print("|       ")
            print("|")
            print("|")
            print("|")
            print("|___________")
            conterrores+=1
        elif conterrores==2 and acerto==False:
            print("Letra equivocada")
            print("_________")
            print("|       |")
            print("|       ")
            print("|")
            print("|")
            print("|")
            print("|___________")
            conterrores+=1
        elif conterrores==3 and acerto==False:
            print("Letra equivocada")
            print("_________")
            print("|       |")
            print("|       O ")
            print("|")
            print("|")
            print("|")
            print("|___________")
            conterrores+=1
        elif conterrores==4 and acerto==False:
            print("Letra equivocada")
            print("_________")
            print("|       |")
            print("|       O ")
            print("|       |")
            print("|")
            print("|")
            print("|___________")
            conterrores+=1
        elif conterrores==5 and acerto==False:
            print("Letra equivocada")
            print("_________")
            print("|       |")
            print("|       O ")
            print("|      /|\\")
            print("|")
            print("|")
            print("|___________")
            conterrores+=1
        elif conterrores==6 and acerto==False:
            print("Letra equivocada")
            print("_________")
            print("|       |")
            print("|       O ")
            print("|      /|\\")
            print("|      / \\")
            print("|")
            print("|___________")
            conterrores+=1  
        elif conterrores==7 and acerto==False:
            print("Letra equivocada")
            print("__________")
            print("|        |")
            print("|       \U0001F480  ")
            print("|")
            print("|")
            print("|")
            print("|___________")    
            print("HAS MUERTO, FIN DEL JUEGO")
            print("La palabra era: "+palabra)    
            exit()
            conterrores+=1
        # Mostramos el progreso actual
        print("".join(progreso))  # "".join(progreso) convierte la lista en una cadena

        # Pedimos otra letra al final del ciclo
        l = str(input("Dame una letra: "))  # Pedimos otra letra
        letra = l.upper()
else:
    #introducimos la palabra que tiene que adivinar el compañero
    p=str(input("Dame la palabra sin que el rival la vea.\n"))
    
    palabra=p.upper()
    nletras = len(palabra)
    # Creamos una lista para almacenar el progreso del jugador (guiones bajos al principio)
    progreso = [" _ "] * nletras
    for i in range(nletras):
        print(" _ ",end="")

    # Pedimos la primera letra al usuario
    l = str(input("\nDame una letra: "))
    letra = l.upper()

    #Repetimos la entrada de datos hasta que nos devuelva un 0
    conterrores=0
    contaciertos=0

    while conterrores <8 and contaciertos<nletras:  
        #Creamos un booleano para saber si acerto
        acerto=False
        # Recorremos la palabra para verificar si la letra coincide
        for indice, var in enumerate(palabra):  # Usamos enumerate para obtener tanto el índice como la letra
            if var == letra:
                # Si la letra coincide, la guardamos en la posición correspondiente del progreso y subimos el contador de aciertos
                progreso[indice] = " " + letra + " "
                acerto=True
                contaciertos+=1
                if contaciertos==nletras:
                    print("Acertaste la Palaba, ENHORABUENA")
                    exit()

        if conterrores==0 and acerto==False:
            #Imprimimos el muñeco
            print("Letra equivocada")
            print("|___________")
            conterrores+=1
        elif conterrores==1 and acerto==False:
            print("Letra equivocada")
            print("|       ")
            print("|       ")
            print("|")
            print("|")
            print("|")
            print("|___________")
            conterrores+=1
        elif conterrores==2 and acerto==False:
            print("Letra equivocada")
            print("_________")
            print("|       |")
            print("|       ")
            print("|")
            print("|")
            print("|")
            print("|___________")
            conterrores+=1
        elif conterrores==3 and acerto==False:
            print("Letra equivocada")
            print("_________")
            print("|       |")
            print("|       O ")
            print("|")
            print("|")
            print("|")
            print("|___________")
            conterrores+=1
        elif conterrores==4 and acerto==False:
            print("Letra equivocada")
            print("_________")
            print("|       |")
            print("|       O ")
            print("|       |")
            print("|")
            print("|")
            print("|___________")
            conterrores+=1
        elif conterrores==5 and acerto==False:
            print("Letra equivocada")
            print("_________")
            print("|       |")
            print("|       O ")
            print("|      /|\\")
            print("|")
            print("|")
            print("|___________")
            conterrores+=1
        elif conterrores==6 and acerto==False:
            print("Letra equivocada")
            print("_________")
            print("|       |")
            print("|       O ")
            print("|      /|\\")
            print("|      / \\")
            print("|")
            print("|___________")
            conterrores+=1  
        elif conterrores==7 and acerto==False:
            print("Letra equivocada")
            print("__________")
            print("|        |")
            print("|       \U0001F480  ")
            print("|")
            print("|")
            print("|")
            print("|___________")    
            print("HAS MUERTO, FIN DEL JUEGO")
            print("La palabra era: "+palabra)    
            exit()
            conterrores+=1
        # Mostramos el progreso actual
        print("".join(progreso))  # "".join(progreso) convierte la lista en una cadena

        # Pedimos otra letra al final del ciclo
        l = str(input("Dame una letra: "))  # Pedimos otra letra
        letra = l.upper()