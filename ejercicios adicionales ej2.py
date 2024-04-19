# Llenar una lista con números enteros (números positivos o negativos). Mostrar la cantidad de números
# positivos y la cantidad de números negativos que hay en dicha lista.

import random

def cargar_lista(n):
    lista = []
    
    for i in range(n):
        valor = random.randint(-10,10)
        lista.append(valor)
        
    return lista

def positivos_negativos(lista):
    negativo = 0
    positivo = 0
    
    for i in range(len(lista)):
        if lista[i] < 0:
            negativo += 1
        elif lista[i] >= 0:
            positivo += 1
            
    return negativo,positivo
    
def main():
    n = int(input("N: "))
    lista = cargar_lista(n)
    print(lista)
    negativos,positivos = positivos_negativos(lista)
    print("La cantidad de numeros negativos es: ",negativos)
    print("La cantidad de numeros positivos es: ",positivos)
    
main()