# Utilizando la función creada en el ejercicio anterior, desarrollar un programa para crear dos matrices de 3x3
# con valores al azar entre dos números ingresados por teclado. Verificar que el rango sea válido, en caso contrario
# solicitar nuevamente ambos valores. Construir una nueva matriz donde cada elemento se obtenga como resultado de sumar
# los elementos correspondientes en las matrices originales. Mostrar todas las matrices y el total obtenido.

# (verificar que a != b y que no sea negativo)

import random

def cargar_matriz():
    matriz = []
    
    a = int(input("Ingrese A: "))
    while a < 0:
        a = int(input("Valor fuera de rango, ingrese A nuevamente: "))
    
    b = int(input("Ingrese B: "))
    while b < 0:
        b = int(input("Valor fuera de rango, ingrese B nuevamente: "))
            
    while a == b:
        print("Valores iguales")
        a = int(input("Ingrese A nuevamente: "))
        b = int(input("Ingrese B nuevamente: "))
        
    for i in range(3):
        matriz.append([])
        for j in range(3):
            valor = random.randint(a,b)
            matriz[i].append(valor)
    return matriz

def imprimir_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end="  ")
        print("\n")
        
def suma_matrices(matriz1,matriz2):
    matrizSuma = []
    
    for i in range(len(matriz1)):
        fila = []
        for j in range(len(matriz1[i])):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        matrizSuma.append(fila)
    return matrizSuma

def main():
    matriz1 = cargar_matriz()
    matriz2 = cargar_matriz()
    print("Matriz 1: ")
    imprimir_matriz(matriz1)
    print("Matriz 2: ")
    imprimir_matriz(matriz2)
    suma = suma_matrices(matriz1,matriz2)
    print("Suma: ")
    imprimir_matriz(suma)
    
main()