# Una escuela necesita conocer cuántos alumnos cumplen años en cada mes del año, con el propósito de ofrecerles un agasajo
# especial en su día. Desarrollar un programa que lea el número de legajo y fecha de nacimiento (día, mes y año) de cada
# uno de los alumnos que concurren a dicha escuela. La carga finaliza con un número de legajo igual a -1.
# Emitir un informe donde aparezca -mes por mes- cuántos alumnos cumplen años a lo largo del año.
# Imprimir también una leyenda que indique cuál es el mes con mayor cantidad de cumpleaños.

def cargar_datos():
    lista_legajo = []
    lista_nacimiento = []
    
    legajo = int(input("Ingrese su legajo: "))
    while legajo != -1:
        lista_legajo.append(legajo)
        dia = int(input("Ingrese su dia de nacimiento: "))
        mes = int(input("Ingrese su mes de nacimiento: "))
        lista_nacimiento.append(mes)
        año = int(input("Ingrese su año de nacimiento: "))
        legajo = int(input("Ingrese su legajo: "))
    return lista_legajo,lista_nacimiento

def informe(lista_nacimiento):
    enero = 0
    febrero = 0
    marzo = 0
    abril = 0
    mayo = 0
    junio = 0
    julio = 0
    agosto = 0
    septiembre = 0
    octubre = 0
    noviembre = 0
    diciembre = 0
    
    for i in range(len(lista_nacimiento)):
        if lista_nacimiento[i] == 1:
            enero += 1
        elif lista_nacimiento[i] == 2:
            febrero += 1
        elif lista_nacimiento[i] == 3:
            marzo += 1
        elif lista_nacimiento[i] == 4:
            abril += 1
        elif lista_nacimiento[i] == 5:
            mayo += 1
        elif lista_nacimiento[i] == 6:
            junio += 1
        elif lista_nacimiento[i] == 7:
            julio += 1
        elif lista_nacimiento[i] == 8:
            agosto += 1
        elif lista_nacimiento[i] == 9:
            septiembre += 1
        elif lista_nacimiento[i] == 10:
            octubre += 1
        elif lista_nacimiento[i] == 11:
            noviembre += 1
        elif lista_nacimiento[i] == 12:
            diciembre += 1
    return enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre

def mes_cumpleaños(enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre):
    if enero > febrero and enero > marzo and enero > abril and enero > mayo and enero > junio and enero > julio and enero > agosto and enero > septiembre and enero > octubre and enero > noviembre and enero > diciembre:
        print("El mes del año con mas cumpleaños es Enero.")
    elif febrero > enero and febrero > marzo and febrero > abril and febrero > mayo and febrero > junio and febrero > julio and febrero > agosto and febrero > septiembre and febrero > octubre and febrero > noviembre and febrero > diciembre:
        print("El mes del año con mas cumpleaños es Febrero.")
    elif marzo > enero and marzo > febrero and marzo > abril and marzo > mayo and marzo > junio and marzo > julio and marzo > agosto and marzo > septiembre and marzo > octubre and marzo > noviembre and marzo > diciembre:
        print("El mes del año con mas cumpleaños es Marzo.")
    elif abril > enero and abril > febrero and abril > marzo and abril > mayo and abril > junio and abril > julio and abril > agosto and abril > septiembre and abril > octubre and abril > noviembre and abril > diciembre:
        print("El mes del año con mas cumpleaños es Abril.")
    elif mayo > enero and mayo > febrero and mayo > marzo and mayo > abril and mayo > junio and mayo > julio and mayo > agosto and mayo > septiembre and mayo > octubre and mayo > noviembre and mayo > diciembre:
        print("El mes del año con mas cumpleaños es Mayo.")
    elif junio > enero and junio > febrero and junio > marzo and junio > abril and junio > mayo and junio > julio and junio > agosto and junio > septiembre and junio > octubre and junio > noviembre and junio > diciembre:
        print("El mes del año con mas cumpleaños es Junio.")
    elif julio > enero and julio > febrero and julio > marzo and julio > abril and julio > mayo and julio > junio and julio > agosto and julio > septiembre and julio > octubre and julio > noviembre and julio > diciembre:
        print("El mes del año con mas cumpleaños es Julio.")
    elif agosto > enero and agosto > febrero and agosto > marzo and agosto > abril and agosto > mayo and agosto > junio and agosto > julio and agosto > septiembre and agosto > octubre and agosto > noviembre and agosto > diciembre:
        print("El mes del año con mas cumpleaños es Agosto.")
    elif septiembre > enero and septiembre > febrero and septiembre > marzo and septiembre > abril and septiembre > mayo and septiembre > junio and septiembre > julio and septiembre > agosto and septiembre > octubre and septiembre > noviembre and septiembre > diciembre:
        print("El mes del año con mas cumpleaños es Septiembre.")
    elif octubre > enero and octubre > febrero and octubre > marzo and octubre > abril and octubre > mayo and octubre > junio and octubre > julio and octubre > agosto and octubre > septiembre and octubre > noviembre and octubre > diciembre:
        print("El mes del año con mas cumpleaños es Octubre.")
    elif noviembre > enero and noviembre > febrero and noviembre > marzo and noviembre > abril and noviembre > mayo and noviembre > junio and noviembre > julio and noviembre > agosto and noviembre > septiembre and noviembre > octubre and noviembre > diciembre:
        print("El mes del año con mas cumpleaños es Noviembre.")
    elif diciembre > enero and diciembre > febrero and diciembre > marzo and diciembre > abril and diciembre > mayo and diciembre > junio and diciembre > julio and diciembre > agosto and diciembre > septiembre and diciembre > octubre and diciembre > noviembre:
        print("El mes del año con mas cumpleaños es Diciembre.")
    
def main():
    lista_legajo,lista_nacimiento = cargar_datos()
    print(lista_legajo)
    print(lista_nacimiento)
    enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre = informe(lista_nacimiento)
    print("Cantidad de alumnos que cumplen en enero: ",enero)
    print("Cantidad de alumnos que cumplen en febrero: ",febrero)
    print("Cantidad de alumnos que cumplen en marzo: ",marzo)
    print("Cantidad de alumnos que cumplen en abril: ",abril)
    print("Cantidad de alumnos que cumplen en mayo: ",mayo)
    print("Cantidad de alumnos que cumplen en junio: ",junio)
    print("Cantidad de alumnos que cumplen en julio: ",julio)
    print("Cantidad de alumnos que cumplen en agosto: ",agosto)
    print("Cantidad de alumnos que cumplen en septiembre: ",septiembre)
    print("Cantidad de alumnos que cumplen en octubre: ",octubre)
    print("Cantidad de alumnos que cumplen en noviembre: ",noviembre)
    print("Cantidad de alumnos que cumplen en diciembre: ",diciembre)
    mes_cumpleaños(enero,febrero,marzo,abril,mayo,junio,julio,agosto,septiembre,octubre,noviembre,diciembre)
    
main()