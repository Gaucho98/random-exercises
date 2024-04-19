# Escribir la función comparar(a, b) que reciba como parámetros dos números enteros y devuelva 1 si el primero es mayor
# que el segundo, 0 si son iguales o -1 si el primero es menor que el segundo. En este ejercicio debe aprovecharse la
# función del ejercicio anterior. Ejemplo: comparar(4, 2) devuelve 1, y comparar(2, 4) devuelve -1.

def signo(a,b):
    if a > b:
        return "1"
    elif a == b:
        return "0"
    else:
        return "-1"

def main():
    a = int(input("A: "))
    b = int(input("B: "))
    res = signo(a,b)
    print(res)
    
main()
