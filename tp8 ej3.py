# Generar una matriz de MxN con valores al azar comprendidos entre A y B. Mostrar la suma de los valores ubicados
# sobre la diagonal principal. Los valores de A y B también se ingresan por teclado.

import random

def cargar_matriz(m,n,a,b):
    matriz = []
    
    for i in range(m):
        matriz.append([])
        for j in range(n):
            valor = random.randint(a,b)
            matriz[i].append(valor)
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="  ")
        print("\n")
        
def suma_diagonal(matriz):
    suma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == j:
                suma += matriz[i][j]
    return suma
    
        
def main():
    m = int(input("Filas: "))
    n = int(input("Columnas: "))
    a = int(input("A: "))
    b = int(input("B: "))
    matriz = cargar_matriz(m,n,a,b)
    imprimir_matriz(matriz)
    suma = suma_diagonal(matriz)
    print(suma)
    
main()