# Determinar si la lista es capicúa (palíndromo). Una lista capicúa se lee de igual modo de izquierda a derecha y de
# derecha a izquierda. Por ejemplo, [2, 7, 7, 2] es capicúa, mientras que [2, 7, 5, 2] no lo es.

# valor = len(lista)-1
# lista.append(valor)

import random

def cargar_lista():
    lista = []
    
    for i in range(4):
        valor = random.randint(0,9)
        lista.append(valor)
    return lista

def dar_vuelta_lista(lista):
    if lista == list(reversed(lista)):
        return "Capicua"
    else:
        return "No capicua"
        

def main():
    lista = cargar_lista()
    print("Lista original: ", lista)
    capicua = dar_vuelta_lista(lista)
    print(capicua)
    
main()
