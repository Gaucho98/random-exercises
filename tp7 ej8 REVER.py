# Rellenar una lista con números enteros entre 0 y 100 obtenidos al azar e imprimir el valor mínimo y el lugar que ocupa.
# Tener en cuenta que el mínimo puede estar repetido, en cuyo caso deberán mostrarse todas las posiciones en las que se
# encuentre. La carga de datos termina cuando se obtenga un 0 como número al azar, el que no deberá cargarse en la lista.

import random

def cargar_lista(n):
    lista = []
    valor = random.randint(0,100)
    
    for i in range(n):
        while valor != 0:
            lista.append(valor)
            valor = random.randint(0,100)
        
    return lista

def encontrar_minimo(lista):
    minimo = lista[0]
    maximo = lista[0]
    
    for i in lista:
        if i < minimo:
            minimo = i
            
    print(minimo)
    
    target = minimo
    
    for i in range(len(lista)):
        if lista[i] == target:
            print(i)
        
def main():
    n = int(input("Ingrese la cantidad de numeros en lista: "))
    lista = cargar_lista(n)
    print(lista)
    minimo = encontrar_minimo(lista)
    
main()