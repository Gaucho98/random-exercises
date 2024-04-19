import random

def carga_productos():
    lista_codigo = []
    lista_stock = []        # cantidad producto
    
    codigo = int(input("Ingrese el codigo del producto: "))
    while codigo < -1:
        codigo = int(input("El numero debe ser positivo, intente nuevamente: "))
    while codigo != -1:
        lista_codigo.append(codigo)
        stock = random.randint(1,50)
        lista_stock.append(stock)
        codigo = int(input("Ingrese el codigo del producto: "))
        while codigo < -1:
            codigo = int(input("El numero debe ser positivo, intente nuevamente: "))
                
    return lista_codigo,lista_stock

def ordenar_productos(lista_codigo,lista_stock):
    length = len(lista_codigo)-1
    f = True
    
    while f:
        f = False
        for i in range(length):
            for j in range(length):
                if lista_codigo[i] > lista_codigo[i+1]:
                    aux = lista_codigo[i]
                    lista_codigo[i] = lista_codigo[i+1]
                    lista_codigo[i+1] = aux
                    aux = lista_stock[j]
                    lista_stock[j] = lista_stock[j+1]
                    lista_stock[j+1] = aux
                    f = True
    return lista_codigo,lista_stock

def codigo_producto_menor5(codigo_ordenado,stock_ordenado):
    stock_menor5 = []
    codigo_menor5 = []
    
    for i in range(len(stock_ordenado)):
        if stock_ordenado[i] < 5:
            codigo_menor5.append(codigo_ordenado[i])
            stock_menor5.append(stock_ordenado[i])
            
    return stock_menor5,codigo_menor5

def unidades_faltantes(lista_codigo,lista_stock):
    contador = 0
    acumulador = 0
    
    for i in range(len(lista_stock)):
        if lista_stock[i] <= 5:
            acumulador += lista_stock[i]
            contador += 1
            
    faltante = contador * 5
    necesito = faltante - acumulador
    
    return necesito 

def producto_mayor_stock(codigo_ordenado,stock_ordenado):
    maximo = 0
    
    for i in range(len(stock_ordenado)):
        if stock_ordenado[i] > maximo:
            maximo = stock_ordenado[i]
            
    target = maximo
    
    mayor_stock = 0
    codigo_perteneciente = 0
    
    for j in range(len(stock_ordenado)):
        if stock_ordenado[j] == maximo:
            mayor_stock = stock_ordenado[j]
            codigo_perteneciente = codigo_ordenado[j]
    
    return mayor_stock,codigo_perteneciente

def busqueda_de_codigo(codigo_ordenado,stock_ordenado):
    lista_busqueda_codigo = []
    lista_busqueda_stock = []
    
    target = int(input("Ingrese el codigo a buscar: "))
    while target != -1:
        for i in range(len(codigo_ordenado)):
            if target == codigo_ordenado[i]:
                lista_busqueda_codigo.append(codigo_ordenado[i])
                lista_busqueda_stock.append(stock_ordenado[i])
        target = int(input("Ingrese el codigo a buscar: "))
         
    return lista_busqueda_codigo,lista_busqueda_stock
        
def impresion_datos(codigo_ordenado,stock_ordenado,stock_menor5,codigo_menor5,necesito,mayor_stock,codigo_perteneciente,lista_busqueda_codigo,lista_busqueda_stock):
    print("---------------------------------")
    print("Codigo:    Cantidad: ")
    for i in range(len(codigo_ordenado)):
        print(codigo_ordenado[i],"      ",stock_ordenado[i])
    print("---------------------------------")
    print("Codigos con stock menor a 5: ")
    for j in range(len(codigo_menor5)):
        print("Codigo",codigo_menor5[j],"tiene stock de: ",stock_menor5[j])
    print("Cantidad de productos faltantes: ",necesito)
    print("---------------------------------")
    print("Producto con mayor stock ->",mayor_stock,".Pertenece a codigo",codigo_perteneciente)
    print("---------------------------------")
    for i in range(len(lista_busqueda_stock)):
        if lista_busqueda_stock[i] < 5:
            print(print("El producto",lista_busqueda_codigo[i],"esta por debajo del stock minimo. Stock ->",lista_busqueda_stock[i]))
        else:
            print("Hay stock suficiente del producto buscado.",lista_busqueda_codigo[i])
    print("---------------------------------")
            
def main():
#     n = int(input("Ingrese la cantidad de productos diferentes (N): "))
    lista_codigo,lista_stock = carga_productos()
    codigo_ordenado,stock_ordenado = ordenar_productos(lista_codigo,lista_stock)
    stock_menor5,codigo_menor5 = codigo_producto_menor5(codigo_ordenado,stock_ordenado)
    necesito = unidades_faltantes(lista_codigo,lista_stock)
    mayor_stock,codigo_perteneciente = producto_mayor_stock(codigo_ordenado,stock_ordenado)
    lista_busqueda_codigo,lista_busqueda_stock = busqueda_de_codigo(codigo_ordenado,stock_ordenado)
    impresion_datos(codigo_ordenado,stock_ordenado,stock_menor5,codigo_menor5,necesito,mayor_stock,codigo_perteneciente,lista_busqueda_codigo,lista_busqueda_stock)
    
main()