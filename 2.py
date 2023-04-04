# Se quiere manipular cierta información de un sistema de correo electrónico llamado miM@il para
# esto se tienen 3 listas:
# Una lista de enteros llamado cuentas que guarda en cuentas[i] el número de cuentas que tiene el cliente i
# # en el sistema de correo.
# La lista cuentas guarda en la posición i el ingreso la cantidad de cuentas que tiene un cliente, por
# ejemplo, el cliente 3 tienen un total de cuentas[2] cantidad de cuentas.
# Adicionalmente se tiene una lista llamada espacio que almacena espacio[i] el espacio usado por el
# cliente i en el sistema de correo.
# Por ejemplo, el cliente 3 tienen un total de espacio[2] espacio utilizado.
# Por último se posee una lista llamada estados que guarda en estados[i]
# True → si el cliente i es un cliente activo del sistema
# False → si el cliente i no está activo.
# El sistema miM@il ha definido que 10MB es el máximo espacio que puede usar un cliente en el sistema
# (teniendo en cuenta todas sus cuentas), pero se sabe que este límite puede variar frecuentemente.
# Usted debe realizar las siguientes rutinas
# (Listo)1. Haga un procedimiento llamado inicializarListaEstados que inicializa la lista de estados con el valor true en todos
# sus elementos.
# (Listo)2. Realice una función llamada calcularMayorNumeroCuentas que retorne el cliente con el mayor número de cuentas
# del sistema.
# (Listo)3. Cree una función llamada promedioEspacio que retorne el promedio del espacio usado en el sistema tomando
# en cuenta únicamente los clientes que están activos.
# 4. Construya un procedimiento llamado desactivarClientes desactive todos los clientes (asigna false en la lista) que
# estén usando un espacio mayor al máximo indicado por el sistema de correo y que tienen por lo menos una
# cuenta. Además, libera el espacio usado por el cliente en el sistema (asigna 0 al espacio usado).
# 5. Realice un procedimiento que se llame modificarLimiteEspacio que permita cambiar el valor del límite de 10MB a
# cualquier otro definido por el usuario.
# 6. Realice un menú de opciones que permita interactuar con el programa.

accounts = [2, 1, 3, 4, 1, 3, 5, 4, 2, 1]
states = [True, True, False, True, True, True, True, False, True, True]
space = [30, 5, 7, 6, 12, 3, 10, 8, 4, 11]
space_max = 10


def inicializarListaEstados():
    for _ in accounts:
        states.append(True)


def calcularMayorNumeroCuentas():
    most_accounts_user = 0
    for account in accounts:
        if account > most_accounts_user:
            most_accounts_user = accounts.index(account)
    return most_accounts_user


def promedioEspacio():
    active_accounts = 0
    average_space = 0
    for space_used in space:
        space_index = accounts[space.index(space_used)]
        if states[space_index]:
            active_accounts += 1
            average_space += space_used
    average_space = average_space / active_accounts
    return average_space


def desactivarClientes():
    for account in accounts:
        account_index = accounts.index(account)
        if account > 0 and space[account_index] > space_max:
            states[account_index] = False
            space[account_index] = 0


def modificarLimiteEspacio():
    global space_max
    space_max = int(input("Seleccione el numero maximo de Mb por cuenta: "))


def menu():
    print("---------------------------------------")
    print("Seleccione una opcion")
    print("1.Inicializar Lista de Estados")
    print("2.Calcular el usuario con mayor cuentas")
    print("3.Uso promedio del espacio")
    print("4.Desactivar clientes con uso de espacio excedido")
    print("5.Modificar el limite de espacio")
    option = int(input())
    print("---------------------------------------")
    return option


option = menu()
if option == 1:
    inicializarListaEstados()
elif option == 2:
    calcularMayorNumeroCuentas()
elif option == 3:
    promedioEspacio()
elif option == 4:
    desactivarClientes()
elif option == 5:
    modificarLimiteEspacio()
else:
    print("Invalid input")
