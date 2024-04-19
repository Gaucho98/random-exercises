# Generar una matriz cuadrada de NxN. Informar cuál es la suma de los elementos ubicados en el triángulo superior de la
# misma.

import random

def cargar_matriz(n):
    matriz = []
    
    for i in range(n):
        matriz.append([])
        for j in range(n):
            valor = random.randint(0,10)
            matriz[i].append(valor)
    return matriz

def imprimir_matriz(lamatriz):
    for i in range(len(lamatriz)):
        for j in range(len(lamatriz[i])):
            print(lamatriz[i][j], end="   ")
        print("\n")
        
def sumar_triangulo_sup(lamatriz):
    suma = 0
    
    for i in range(len(lamatriz)):
        for j in range(len(lamatriz[i])):
            if i < j:
                suma += lamatriz[i][j]
    return suma
            
def main():
    n = int(input("Ingrese N: "))
    lamatriz = cargar_matriz(n)
    imprimir_matriz(lamatriz)
    suma = sumar_triangulo_sup(lamatriz)
    print(suma)
    
main()