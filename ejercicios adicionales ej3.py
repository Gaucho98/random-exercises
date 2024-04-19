# Cargar una lista con números aleatorios y reemplazar un valor en una posición determinada por el
# usuario.

import random

def cargar_lista(n):
    lista = []
    
    for i in range(n):
        valor = random.randint(1,100)
        lista.append(valor)
        
    return lista

def reemplazar_valor(lista,pos_change,num_change):
    lista.insert(pos_change,num_change)
    del(lista[pos_change+1])
    
    return lista
    

def main():
    n = int(input("Cantidad de numeros en lista: "))
    lista = cargar_lista(n)
    print("Lista: ",lista)
    pos_change = int(input("Ingrese la posicion a reemplazar: "))
    num_change = int(input("Ingrese el numero reemplazar: "))
    lista_nueva = reemplazar_valor(lista,pos_change,num_change)
    print("Lista con valor reemplazado: ",lista_nueva)
    
main()