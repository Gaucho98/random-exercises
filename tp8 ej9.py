# Generar una matriz cuadrada de NxN con números al azar entre 0 y 99. Luego crear una lista que contenga la suma de cada una
# de las filas de la matriz, sin valores repetidos. Es decir que si dos filas suman igual, el valor debe estar una sola vez en
# la lista. Mostrar por pantalla la matriz y la lista. Esta última debe ordenarse de menor a mayor.

import random

def cargar_lista(n):
    matriz = []
    
    for i in range(n):
        matriz.append([])
        for j in range(n):
            valor = random.randint(0,5)
            matriz[i].append(valor)
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="  ")
        print("\n")
        
def sumar_filas(matriz):
    lista_suma = []
    
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[i])):
            suma += matriz[i][j]
        lista_suma.append(suma)
    return lista_suma

def eliminar_repetidos(sumas):
    sumas2 = []
    
    for i in range(len(sumas)):
        if sumas[i] not in sumas2:
            sumas2.append(sumas[i])
            
    return sumas2
            
def ordenar_lista(lista_sin_repetidos):
    flag = True
    
    while flag:
        flag = False
        for i in range(len(lista_sin_repetidos)-1):
            if lista_sin_repetidos[i] > lista_sin_repetidos[i+1]:
                aux = lista_sin_repetidos[i]
                lista_sin_repetidos[i] = lista_sin_repetidos[i+1]
                lista_sin_repetidos[i+1] = aux
                flag = True
                
    return lista_sin_repetidos
        
def main():
    n = int(input("N: "))
    matriz = cargar_lista(n)
    imprimir_matriz(matriz)
    sumas = sumar_filas(matriz)
    lista_sin_repetidos = eliminar_repetidos(sumas)
    lista_ordenada = ordenar_lista(lista_sin_repetidos)
    print("Suma filas sin repetir, ordenadas de menor a mayor: ",lista_ordenada)
    
main()