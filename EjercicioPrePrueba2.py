import os, time
os.system("cls")

estacionesDisponibles = 25
capacidadMax = 25
historial = 0

bandera = True

while bandera:
    print("¡Bienvenido al Sistema de Gestión de Estaciones del Centro de Cómputo!")
    time.sleep(3)
    print("=== MENÚ PRINCIPAL ===")
    print("1. Estaciones Disponibles.")
    print("2. Asignar Estación.")
    print("3. Liberar Estación.")
    print("4. Historial de Uso.")
    print("5. Salir.")

    try:
        opcion = int(input("Ingrese una Opción\n"))
        if opcion == 1:
            print(f"Actualmente hay {estacionesDisponibles} Estaciones Disponibles de una capacidad Máxima de {capacidadMax} Estaciones.")
        elif opcion == 2:
            if estacionesDisponibles == 0:
                print("No hay Estaciones Disponibles en este Momento.")
            else:
                try:
                    cantidadAsignar = int(input("Ingrese la Cantidad de Estaciones a Asignar\n"))
                    if cantidadAsignar <= 0:
                        print("La cantidad a Asignar debe ser mayor a 0.")
                    elif cantidadAsignar > estacionesDisponibles:
                        print(f"No hay Capacidad Suficiente. Quedan {estacionesDisponibles} Estaciones Disponibles.")
                    else:
                        estacionesDisponibles -= cantidadAsignar
                        historial += cantidadAsignar
                        print(f"Se han Asignado {cantidadAsignar} Estaciones.")
                except:
                    print("Ingrese un Valor Válido.")
        elif opcion == 3:
            if estacionesDisponibles == capacidadMax:
                print("Todas las Estaciones están Disponibles, No se puede Liberar.")
            else:
                try:
                    cantidadLiberar = int(input("Ingrese la Cantidad de Estaciones que quiere Liberar\n"))
                    if cantidadLiberar <= 0:
                        print("La cantidad a liberar debe ser Mayor a 0.")
                    elif (estacionesDisponibles + cantidadLiberar) > capacidadMax:
                        print(f"Se ha superado la Capacidad Máxima de {capacidadMax} Estaciones.")
                        print(f" Actualmente hay {capacidadMax - estacionesDisponibles} Estaciones en Uso. ")
                    else:
                        estacionesDisponibles += cantidadLiberar
                        historial -= cantidadLiberar
                        print(f"Se han liberado {cantidadLiberar} Estaciones.")
                except:
                    print("Ingrese un Valor Válido.")
        elif opcion == 4:
            print(f"Historial de Uso: {historial}")
        elif opcion == 5:
            print("Gracias por utilizar nuestro Software, Hasta la Próxima.")
            break
        else:
            print("Ingrese una Opción Válida. (1-5)")

    except:
        print("El valor Ingresado debe ser Numérico.")
