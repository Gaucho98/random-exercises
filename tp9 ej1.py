# Leer los números de legajo de los alumnos de un curso y su nota de examen final. El fin de la carga se determina ingresando
# un -1 como legajo. Se debe validar que la nota ingresada esté entre 1 y 10. Terminada la lectura de datos, informar:
#     • Cantidad de alumnos que aprobaron con nota mayor o igual a 4
#     • Cantidad de alumnos que desaprobaron el examen. Nota menor a 4
#     • Promedio de nota y los legajos que superan el promedio
# Luego se solicita mostrar un listado de legajos y calificaciones ordenado de manera ascendente según el número de
# legajo. Resolver de dos formas: Utilizando dos listas paralelas y utilizando una matriz de dos filas.

def cargar_datos():
    legajos = []
    notas = []
    
    legajo = int(input("Ingrese legajo: "))
    while legajo != -1:
        legajos.append(legajo)
        nota = int(input("Ingrese nota: "))
        while nota < 1 or nota > 10:
            nota = int(input("Nota fuera de rango, intente de nuevo: "))
        notas.append(nota)
        legajo = int(input("Ingrese legajo: "))
    return legajos, notas

def lectura_datos(legajos,notas):
    mayor_4 = 0
    menor_4 = 0
    total = 0
    
    for i in range(len(notas)):
        if notas[i] >= 4 and notas[i] <= 10:
            mayor_4 += 1
            
    for i in range(len(notas)):
        if notas[i] < 4 and notas[i] >= 0:
            menor_4 += 1
            
    for i in range(len(notas)):
        total += notas[i]
        
    cantidad_notas = mayor_4 + menor_4    
    promedio = total // cantidad_notas
    
    return mayor_4, menor_4, promedio

def superan_promedio(legajos,notas,promedio):
    mayor_promedio = []
    
    for i in range(len(notas)):
        if notas[i] > promedio:
            mayor_promedio.append(legajos[i])
    return mayor_promedio
            

def ordenamiento(legajos,notas):
    length = len(legajos)-1
    f = True
    
    while f:
        f = False
        for i in range(len(legajos)-1):
            for j in range(len(notas)-1):
                if legajos[i] > legajos[i+1]:
                    aux = legajos[i]
                    legajos[i] = legajos[i+1]
                    legajos[i+1] = aux
                    aux = notas[i]
                    notas[i] = notas[i+1]
                    notas[i+1] = aux
                    f = True
    return legajos, notas
                    
def impresion_datos(aprobados, desaprobados,promedio,mayor_promedio,legajos_ordenados,notas_ordenadas):
    print("Cantidad de notas aprobadas: ", aprobados)
    print("Cantidad de notas desaprobadas: ", desaprobados)
    print("Promedio de notas: ", promedio)
    print("Legajos que superan el promedio: ", mayor_promedio)
    print("Los legajos ordenados son: ", legajos_ordenados)
    print("Las notas ordenadas segun legajo son: ", notas_ordenadas)

def main():
    legajos, notas = cargar_datos()
    aprobados, desaprobados, promedio = lectura_datos(legajos,notas)
    mayor_promedio = superan_promedio(legajos,notas,promedio)
    legajos_ordenados, notas_ordenadas = ordenamiento(legajos,notas)
    impresion_datos(aprobados, desaprobados,promedio,mayor_promedio,legajos_ordenados,notas_ordenadas)
    
main()