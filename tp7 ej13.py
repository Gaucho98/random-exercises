# Leer dos listas de números M y N y ordenarlas de menor a mayor. Luego se solicita generar e imprimir una tercera
# lista que resulte de intercalar los elementos de M y N. La nueva lista también debe quedar ordenada, sin utilizar
# ningún método de ordenamiento en ella

import random

def cargar_listas(n,m):
    listaN = []
    listaM = []
    
    for i in range(n):
        valor = random.randint(0,100)
        listaN.append(valor)
    
    for i in range(m):
        valor = random.randint(0,100)
        listaM.append(valor)
        
    return listaN,listaM

def ordenar_listaN(listaN):
    flags = True
    
    while flags:
        flags = False
        for i in range(len(listaN)-1):
            if listaN[i] > listaN[i+1]:
                aux = listaN[i]
                listaN[i] = listaN[i+1]
                listaN[i+1] = aux
                flags = True
    return listaN

def ordenar_listaM(listaM):
    flags = True
    
    while flags:
        flags = False
        for i in range(len(listaM)-1):
            if listaM[i] > listaM[i+1]:
                aux = listaM[i]
                listaM[i] = listaM[i+1]
                listaM[i+1] = aux
                flags = True
    return listaM

def intercalar_listas(listaN,listaM):
    listaI = []
    i = 0
    j = 0
    
    while i < len(listaN) and j < len(listaM):
        if listaN[i] <= listaM[j]:
            listaI.append(listaN[i])
            i += 1
        else:
            listaI.append(listaM[j])
            j += 1
        
    return listaI
        
def main():
    n = int(input("Ingrese la cantidad de numeros de lista N: "))
    m = int(input("Ingrese la cantidad de numeros de lista M: "))
    listaN,listaM = cargar_listas(n,m)
    print("Lista N original: ", listaN)
    print("Lista M original: ", listaM)
    listaN = ordenar_listaN(listaN)
    print("Lista N ordenada: ", listaN)
    listaM = ordenar_listaM(listaM)
    print("Lista M ordenada: ", listaM)
    listaI = intercalar_listas(listaN,listaM)
    print("Listas intercaladas: ", listaI)
    
main()