# Una empresa de colectivos debe renovar su flota de vehículos que tengan más de 20 años de antigüedad. Para eso necesita un
# programa que le permita llevar el control de dicha renovación. El programa deberá realizar las siguientes tareas:
#     a) Ingresar el año de renovación (validar que el año sea mayor o igual al año actual).
#     b) Ingresar el número de interno de cada uno de los vehículos y a continuación su modelo (año de fabricación).
#     Finalizar la carga ingresando -1 en el número de unidad.
#     c) Al ingresar los datos del vehículo, validar que el modelo sea mayor a 1980 y menor al año de renovación.
#     d) Mostrar por pantalla un listado con todos los datos de los vehículos que deben ser renovados (número de interno, modelo).
#     e) Informar cuántos vehículos posee la empresa y qué porcentaje de éstos debe ser renovado.
#     f) Informar el año de fabricación de la unidad más antigua de la empresa.

def carga_datos():
    año_actual = 2023
    
    año = int(input("Ingrese el año de renovacion: "))
    while año < año_actual:
        año = int(input("Año invalido, el año debe ser igual o mayor al actual: "))
    
    lista_interno = []
    lista_modelo = []
    
    interno = int(input("Ingrese el numero de interno: "))
    while interno != -1:
        lista_interno.append(interno)
        modelo = int(input("Ingrese el modelo (año): "))
        while modelo < 1980 or modelo > año:
            modelo = int(input("Modelo invalido, intente nuevamente: "))
        lista_modelo.append(modelo)
        interno = int(input("Ingrese el numero de interno: "))
        
    return lista_interno,lista_modelo,año
  
def vehiculos_a_renovar(lista_interno,lista_modelo,año):
    año_renovar = año - 20
    lista_modelo_renovar = []
    lista_interno_renovar = []
    
    for i in range(len(lista_modelo)):
        if lista_modelo[i] < año_renovar:
            lista_modelo_renovar.append(lista_modelo[i])
            lista_interno_renovar.append(lista_interno[i])
            
    return lista_modelo_renovar,lista_interno_renovar

def informe_cantidad(lista_interno,interno_renovar):
    total_internos = 0
    total_renovar = 0
    
    for i in range(len(lista_interno)):
        total_internos += 1
        
    for y in range(len(interno_renovar)):
        total_renovar += 1
        
    porcentaje_renovar = (total_renovar * 100) // total_internos
        
    return total_internos,porcentaje_renovar

def unidad_mas_antigua(lista_modelo):
    minimo = lista_modelo[0]
    
    for i in range(len(lista_modelo)):
        if lista_modelo[i] < minimo:
            minimo = lista_modelo[i]
            
    return minimo
        
def impresion(modelo_renovar,interno_renovar,total_internos,porcentaje_renovar,mas_antiguo):
    print("--------------------------------------")
    for i in range(len(modelo_renovar)):
        print("El interno", interno_renovar[i],"debe ser renovado. Modelo: ",modelo_renovar[i])
    print("--------------------------------------")
    print("La cantidad total de internos es: ",total_internos,". Porcentaje a renovar: ",porcentaje_renovar,"%")
    print("--------------------------------------")
    print("La unidad mas antigua de la empresa es del año: ", mas_antiguo)
        
def main():
    lista_interno,lista_modelo,año = carga_datos()
    modelo_renovar,interno_renovar = vehiculos_a_renovar(lista_interno,lista_modelo,año)
    total_internos,porcentaje_renovar = informe_cantidad(lista_interno,interno_renovar)
    mas_antiguo = unidad_mas_antigua(lista_modelo)
    impresion(modelo_renovar,interno_renovar,total_internos,porcentaje_renovar,mas_antiguo)
    
main()