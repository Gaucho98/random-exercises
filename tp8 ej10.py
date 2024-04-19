# Ingresar valores desde el teclado en una matriz de MxN y mostrar la matriz creada. Ordenar cada una de las filas utilizando
# los distintos métodos de ordenamiento estudiados. Mostrar nuevamente la matriz.

import random

def cargar_matriz(m,n):
    matriz = []
    
    for i in range(m):
        matriz.append([])
        for j in range(n):
            valor = int(input("Ingrese un numero: "))
            matriz[i].append(valor)
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="  ")
        print("\n")
        
def ordenar_matriz(matriz):
    for fila in matriz:
        for i in range(len(fila)-1):
            for j in range(len(fila)-i-1):
                if fila[j] > fila[j+1]:
                    aux = fila[j]
                    fila[j] = fila[j+1]
                    fila[j+1] = aux
                
def main():
    m = int(input("M: "))
    n = int(input("N: "))
    matriz = cargar_matriz(m,n)
    print("Matriz original: ")
    imprimir_matriz(matriz)
    print("Matriz con filas ordenadas: ")
    filas_ordenadas = ordenar_matriz(matriz)
    imprimir_matriz(matriz)
    
main()