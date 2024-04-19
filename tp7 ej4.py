# Escribir una función para contar cuántas veces aparece un valor dentro de la lista. La función recibe como parámetros
# la lista y el valor a buscar, y devuelve un número entero.

import random

def cargar_lista(n):
    lista = []
    
    for i in range(n):
        valor = random.randint(0,10)
        lista.append(valor)
    return lista

def buscar_cantidad_valor(lista,v):
    acumulador = 0
    
    for i in range(len(lista)):
        if lista[i] == v:
            acumulador += 1
    return acumulador

def main():
    n = int(input("Ingrese la cantidad de numeros de lista: "))
    v = int(input("Ingrese el valor a buscar: "))
    lista = cargar_lista(n)
    print(lista)
    cantidad = buscar_cantidad_valor(lista,v)
    print("Cantidad de veces que aparece el valor a buscar: ", cantidad)
    
main()