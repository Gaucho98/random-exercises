# Imprimir una columna de asteriscos, donde su altura se recibe como parámetro.

def columna(n):
    for i in range(n):
        print("*")
    
def main():
    n = int(input("Ingrese un numero: "))
    columna(n)

main()