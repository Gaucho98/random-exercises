# pasar los numeros de una matriz a lista

import random

def cargar_matriz(m,n):
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
        
def matriz_a_lista(matriz):
    lista = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            lista.append(matriz[i][j])
    return lista
            
def main():
    m = int(input("M: "))
    n = int(input("N: "))
    matriz = cargar_matriz(m,n)
    print("Matriz: ")
    imprimir_matriz(matriz)
    lista = matriz_a_lista(matriz)
    print("Matriz a lista: ",lista)
    
main()