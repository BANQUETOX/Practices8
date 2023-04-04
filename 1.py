# Se tiene una lista con los diferentes nombres de provincias del país.
# Provincias
# San José
# Cartago
# Alajuela
# Heredia
# Guanacaste
# Limón
# Puntarenas
# Cada provincia tiene una extensión en territorio diferente las cuáles están dadas por la lista de superficies
# Superficies
# 4965.9
# 3124.67
# 9757.93
# 2656.98
# 10140.71
# 9188.52
# 11265.69
# Algunas de esas provincias cuentan con acceso al mar como se indica en la siguiente lista, donde true
# significa que sí tiene acceso al mar
# Accesos
# False
# False
# False
# False
# True
# True
# True
# Y por último se cuenta con una lista donde se almacena la población estimada que tiene cada una de las
# provincias.
# Poblaciones
# 1633282
# 510727
# 847660
# 449257
# 326953
# 444884
# 410929
# Rutinas a realizar
# Se solicita que usted realice la solución a los siguientes puntos, utilizando las listas y rutinas.
# Crear una función que reciba el nombre de una provincia e indique si existe o no existe (debe devolver el índice de
# la provincia dentro de la lista en caso de que exista, en caso de que la provincia no exista debe devolver -1).
# Realice un procedimiento que imprima la densidad poblacional de cada una de las 7 provincias, la densidad
# poblacional se calcula mediante la siguiente fórmula (densidad = población/ superficie).
# Crear un procedimiento que imprima cuál es la provincia con la mayor densidad poblacional.
# Realice una función que retorne cuanto es el total de terreno que ocupan las provincias que tienen salida al mar.
# Diseñe una función que calcule el tamaño total del país de Costa Rica.
# Realice una función que muestre cuánto es el porcentaje de superficie al que equivale cada provincia con respecto
# al país.
# Cree un menú de opciones que permita interactuar con los puntos anteriores.

provinces = ["San José", "Cartago", "Alajuela",
             "Heredia", "Guanacaste", "Limón", "Puntarenas"]
territory = [4965.9, 3124.67, 9757.93, 2656.98, 10140.71, 9188.52, 11265.69]
access_to_coast = [False, False, False, False, True, True, True]
population = [1633282, 510727, 847660, 449257, 326953, 444884, 410929]


def exist_province(name):
    if name in provinces:
        print(provinces.index(name))
    else:
        print(-1)


def calc_density():
    for province in provinces:
        province_territory = territory[provinces.index(province)]
        province_population = population[provinces.index(province)]
        province_density = province_population / province_territory
        print(
            f"Para la provincia {province} la densidad es de {round(province_density)}")


def most_density_province():
    most_density_province_name = ""
    most_density_province = 0
    for province in provinces:
        province_territory = territory[provinces.index(province)]
        province_population = population[provinces.index(province)]
        province_density = province_population / province_territory
        if province_density > most_density_province:
            most_density_province = province_population
            most_density_province_name = province
    print(most_density_province_name)


def most_population():
    most_population_province = 0
    most_population_province_name = ""
    for province in provinces:
        province_population = population[provinces.index(province)]
        if province_population > most_population_province:
            most_population_province = province_population
            most_population_province_name = province
    print(most_population_province_name)


def coast_contact_terrirtory():
    total_coast_territory = 0
    for province in provinces:
        if access_to_coast[provinces.index(province)]:
            total_coast_territory += territory[provinces.index(province)]
    print(total_coast_territory)


def calc_total_territory():
    total_territory = 0
    for province in provinces:
        province_territory = territory[provinces.index(province)]
        total_territory += province_territory
    print(f"El territorio total del pais es de {total_territory}")
    return total_territory


def calc_territory_percentage():
    total_territory = calc_total_territory()
    for province in provinces:
        province_territory = territory[provinces.index(province)]
        province_percentage = round(
            (province_territory * 100) / total_territory)
        print(
            f"El porventaje de territorio de {province} es de un {province_percentage} porciento")


def menu():
    print("---------------------------------------")
    print("Seleccione una opcion")
    print("1.Existe provincia")
    print("2.Densidad de cada provincia")
    print("3.Provincia de mayor densidad")
    print("4.Provincia con mayor poblacion")
    print("5.Territorio que conecta con la costa")
    print("6.Territorio total")
    print("7.Porcentaje de territorio de cada provincia")
    option = int(input())
    print("---------------------------------------")
    return option


option = menu()
if option == 1:
    exist_province(input("Escriba el nombre de la provincia "))
elif option == 2:
    calc_density()
elif option == 3:
    most_density_province()
elif option == 4:
    most_population()
elif option == 5:
    coast_contact_terrirtory()
elif option == 6:
    calc_total_territory()
elif option == 7:
    calc_territory_percentage()
else:
    print("Invalid input")
