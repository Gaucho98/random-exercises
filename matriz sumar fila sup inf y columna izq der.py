# crear una matriz de NxN y sumar la fila superior, luego la fila inferior, luego la columna izq y luego la derecha.

import random

def crear_matriz(n):
    matriz = []
    
    for i in range(n):
        matriz.append([])
        for j in range(n):
            valor = random.randint(0,9)
            matriz[i].append(valor)
    
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="  ")
        print("\n")
        
def sumar_fila_superior(matriz):
    suma = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == 0:
                suma += matriz[i][j]
                
    return suma

def sumar_fila_inferior(matriz,n):
    suma = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == n-1:
                suma += matriz[i][j]
                
    return suma

def sumar_columna_izquierda(matriz):
    suma = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == 0:
                suma += matriz[i][j]
                
    return suma

def sumar_columna_derecha(matriz,n):
    suma = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j == n-1:
                suma += matriz[i][j]
                
    return suma
                
def main():
    n = int(input("N: "))
    matriz = crear_matriz(n)
    imprimir_matriz(matriz)
    suma_filaSup = sumar_fila_superior(matriz)
    print("Fila superior: ",suma_filaSup)
    suma_filaInf = sumar_fila_inferior(matriz,n)
    print("Fila inferior: ",suma_filaInf)
    suma_columnaIzq = sumar_columna_izquierda(matriz)
    print("Columna izquierda: ",suma_columnaIzq)
    suma_columnaDer = sumar_columna_derecha(matriz,n)
    print("Columna derecha: ",suma_columnaDer)
    
main()