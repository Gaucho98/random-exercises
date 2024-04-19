# Dada una lista ordenada de números llamada A y un nuevo número N, desarrollar un programa que agregue el elemento N
# dentro de la lista A, respetando el ordenamiento existente. El programa deberá detectar automáticamente si el
# ordenamiento es ascendente o descendente antes de realizar la inserción. No se permite añadir el elemento al final
# y reordenar la lista

# crear lista
# ordenar lista A
# luego pedir numero N
# agregar N a lista A respetando el orden

import random

def cargar_lista(n):
    lista = []
    
    for i in range(n):
        valor = random.randint(0,100)
        lista.append(valor)
    return lista
        
def ordenar_lista(lista):
    flags = True
    
    while flags:
        flags = False
        for i in range(len(lista)-1):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                flags = True
    return lista
        
def insertar_numero(lista_ordenada, num_insert):
    i = 0
    
    while i < len(lista_ordenada) and lista_ordenada[i] < num_insert:
        i += 1
    lista_ordenada.insert(i,num_insert)
        
    return lista_ordenada
    
def main():
    n = int(input("Ingrese la cantidad de numeros en lista: "))
    lista = cargar_lista(n)
    print("Lista: ", lista)
    lista_ordenada = ordenar_lista(lista)
    print("Lista ordenada: ", lista_ordenada)
    num_insert = int(input("Indique el numero a insertar en lista: "))
    lista_ordenada_conN = insertar_numero(lista_ordenada, num_insert)
    print("Lista ordenada con N: ", lista_ordenada_conN)
    
main()