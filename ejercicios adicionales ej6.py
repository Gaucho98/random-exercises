# Eliminar de una lista de números enteros los valores que se encuentren en una segunda lista.
# Mostrar la lista original, la lista de valores a eliminar y como queda la lista original luego de
# eliminar los valores.

import random

def cargar_listas(n):
    lista1 = []
    lista2 = []
    
    for i in range(n):
        valor = random.randint(0,10)
        lista1.append(valor)
        
    for j in range(n):
        valor = random.randint(0,10)
        lista2.append(valor)
        
    return lista1,lista2

def eliminar_repetidos(lista1,lista2):
    lista3 = []
    
    for i in range(len(lista1)):
        if lista1[i] not in lista2:
            lista3.append(lista1[i])
            
    return lista3

def main():
    n = int(input("N: "))
    lista1,lista2 = cargar_listas(n)
    print("Lista original: ",lista1)
    print("Lista de valores a eliminar: ",lista2)
    lista3 = eliminar_repetidos(lista1,lista2)
    print("Lista resultante: ",lista3)
    
main()