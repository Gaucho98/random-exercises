# Crear una lista de N números generados al azar entre 0 y 100 pero sin elementos repetidos. El valor de N se ingresa por
# teclado. Resolver este problema utilizando dos estrategias distintas:
#     • Impidiendo el agregado de elementos repetidos
#     • Eliminando los duplicados luego de generar la lista. Asegurarse que la cantidad final de elementos sea la solicitada

import random

def buscar_en_lista(lista,valor):
    for i in range(len(lista)):
        if valor == lista[i]:
            return True
    return False

def cargar_lista(n):
    lista = []
    
    for i in range(n):
        valor = random.randint(0,100)
        
        while buscar_en_lista(lista,valor):
            valor = random.randint(0,100)
        lista.append(valor)
        
    return lista,valor
    

def main():
    n = int(input("N: "))
    lista,valor = cargar_lista(n)
    buscar_en_lista(lista,valor)
    print(lista)
    
main()