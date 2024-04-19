# Ingresar un número entero positivo, el que debe ser múltiplo de 4. Luego crear una matriz que contenga 4 elementos
# por fila, hasta completar la cantidad de elementos indicada. Mostrar la matriz e informar cuántas filas se crearon.
# La matriz se rellena con números al azar.

import random

def cargar_matriz():
    matriz = []
    
    n = int(input("Ingrese un numero multiplo de 4: "))
    while (n // 4) == 0:
        n = int(input("El numero no es multiplo de 4 o negativo, intente de nuevo: "))
    
    for i in range(n):
        matriz.append([])
        for j in range(4):
            valor = random.randint(100,999)
            matriz[i].append(valor)
    return matriz, n
            
def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="  ")
        print("\n")

def main():
    matriz, filas = cargar_matriz()
    print("Matriz: ")
    imprimir_matriz(matriz)
    print("Filas: ", filas)
    
main()