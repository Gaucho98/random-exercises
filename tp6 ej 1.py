# Dados dos parámetros enteros A y B, obtener AB (A elevado a la B) mediante multiplicaciones sucesivas, utilizando la
# función del ejercicio anterior para multiplicar. Por ejemplo 43 = 4 * 4 * 4.

def funcion(a,b):
    mult = a ^ b
    return mult
          
def main():
    a = int(input("A: "))
    b = int(input("B: "))
    res = funcion(a,b)
    print(res)
    
main()
