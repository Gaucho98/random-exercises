# Devolver True si el número entero recibido como primer parámetro es múltiplo del segundo, o False en caso contrario.
# Ejemplo: esmultiplo(40, 8) devuelve True y esmultiplo(50, 3) devuelve False.

def multiplo(n,m):
    if (n // m) % 2:
        return True
    else:
        return False

def main():
    n = int(input("N: "))
    m = int(input("M: "))
    res = multiplo(n,m)
    print(res)
    
main()
