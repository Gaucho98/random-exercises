# list() ?

# Obtener un elemento
shopping = ["Agua", "Huevos", "Aceite"]
# shopping[]
print("Obtener un elemento: ",shopping[0])

# Trocear una lista
shopping2 = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
# shopping2[x:x]
print("Trocear una lista: ",shopping2[0:3])

# Invertir una lista
shopping3 = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
# shopping3[::-]
print("Invertir una lista: ",shopping3[::-1])
# list(reversed(shopping3)) 
print("Invertir una lista: ",list(reversed(shopping3)))
# shopping3.reverse()
shopping3.reverse()
print("Invertir una lista: ",shopping3)

# Añadir al final de la lista
shopping4 = ["Agua", "Huevos", "Aceite"]
# shopping.append(Atún)
shopping.append("Atún")
print("Añadir al final de la lista: ", shopping4)

# Añadir en cualquier posición de una lista
shopping5 = ["Agua", "Huevos", "Aceite"]
# shopping5.insert(1, "Jamón")
shopping.insert(1, "Jamón")
print("Añadir en cualquier posición de una lista: ", shopping5)

# Repetir elementos
shopping6 = ["Agua", "Huevos", "Aceite"]
a = shopping6 * 3
print("Repetir elementos: ", a)

# Combinar listas
shopping7 = ["Agua", "Huevos", "Aceite"]
fruitshop = ["Naranja", "Manzana", "Piña"]
b = shopping7 + fruitshop
shopping7.extend(fruitshop)
print("Combinar listas: ", b)
print("Combinar listas: ", shopping7)

# Modificar una lista
shopping8 = ["Agua", "Huevos", "Aceite"]
shopping8[0] = "Jugo"
print("Modificar una lista: ",shopping8)

# Borrar elementos
shopping9 = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
del(shopping9[3])
print("Borrar elementos: ", shopping9)
print(shopping9.pop(2))
print("Borrar elementos: ", shopping9)

# Borrado completo de la lista
shopping10 = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
shopping10.clear()
print("Borrado completo de la lista: ", shopping10)

# Encontrar un elemento
shopping11 = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
print("Encontrar un elemento: ", shopping11.index("Huevos"))

# Número de ocurrencias
sheldon_greeting = ["Penny", "Penny", "Penny", "Howard"]
print("Número de ocurrencias: ", sheldon_greeting.count("Penny"))

# Convertir lista a cadena de texto
shopping12 = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
print("Convertir lista a cadena de texto: ", " ".join(shopping12))

# Ordenar una lista
shopping13 = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
print("Ordenar una lista: ", sorted(shopping13))

# Longitud de una lista
shopping13 = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
print("Longitud de una lista: ", len(shopping13))

# Iterar sobre una lista
shopping14 = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
print("Iterar sobre una lista: ")
for product in shopping14:
    print("Yo compro", product)
    
# Iterar usando enumeración
shopping15 = ["Agua", "Huevos", "Aceite", "Sal", "Limón"]
print("Iterar usando enumeración: ")
for i, product in enumerate(shopping15):
    print(i, product)
    
# Copias lista
original_list = [4, 3, 7, 1]
copy_list = original_list.copy()
original_list[0] = 15
print(original_list)
print(copy_list)

