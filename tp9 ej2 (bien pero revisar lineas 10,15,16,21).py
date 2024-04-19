#  Una Administradora de Consorcios necesita un sistema para poder gestionar el cobro de las expensas de un edificio de
#  departamentos de 20 unidades. En dos listas almacena la siguiente información: Número de unidad y superficie en metros
#  cuadrados. Validar que no se ingresen números de unidades duplicadas. Cada unidad paga de expensas un valor fijo por
#  metro cuadrado, el que se ingresa por teclado. Se pide:
#      • Informar el promedio de expensas del mes.
#      • Ordenar los listados de mayor a menor según la superficie. Mostrar por pantalla el listado ordenado informando el
#      número de unidad y la superficie en metros cuadrados.

def carga_datos():
    lista_unidad = [0]
    lista_superficie = []
    
    for i in range(3):
        unidad = int(input("Unidad: "))
        for j in range(len(lista_unidad)):
            while unidad == lista_unidad[j]:
                unidad = int(input("Unidad ya ingresada, intente de nuevo: "))
        lista_unidad.append(unidad)
        superficie = int(input("Superficie: "))
        lista_superficie.append(superficie)
        
    del(lista_unidad[0])
        
    return lista_unidad,lista_superficie

def promedio(lista_unidad,lista_superficie,valor):
    contador_unidad = 0
    total_valor = 0
    lista_valor_superficie = []
    
    for i in range(len(lista_superficie)):
        valor_total = lista_superficie[i] * valor
        lista_valor_superficie.append(valor_total)
        contador_unidad += 1
        
    for i in range(len(lista_valor_superficie)):
        total_valor += lista_valor_superficie[i]
        
    elpromedio = total_valor // contador_unidad
    return elpromedio

def ordenamiento_listas(lista_unidad,lista_superficie):
    length = len(lista_superficie)-1
    f = True
    
    while f:
        f = False
        for i in range(length):
            for j in range(length):
                if lista_superficie[i] < lista_superficie[i+1]:
                    aux = lista_superficie[i]
                    lista_superficie[i] = lista_superficie[i+1]
                    lista_superficie[i+1] = aux
                    aux = lista_unidad[i]
                    lista_unidad[i] = lista_unidad[i+1]
                    lista_unidad[i+1] = aux
                    f = True
                    
    return lista_superficie,lista_unidad

def impresion(elpromedio,lista_superficie_ordenada,lista_unidad_ordenada):
    print("Promedio de expensas mensual: ", elpromedio)
    print("Lista superficies ordenadas: ", lista_superficie_ordenada)
    print("Lista unidades ordenadas segun superficies: ", lista_unidad_ordenada)

def main():
    valor = int(input("Valor por metro cuadrado: "))
    lista_unidad,lista_superficie = carga_datos()
    elpromedio = promedio(lista_unidad,lista_superficie,valor)
    lista_superficie_ordenada,lista_unidad_ordenada = ordenamiento_listas(lista_unidad,lista_superficie)
    impresion(elpromedio,lista_superficie_ordenada,lista_unidad_ordenada)
    
main()