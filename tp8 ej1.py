# Crear una matriz de 3x4 (3 filas y 4 columnas) con valores obtenidos al azar entre 1 y 10. Mostrar la matriz por
# pantalla respetando el formato de 3 filas y 4 columnas.

import random

def cargar_matriz(n,m):
    matriz = []
    
    for i in range(n):
        matriz.append([])
        for j in range(m):
            valor = random.randint(1,10)
            matriz[i].append(valor)
    return matriz
                       
def imprimir_matriz(lamatriz):
    for i in range(len(lamatriz)):
        for j in range(len(lamatriz[i])):
            print(lamatriz[i][j], end="  ")
        print("\n")
    
def main():
    n = int(input("Ingrese la cantidad de filas: "))
    m = int(input("Ingrese la cantidad de columnas: "))
    lamatriz = cargar_matriz(n,m)
    imprimir_matriz(lamatriz)
    
main()