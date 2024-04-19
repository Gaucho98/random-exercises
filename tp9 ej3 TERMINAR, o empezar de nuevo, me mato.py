# Hora de jugar: Desarrollar un programa que genere un número entero al azar de cuatro cifras y le proponga al usuario
# que lo descubra, ingresando valores repetidamente hasta hallarlo. En cada intento el programa mostrará mensajes
# indicando si el número ingresado es mayor o menor que el valor secreto. Permitir que el usuario abandone la partida
# al ingresar -1. Al terminar el juego informar la cantidad de intentos realizada, haciendo que el usuario ingrese su
# número de documento si mejoró la mejor marca de intentos obtenida hasta el momento. Luego mostrar la lista ordenada de
# los 5 mejores puntajes (indicando también a quién pertenecen) y preguntar si se desea jugar otra vez, reiniciando el juego
# en caso afirmativo

import random

def juego_main(numero_descubrir):
    lista_intentos = [1]
    intentos = 0
    
    numero = int(input("Ingrese un numero: "))
    while numero != -1:
        if numero < numero_descubrir:
            numero = int(input("El numero a descubrir es MAYOR: "))
            intentos += 1
        elif numero > numero_descubrir:
            numero = int(input("El numero a descubrir es MENOR: "))
            intentos += 1
        else:
            intentos += 1
            lista_intentos.append(intentos)
            return("Encontraste el numero!"),intentos,lista_intentos

def ingreso_documento(intentos,lista_intentos):
    lista_docu = []
    
    for i in range(len(lista_intentos)):
        if intentos < lista_intentos[i]:
            docu = int(input("Ingrese su documento: "))
            lista_docu.append(docu)
            
    del(lista_intentos[0])
    return lista_docu

def ordenamiento(lista_intentos,lista_docu):
    length = len(lista_intentos)-1
    f = True
    
    while f:
        f = False
        for i in range(length):
            for j in range(length):
                if lista_intentos[i] > lista_intentos[i+1]:
                    aux = lista_intentos[i]
                    lista_intentos[i] = lista_intentos[i+1]
                    lista_intentos[i+1] = aux
                    aux = lista_docu[i]
                    lista_docu[i] = lista_docu[i+1]
                    lista_docu[i+1] = aux
                    f = True
    return lista_intentos,lista_docu

def impresion(lista_intentos_ordenada,lista_docu_ordenada):
    for i in range(len(lista_intentos_ordenada)):
#         print("El documento ", lista_docu_ordenada[i],"tuvo ",lista_intentos_ordenada[i], "intentos")
        print("Intentos: "lista_intentos_ordenada)
        print("Documentos: "lista_docu_ordenada)
    
def jugar_denuevo():
    jugar = input("Desea jugar de nuevo? Y o N: ")
    while jugar != "Y" and jugar != "N":
        jugar = input("Respuesta invalida, solo se acepta Y o N:")
    if jugar == "Y" or jugar == "y":
        return True
    elif jugar == "N" or jugar == "n":
        return False 
    
def main():
    print("Descubra el numero! ")
    numero_descubrir = random.randint(0,10)
    mensaje,intentos,lista_intentos = juego_main(numero_descubrir)
    print(mensaje)
    lista_docu = ingreso_documento(intentos,lista_intentos)
    lista_intentos_ordenada,lista_docu_ordenada = ordenamiento(lista_intentos,lista_docu)
    jugar = jugar_denuevo()
    if jugar == True:
        main()
    impresion(lista_intentos_ordenada,lista_docu_ordenada)
    
main()