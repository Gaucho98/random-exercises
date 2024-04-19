# Cargar dos listas de números A y B con N números al azar entre 1 y 100, donde N se ingresa por teclado.
# Mostrar ambas listas por pantalla. Luego construir e imprimir tres nuevas listas C, D y E que contengan:
#     • La concatenación de los valores pares de A con los impares de B. (valores pares o valores impares se refiere a
#       los elementos propiamente dichos y no a sus posiciones).
#     • La concatenación de los valores impares de A con el reverso de los valores pares de B.
#     • La intercalación de los elementos de A y B.

import random

def cargar_listasA_B(n):
    listaA = []
    listaB = []
    
    for i in range(n):
        valor = random.randint(0,100)
        listaA.append(valor)
        
    for i in range(n):
        valor = random.randint(0,100)
        listaB.append(valor)
        
    return listaA,listaB

def cargar_listaC(listaA,listaB):
    listaC = []
    
    for i in range(len(listaA)):
        if listaA[i] % 2 == 0:
            listaC.append(listaA[i])
            
    for j in range(len(listaB)):
        if listaB[j] % 2 == 1:
            listaC.append(listaB[j])
    return listaC

def cargar_listaD(listaA,listaB):
    listaD = []
    listaB.reverse()
    
    for i in range(len(listaA)):
        if listaA[i] % 2 == 1:
            listaD.append(listaA[i])
            
    for j in range(len(listaB)):
        if listaB[j] % 2 == 0:
            listaD.append(listaB[j])
            
    return listaD

def cargar_listaE(listaA,listaB):
    listaE = []
    listaB.reverse()
    
    for i, listaB in zip(listaA,listaB):
        listaE.append(i)
        listaE.append(listaB)
        
    return listaE

def main():
    n = int(input("Ingrese la cantidad de numeros: "))
    listaA,listaB = cargar_listasA_B(n)
    print("Lista A: ", listaA)
    print("Lista B: ", listaB)
    listaC = cargar_listaC(listaA,listaB)
    print("Lista C: ", listaC)
    listaD = cargar_listaD(listaA,listaB)
    print("Lista D: ", listaD)
    listaE = cargar_listaE(listaA,listaB)
    print("Lista E: ", listaE)
    
main()