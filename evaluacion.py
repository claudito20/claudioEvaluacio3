#Desarrolle una aplicación en Python utilizando Visual Studio que permita resolver el siguiente caso:
#La empresa de eSports “eShirlitos”, necesita desarrollar un sistema que permita registrar los puntajes obtenidos por sus competidores en Fortnite, Valorant y Fifa. Para el funcionamiento del sistema se requiere las siguientes funcionalidades
#1.
#Registrar puntajes torneo
#2.
#Listar los todos puntajes
#3.
#Imprimir por Tipo
#4.
#Salir del programa
#1.
#Registrar puntajes torneo
#Para registrar puntajes se requiere lo siguiente: Identificador de Jugador, Nombre y apellido del jugador, juego, puntaje obtenido. Por ejemplo, si el jugador compite en Fortnite y Fifa. Debe permitir seleccionar entre 1 de las 3 opciones e ingresar la cantidad de puntos obtenidos en esos dos juegos, también debe incluir su tipo (Principiante – Avanzado - Experto). Por lo tanto, un detalle de puntos del torneo podría verse registrado de la siguiente manera:
#Id Jugador Nombre VALORANT FORNITE

jugadores = []
id = []
tipodejuego = []
puntajefornite = 12500
puntajefifa = 3500
categoria = []
registrar_puntajes = []
nombre = (input("ingrese su nombre y apellido :"))
id = (input("ingrese su id :"))
categoria=(input("ingrese la categoria de nivel: principiante,avanzado, experto :  "))
tipodejuego = (input("ingrese el tipo de juego que desea  . Fornite o Fifa:"))
tipodejuego =  (puntajefornite)
tipodejuego =(puntajefifa)

print(" hola tienes en el juego" "puntos" , puntajefornite)
print("hola tiene en el juego" , puntajefifa)
tipodejuego = puntajefornite + puntajefifa
totalpuntaje= int (tipodejuego)
print("1. Registrar puntajes torneo")
print("2. Listar los todos puntajes")
print("3.Imprimir por Tipo")
print("4.Salir del programa")

opc = int (input("ingrese la opcion que  desea: "))
if opc == 1:
    print("registra puntajes del torneo: ")
    jugadores()
elif opc == 2:
    print("lista de los  puntajes : ")

elif opc == 3:
    print("imprimir por el tipo: ")
elif opc == 4:
        print("Salir")
else:
     print("opcion no valida ,por favor intentalo denuevo")



