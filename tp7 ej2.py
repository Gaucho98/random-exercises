# Calcular la suma de los números de la lista.

import random

def cargar_lista(n):
    lista = []
    
    for i in range(n):
        valor = random.randint(1,10)
        lista.append(valor)
    return lista

def sumar_lista(lalista):
    acumulador = 0
    
    for i in range(len(lalista)):
        acumulador += lalista[i]
    return acumulador

def main():
    n = int(input("Ingrese la cantidad de numeros de la lista: "))
    lalista = cargar_lista(n)
    print(lalista)
    suma = sumar_lista(lalista)
    print(suma)
    
main()