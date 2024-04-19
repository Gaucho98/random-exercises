#  Dadas los siguientes arreglos apareados nombres y edades, se pide ordenar por edad de menor a mayor
#  (recuerde que, entre arreglos relacionados, las posiciones indican la relación que hay entre los
#  datos de estos, así en el ejemplo, el nombre “Juan” se corresponde con la edad 28, “Pablo”
#  con la edad 22, etc.):
#  nombres = [‘Juan’, ‘Pablo’, ‘Damián’, ‘Manuel’, ‘Nahuel’, ‘Lucas’]
#  edades = [ 28, 22, 12, 18, 25, 43 ]

def order_by_age(names,ages):
    flag = True
    
    while flag:
        flag = False
        for i in range(len(ages)-1):
            for j in range(len(names)-1):
                if ages[i] > ages[i+1]:
                    aux = ages[i]
                    ages[i] = ages[i+1]
                    ages[i+1] = aux
                    aux = names[i]
                    names[i] = names[i+1]
                    names[i+1] = aux
                    flag = True
                
    return ages,names
    
def print_by_age(ages_ordered,names_ordered):
    for i in range(len(ages_ordered)):
        print("The age of ", names_ordered[i],"is ",ages_ordered[i])

def main():
    names = ["Juan","Pablo","Damián","Manuel","Nahuel","Lucas"]
    ages = [28, 22, 12, 18, 25, 43]
    ages_ordered,names_ordered = order_by_age(names,ages)
    print_by_age(ages_ordered,names_ordered)
    
main()