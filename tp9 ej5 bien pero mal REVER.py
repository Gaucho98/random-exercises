# Ingresar por teclado un número N y construir una lista llamada SECUENCIAS con N números enteros al azar entre 1 y 20.
# Esta lista se caracterizará porque sus valores deben encontrarse divididos en secuencias de números separadas por ceros,
# cuya suma no sea mayor que 20. Para eso se deberá agregar un elemento de valor 0 a fin de separar cada secuencia de
# la siguiente, cuidando que ninguna secuencia sume más de 20. Agregar un 0 adicional al final de la lista y
# mostrar la lista obtenida por pantalla.
#  5 2 9   0   6 4   0   15 3   0   19   0   12 1 5   0


import random

def cargar_lista(n):
    secuencias = []
    acumulador = 0
    j = 0
    
    for i in range(n):
        valor = random.randint(1,20)
        secuencias.append(valor)
        acumulador += secuencias[i]
        j += 1
        while acumulador > 20:
            secuencias.insert(j-1,0)
            acumulador = 0
    secuencias.append(0)
        
    return secuencias

def main():
    n = int(input("Ingrese N: "))
    lista = cargar_lista(n)
    print(lista)
    
main()