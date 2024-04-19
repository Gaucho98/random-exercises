# Desarrollar una función para crear una matriz de MxN. La función recibe M y N por parámetro, la rellena con valores al
# azar entre A y B (también recibidos por parámetro) y retorna la matriz creada. Si no hay valores entre A y B o alguna
# de las dimensiones es negativa se deberá retornar la matriz vacía. Desarrollar también un pequeño programa principal para
# invocar a la función y mostrar la matriz por pantalla. Además mostrar la suma de cada fila y cada columna.

import random

def cargar_matriz(m,n,a,b):
    matriz = []
    
    for i in range(m):
        matriz.append([])
        for j in range(n):
            valor = random.randint(a,b)
            if a == b or a < 0 or b < 0:
                matriz[i].append(".")
            else:
                matriz[i].append(valor)
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="  ")
        print("\n")
        
def suma_filas(matriz):
    suma = []
    
    for i in range(len(matriz)):
        suma_filas = 0
        for j in range(len(matriz[i])):
            suma_filas += matriz[i][j]
        suma.append(suma_filas)
    print("Suma filas: ", suma)
    
def suma_columnas(matriz):
    suma = []
    
    for i in range(len(matriz)):
        suma_columnas = 0
        for j in range(len(matriz[i])):
            suma_columnas += matriz[j][i]
        suma.append(suma_columnas)
    print("Suma columnas: ", suma)

def main():
    m = int(input("Filas: "))
    n = int(input("Columnas: "))
    a = int(input("A: "))
    b = int(input("B: "))
    matriz = cargar_matriz(m,n,a,b)
    imprimir_matriz(matriz)
    suma_filas(matriz)
    suma_columnas(matriz)
    
main()