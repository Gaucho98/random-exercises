# Dada una matriz de n*m, obtener la suma de los valores de cada fila e ir guardándolos en una lista.
# Recorrer la lista e informar en que posición se encuentra el mayor valor.

import random

def cargar_matriz(n,m):
    matriz = []
    
    for i in range(n):
        matriz.append([])
        for j in range(m):
            valor = random.randint(0,10)
            matriz[i].append(valor)
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j],end="  ")
        print("\n")

def sumar_filas(matriz):
    lista_suma = []
    
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        lista_suma.append(suma)
    return lista_suma

def mayor_valor(suma):
    maximo = 0
    
    for i in range(len(suma)):
        if suma[i] > maximo:
            maximo = suma[i]
    
    print("Valor maximo: ",maximo)
            
    target = maximo
    
    for j in range(len(suma)):
        if suma[j] == target:
            print("Posicion: ", j)
    
def main():
    n = int(input("N: "))
    m = int(input("M: "))
    matriz = cargar_matriz(n,m)
    imprimir_matriz(matriz)
    suma = sumar_filas(matriz)
    print("Suma de cada fila: ",suma)
    mayor_valor(suma)
    
main()