# Escribir una función para ingresar desde el teclado una serie de números entre A y B y guardarlos en una lista.
# En caso de ingresar un valor fuera de rango la función mostrará un mensaje de error y solicitará un nuevo número.
# Para finalizar la carga se deberá ingresar -1. La función recibe como parámetros los valores de A y B, y devuelve
# la lista cargada (o vacía, si el usuario no ingresó nada) como valor de retorno. Tener en cuenta que A puede ser mayor,
# menor o igual a B.

def cargar_lista(a,b):
    lista = []
    
    numero = int(input("Ingrese un numero: "))
    while numero != -1:
        if a < b:
            while numero < a or numero > b:
                numero = int(input("Valor fuera de rango: "))
        elif a > b:
            while numero > a or numero < b:
                numero = int(input("Valor fuera de rango: "))
        elif a == b:
            while numero != a:
                numero = int(input("Valor fuera de rango: "))
        lista.append(numero)
        numero = int(input("Ingrese un numero: "))
    return lista

def main():
    a = int(input("Ingrese A: "))
    b = int(input("Ingrese B: "))
    lalista = cargar_lista(a,b)
    print(lalista)
    
main()