# Indicar las coordenadas del mayor valor encontrado en una matriz de MxN, generada con valores aleatorios entre 100 y 1000.

import random

def crear_matriz(m,n):
    matriz = []
    
    for i in range(m):
        matriz.append([])
        for j in range(n):
            valor = random.randint(100,1000)
            matriz[i].append(valor)
    
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="  ")
        print("\n")
        
def coordenadas_maximo(matriz):
    maximo = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maximo:
                maximo = matriz[i][j]
                
    target = maximo
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == target:
                print("Fila:",i,"Columna:",j)
                
    return maximo
                

def main():
    m = int(input("M: "))
    n = int(input("N: "))
    matriz = crear_matriz(m,n)
    imprimir_matriz(matriz)
    maximo = coordenadas_maximo(matriz)
    print("Valor maximo: ",maximo)
    
main()
