# Desarrollar la función signo(n), que reciba un número entero y devuelva 1, -1 o 0 según el valor recibido sea positivo,
# negativo o nulo.

def signo(n):
    if n < 0:
        return "-1"
    elif n > 0:
        return "1"
    else:
        return "0"

def main():
    n = int(input("N: "))
    res = signo(n)
    print(res)
    
main()