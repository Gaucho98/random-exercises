# Desarrollar un algoritmo que permita mostrar una lista de enteros con sus valores a la mitad.
# Ejemplo: Lista [1,2,3,4], mostrar: 0.5 1.0 1.5 2.0.

def cargar_lista():
    lista = [1,2,3,4]
    lista_dividido = []
    
    for i in range(len(lista)):
        dividido = lista[i] / 2
        lista_dividido.append(dividido)
    return lista_dividido
    

def main():
    dividido = cargar_lista()
    print(dividido)
    
main()