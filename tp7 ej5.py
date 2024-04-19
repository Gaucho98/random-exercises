# Desarrollar una función que reciba la lista como parámetro y devuelva una nueva lista con los mismos elementos de la
# primera, pero en orden inverso. Por ejemplo, si la función recibe [5, 7, 1] debe devolver [1, 7, 5].

import random

def cargar_lista(n):
    lista = []
    
    for i in range(n):
        valor = random.randint(0,9)
        lista.append(valor)
    return lista

def dar_vuelta_lista(lista):
    lista_dada_vuelta = list(reversed(lista))
    
    return lista_dada_vuelta
    
def main():
    n = int(input("Ingrese la candidad de numeros de la lista: "))
    lista = cargar_lista(n)
    print("Lista original: ", lista)
    lista_vuelta = dar_vuelta_lista(lista)
    print("Lista dada vuelta: ", lista_vuelta)
    
main()