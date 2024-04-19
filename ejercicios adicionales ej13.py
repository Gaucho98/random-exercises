# Desarrollar un programa para crear una lista con números al azar entre 1 y 20. Finalizar la carga al crear el número
# cero y contemplar además que la lista debe tener al menos 10 elementos cargados. Mostrar la lista por pantalla. Luego
# se pide: Informar cuántos números NO están repetidos. Desarrollar una función que reciba la lista y retorna cuántos
# números únicos hay en la lista.

import random

def cargar_lista():
    lista = []
    i = 0
    
    valor = random.randint(0,20)
    while valor != 0 or i < 10:
            lista.append(valor)
            valor = random.randint(0,20)
            i += 1
            
    return lista

def repetidos(lista):
    lista2 = []
    
    for i in range(len(lista)):
        if lista[i] not in lista2:
            lista2.append(lista[i])
    
    j = len(lista2)
    
    return j

def main():
    lista = cargar_lista()
    print("Lista: ",lista)
    no_repetidos = repetidos(lista)
    print("Cantidad de numeros NO repetidos: ",no_repetidos)
    
main()