import os
import time
import random
from colorama import Fore, Style

# Configuración de colores
red = Fore.RED
verde = Fore.GREEN
amarillo = Fore.YELLOW
azul = Fore.BLUE
cyan = Fore.CYAN
reset = Style.RESET_ALL

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para mostrar el banner
def banner():
    print(azul + """
    __           __            ____                   
   / /_  _______/ /__   ____  / __/                   
  / / / / / ___/ //_/  / __ \/ /_                     
 / / /_/ / /__/ ,<    / /_/ / __/                     
/_/\__,_/\___/_/|_|   \____/_/                  
   __  __                            __               
  / /_/ /_  ___     _______  _______/ /____  ____ ___ 
 / __/ __ \/ _ \   / ___/ / / / ___/ __/ _ \/ __ `__ 
/ /_/ / / /  __/  (__  ) /_/ (__  ) /_/  __/ / / / / /
\__/_/ /_/\___/  /____/\__, /____/\__/\___/_/ /_/ /_/ 
                      /____/   
  """ + reset)

# Función para mostrar el menú
def mostrar_menu():
    print(reset + "")
    print("####################################")
    print("#                                  #")
    print("#            [1] JUGAR             #")
    print("#            " + red + "[2] SALIR" + reset + "             #")
    print("#                                  #")
    print("####################################")
    opcion = input(verde + "  Elige una opción: " + reset)
    return opcion

# Función para cargar preguntas
def cargar_preguntas(ruta_archivo):
    if not os.path.isfile(ruta_archivo):
        print(red + f"Error: No se encontró el archivo en {os.path.abspath(ruta_archivo)}" + reset)
        exit()
    
    preguntas = []
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            pregunta, respuesta = linea.strip().split("|")
            preguntas.append({"pregunta": pregunta, "respuesta": respuesta})
    return preguntas

# Función para iniciar el juego
def jugar():
    limpiar_pantalla()
    mensaje = ("""
    Si juegas es bajo tu responsabilidad, ten en cuenta lo siguiente:

    El juego consta de 20 preguntas, por cada una que
    respondas bien se te dará un premio aleatorio, pero
    así mismo por cada que respondas mal corres el riesgo
    de perder datos de tu dispositivo.

    Para aclarar: no te robamos datos, este script es seguro.
    """)
    for letra in mensaje:
        print(cyan + letra, end="", flush=True)
        time.sleep(0.07)
    time.sleep(3)
    limpiar_pantalla()
    print(amarillo + "\nIniciando..." + reset)
    time.sleep(2)
    limpiar_pantalla()
    
    ruta_archivo = os.path.join(os.path.dirname(__file__), "preguntas.txt")
    preguntas = cargar_preguntas(ruta_archivo)
    preguntas_aleatorias = random.sample(preguntas, min(20, len(preguntas)))
    correctas, incorrectas = 0, 0

    for i, pregunta in enumerate(preguntas_aleatorias, start=1):
        limpiar_pantalla()
        banner()
        print(amarillo + f"\nPregunta {i} de {len(preguntas_aleatorias)}" + reset)
        print(verde + f"Correctas: {correctas}" + reset)
        print(red + f"Incorrectas: {incorrectas}" + reset)
        print("\n" + pregunta["pregunta"])
        respuesta_usuario = input(verde + "\nTu respuesta: " + reset)

        if respuesta_usuario.lower() == pregunta["respuesta"].lower():
            print(verde + "\n¡Correcto!" + reset)
            correctas += 1
        else:
            print(red + f"\n¡Incorrecto! La respuesta correcta es: {pregunta['respuesta']}" + reset)
            incorrectas += 1
        time.sleep(2)
    
    limpiar_pantalla()
    banner()
    print(amarillo + "\nResultado final:" + reset)
    print(verde + f"Correctas: {correctas}" + reset)
    print(red + f"Incorrectas: {incorrectas}" + reset)
    time.sleep(3)

# Función principal
def main():
    limpiar_pantalla()
    print(red + "              JUEGA BAJO TU RESPONSABILIDAD")
    time.sleep(3)
    limpiar_pantalla()
    banner()

    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            jugar()
            limpiar_pantalla()
        elif opcion == "2":
            print(amarillo + "\n  Saliendo del juego..." + reset)
            time.sleep(2)
            break
        else:
            print(red + "\n  Opción inválida. Por favor, elige una opción válida." + reset)
            time.sleep(1.9)
            limpiar_pantalla()
            banner()

main()