# Eliminar de una lista de números enteros los valores que se encuentren en una segunda lista. Imprimir la lista original,
# la lista de valores a eliminar y la lista resultante. Ambas listas deben rellenarse con números al azar. La cantidad y
# el rango de los valores los decide el programador

import random

def cargar_lista(n,a,b):
    lista = []
    lista2 = []
    
    for i in range(n):
        valor = random.randint(a,b)
        lista.append(valor)
        
    for j in range(n):
        valor = random.randint(a,b)
        lista2.append(valor)
        
    return lista,lista2

def eliminar_repetidos(lista,lista2):
    lista3 = []
    
    for i in range(len(lista)):
        if lista[i] != lista2[i]:
            lista3.append(lista[i])
            
    return lista3

def main():
    n = int(input("Ingrese la cantidad de numeros en lista: "))
    a = int(input("Desde: "))
    b = int(input("Hasta: "))
    lista,lista2 = cargar_lista(n,a,b)
    print("Lista original: ",lista)
    print("Lista de valores a eliminar: ",lista2)
    lista3 = eliminar_repetidos(lista,lista2)
    print("Lista resultante: ",lista3)
    
main()