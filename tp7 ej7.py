# Escribir una función para devolver una lista con todas las posiciones que ocupa un valor pasado como parámetro,
# utilizando búsqueda binaria en una lista desordenada. La función debe devolver una lista vacía si el elemento
# no se encuentra en la lista original.

import random

def cargar_lista(n):
    lista = []
    
    for i in range(n):
        valor = random.randint(0,100)
        lista.append(valor)
    return lista

def ordenar_lista(lista):
    length = len(lista)-1
    flags = True
    
    while flags:
        flags = False
        for i in range(length):
            if lista[i] > lista[i+1]:
                aux = lista[i]
                lista[i] = lista[i+1]
                lista[i+1] = aux
                flags = True
    return lista
        

def busqueda_binaria(lista_ordenada,m):
    lalista = []
    
    inicio = 0
    final = len(lista_ordenada)-1
    
    while inicio <= final:
        medio = (inicio + final) // 2
        if m == lista_ordenada[medio]:
            lalista.append(medio)
            return lalista
        elif m < lista_ordenada[medio]:
            final = medio - 1
        else:
            inicio = medio + 1
    return lalista

def main():
    n = int(input("Ingrese la cantidad de numeros de la lista: "))
    m = int(input("Ingrese el numero a buscar: "))
    lista = cargar_lista(n)
    print(lista)
    lista_ordenada = ordenar_lista(lista)
    print(lista_ordenada)
    valor_buscar = busqueda_binaria(lista_ordenada,m)
    print(valor_buscar)
    
main()