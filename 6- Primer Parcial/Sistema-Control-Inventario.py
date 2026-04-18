herramientas = [] # lista para los nombres de las herramientas
existencias = [] # lista paralela para las existencias (stock) de cada herramienta

while True:
# Mostrar el menú principal con sus distintas opciones
    print("\nMenú de inventario:")
    print("1. Carga inicial de herramientas")
    print("2. Cargar existencias de herramientas")
    print("3. Mostrar inventario")
    print("4. Consulta de stock")
    print("5. Reporte de agotados")
    print("6. Alta de nuevo producto")
    print("7. Actualización de stock (venta/ingreso)")
    print("8. Salir")
    opcion = input("Seleccione una opción (1-8): ").strip()

    if opcion == "1":
    # Opción 1: carga inicial de nombres de herramientas
        cantidad = input("¿Cuántas herramientas desea cargar? ").strip()
        while not cantidad.isdigit() or int(cantidad) <= 0:
            print("Debe ingresar un número entero positivo.")
            cantidad = input("¿Cuántas herramientas desea cargar? ").strip()
        cantidad = int(cantidad)
        for i in range(cantidad):
        # validar cada nombre para que no esté vacío ni repetido
            while True:
                nombre = input(f"Ingrese el nombre de la herramienta {i+1}: ").strip()
                if not nombre:
                    print("El nombre no puede estar vacío. Intente nuevamente.")
                elif nombre in herramientas:
                    print("Ese nombre ya existe. Ingrese un nombre diferente.")
                else:
                    herramientas.append(nombre)
                    existencias.append(0) # inicializar existencias en 0
                    break

    elif opcion == "2":
        # Opción 2: cargar existencias de cada herramienta registrada en el sistema
        if len(herramientas) == 0:
            print("No hay herramientas cargadas. Primero debe cargar las herramientas (opción 1).")
        else: 
            for i in range(len(herramientas)):
                cantidad = input(f"Ingrese existencias para '{herramientas[i]}': ").strip()
                while not cantidad.isdigit():
                    print("Debe ingresar un número entero mayor o igual a cero.")
                    cantidad = input(f"Ingrese existencias para '{herramientas[i]}': ").strip()
                existencias[i] = int(cantidad)
    
    elif opcion == "3":
        # Opción 3: mostrar inventario completo con stock
        if len(herramientas) == 0:
            print("No hay inventario para mostrar.")
        else:
            print("\nInventario:")
            for i in range(len(herramientas)):
                print(f"{herramientas[i]} - {existencias[i]} unidades")

    elif opcion == "4":
        # Opción 4: consultar stock de una herramienta por nombre
        if len(herramientas) == 0:
            print("No hay herramientas cargadas para consultar.")
        else:
            nombre = input("Ingrese el nombre de la herramienta a consultar: ").strip()
            if nombre in herramientas:
                indice = herramientas.index(nombre)
                print(f"'{nombre}' tiene {existencias[indice]} unidades en stock.")
            else:
                print(f"La herramienta '{nombre}' no se encuentra en el inventario.")
            
    elif opcion == "5":
        # Opción 5: reporte de herramientas agotadas (stock 0)
        if len(herramientas) == 0:
            print("No hay herramientas cargadas para generar el reporte.")
        else:
            print("\nHerramientas agotadas:")
            encontrados = False
            for i in range(len(herramientas)):
                if existencias[i] == 0:
                    print(f"{herramientas[i]} - AGOTADA")
                    encontrados = True
            if not encontrados:
                print("No hay herramientas agotadas.")
        
    elif opcion == "6":
        # Opción  6: alta de un nuevo producto
        nombre = input("Ingrese el nombre de la nueva herramienta: ").strip()
        if nombre == "":
            print("Nombre vacío. Volviendo al menú principal.")
        elif nombre in herramientas:
            print("Esa herramienta ya existe. No se puede agregar.")
        else:
            cantidad = input(f"Ingrese existencias inicales para '{nombre}': ").strip()
            if not cantidad.isdigit() or int(cantidad) < 0:
                print("Existencias negativas o no válidas. Volviendo al menú principal.")
            else:
                herramientas.append(nombre)
                existencias.append(int(cantidad))
                print(f"Herramienta '{nombre}' agregada con {cantidad} unidades.")

    elif opcion == "7":
        # Opción 7: actualizar stock mediante venta o ingreso
        if len(herramientas) == 0:
            print("No hay herramientas cargadas.")
        else:
            nombre = input("Ingrese el nombre de la herramienta: ").strip()
            if nombre not in herramientas:
                print(f"La herramienta '{nombre}' no existe en el catálogo.")
            else:
                indice = herramientas.index(nombre)
                accion = input("¿Venta o Ingreso? ").strip().lower()
                while accion != "venta" and accion != "ingreso":
                    print("Debe ingresar 'venta' o 'ingreso'.")
                    accion = input("¿Venta o Ingreso? ").strip().lower()

                if accion == "venta":
                    cantidad = input("Ingrese la cantidad a vender: ").strip()
                    while not cantidad.isdigit() or int(cantidad) <= 0:
                        print("Debe ingresar un número entero positivo.")
                        cantidad = input("Ingrese la cantidad a vender: ").strip()
                    cantidad = int(cantidad)
                    if cantidad > existencias[indice]:
                        print("No hay unidades suficientes para la venta.")
                    else:
                        existencias[indice] -= cantidad
                        print(f"Venta realizada. Nuevo stock de '{nombre}': {existencias[indice]}")

                else:
                    cantidad = input("Ingrese la cantidad a ingresar: ").strip()
                    while not cantidad.isdigit() or int(cantidad) < 0:
                        print("Debe ingresar un número entero mayor o igual a cero.")
                        cantidad = input("Ingrese la cantidad a ingresar: ").strip()
                    cantidad = int(cantidad)
                    existencias[indice] += cantidad
                    print(f"Ingreso realizado. Nuevo stock de '{nombre}': {existencias[indice]}")

    elif opcion == "8":
        # Opción 8: salir del sistema
        print("Saliendo del sistema.")
        break

    else:
        # Manejo de opción inválida
        print("Opción no válida. Seleccione un número entre 1 y 8.")