# Ingresar 20 números e indicar cuales son los 5 mayores.

import random

def cargar_lista():
    lista = []
    
    for i in range(20):
        valor = random.randint(0,100)
        lista.append(valor)
    return lista

def indicar_mayores1(lista):
    maximo = 0
    
    for i in range(len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
            
    print(maximo)        
    lista.remove(maximo)
   
    return lista

def indicar_mayores2(lista1):
    maximo = 0
    
    for j in range(len(lista1)):
        if lista1[j] > maximo:
            maximo = lista1[j]
            
    print(maximo)        
    lista1.remove(maximo)
    
    return lista1

def indicar_mayores3(lista2):
    maximo = 0
    
    for j in range(len(lista2)):
        if lista2[j] > maximo:
            maximo = lista2[j]
            
    print(maximo)        
    lista2.remove(maximo)
    
    return lista2

def indicar_mayores4(lista3):
    maximo = 0
    
    for j in range(len(lista3)):
        if lista3[j] > maximo:
            maximo = lista3[j]
            
    print(maximo)        
    lista3.remove(maximo)
    
    return lista3

def indicar_mayores5(lista4):
    maximo = 0
    
    for j in range(len(lista4)):
        if lista4[j] > maximo:
            maximo = lista4[j]
            
    print(maximo)        
    lista4.remove(maximo)
    
    return lista4
        
def main():
    lista = cargar_lista()
    print(lista)
    lista1 = indicar_mayores1(lista)
    lista2 = indicar_mayores2(lista1)
    lista3 = indicar_mayores3(lista2)
    lista4 = indicar_mayores4(lista3)
    lista5 = indicar_mayores5(lista4)
    
main()