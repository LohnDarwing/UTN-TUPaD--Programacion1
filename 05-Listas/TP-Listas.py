#1) Crear una lista con las notas de 10 estudiantes.
#-Mostrar la lista completa.
#-Calcular y mostrar el promedio.
#-Indicar la nota más alta y la más baja.

notas = [8.5, 7.0, 9.2, 6.8, 10.0, 5.5, 8.0, 7.7, 9.8, 6.0]

print("Notas de los 10 estudiantes:")
for i, nota in enumerate(notas, start=1):
    print(f"Estudiante {i}: {nota}")

promedio = sum(notas) / len(notas)
nota_maxima = max(notas)
nota_minima = min(notas)

print(f"\nPromedio: {promedio:.2f}")
print(f"Nota más alta: {nota_maxima}")
print(f"Nota más baja: {nota_minima}")

#2)Pedir al usuario que cargue 5 productos en una lista.
#-Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
#-Preguntar al usuario qué producto desea eliminar y actualizar la lista.

productos = []

for i in range(1, 6):
    producto = input(f"Ingrese el producto {i}: ")
    productos.append(producto)

print("\nLista de productos cargada:")
for i, producto in enumerate(productos, start=1):
    print(f"{i}. {producto}")

productos_ordenados = sorted(productos)

print("\nLista ordenada alfabéticamente:")
for i, producto in enumerate(productos_ordenados, start=1):
    print(f"{i}. {producto}")

producto_eliminar = input("\n¿Qué producto desea eliminar? ")

if producto_eliminar in productos:
    productos.remove(producto_eliminar)
    print("\nLista actualizada:")
    for i, producto in enumerate(productos, start=1):
        print(f"{i}. {producto}")
else:
    print(f"\nEl producto '{producto_eliminar}' no está en la lista.")


#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
#-Crear una lista con los pares y otra con los impares.
#-Mostrar cuántos números tiene cada lista.

import random

numeros = [random.randint(1, 100) for _ in range(15)]

pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Números generados:")
for i, n in enumerate(numeros, start=1):
    print(f"{i}. {n}")

print("\nPares:")
for i, n in enumerate(pares, start=1):
    print(f"{i}. {n}")

print("\nImpares:")
for i, n in enumerate(impares, start=1):
    print(f"{i}. {n}")

print(f"\nCantidad de pares: {len(pares)}")
print(f"Cantidad de impares: {len(impares)}")


#4) Dada una lista con valores repetidos:
#datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#-Crear una nueva lista sin elementos repetidos.
#-Mostrar el resultado.

sin_repetidos = []
for valor in datos:
    if valor not in sin_repetidos:
        sin_repetidos.append(valor)

print("Lista original:")
for i, valor in enumerate(datos, start=1):
    print(f"{i}. {valor}")

print("\nLista sin elementos repetidos:")
for i, valor in enumerate(sin_repetidos, start=1):
    print(f"{i}. {valor}")


#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#-Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#-Mostrar la lista final actualizada.

estudiantes = [
    "Ana",
    "Bruno",
    "Carmen",
    "Diego",
    "Elena",
    "Fernando",
    "Gabriela",
    "Hugo"
]

print("Estudiantes presentes en clase:")
for i, nombre in enumerate(estudiantes, start=1):
    print(f"{i}. {nombre}")

accion = input("\n¿Desea agregar un nuevo estudiante o eliminar uno existente? (agregar/eliminar): ").strip().lower()

if accion == "agregar":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ").strip()
    estudiantes.append(nuevo)
    print("\nEstudiante agregado.")
elif accion == "eliminar":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ").strip()
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print("\nEstudiante eliminado.")
    else:
        print(f"\nEl estudiante '{eliminar}' no está en la lista.")
else:
    print("\nAcción no reconocida. No se hicieron cambios.")

print("\nLista final actualizada:")
for i, nombre in enumerate(estudiantes, start=1):
    print(f"{i}. {nombre}")


#6) Crear una lista con los nombres de 8 estudiantes presentes en clase.
#-Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
#-Mostrar la lista final actualizada.

numeros = [10, 25, 33, 47, 52, 68, 79]

print("Lista original:")
for i, n in enumerate(numeros, start=1):
    print(f"{i}. {n}")

rotada = [numeros[-1]] + numeros[:-1]

print("\nLista rotada una posición a la derecha:")
for i, n in enumerate(rotada, start=1):
    print(f"{i}. {n}")


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
#-Calcular el promedio de las mínimas y el de las máximas.
#-Mostrar en qué día se registró la mayor amplitud térmica.

temperaturas = [
    [12, 22],
    [14, 24],
    [11, 21],
    [13, 26],
    [10, 20],
    [15, 27],
    [12, 25]
]

minimas = [temp[0] for temp in temperaturas]
maximas = [temp[1] for temp in temperaturas]
amplitudes = [maximas[i] - minimas[i] for i in range(len(temperaturas))]

promedio_min = sum(minimas) / len(minimas)
promedio_max = sum(maximas) / len(maximas)
dia_mayor_amp = amplitudes.index(max(amplitudes)) + 1

print("Temperaturas de la semana (mínima, máxima):")
for i, temp in enumerate(temperaturas, start=1):
    print(f"Día {i}: {temp[0]}° / {temp[1]}°")

print(f"\nPromedio de mínimas: {promedio_min:.2f}°")
print(f"Promedio de máximas: {promedio_max:.2f}°")
print(f"Mayor amplitud térmica: Día {dia_mayor_amp} con {max(amplitudes)}°")


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
#-Mostrar el promedio de cada estudiante.
#-Mostrar el promedio de cada materia.

notas = [
    [8.5, 7.0, 9.2],
    [6.8, 8.0, 7.5],
    [9.0, 8.8, 9.5],
    [7.5, 6.9, 8.1],
    [8.2, 9.1, 7.8]
]

print("Notas de los 5 estudiantes en 3 materias:")
for i, estudiante in enumerate(notas, start=1):
    print(f"Estudiante {i}: {estudiante}")

# Promedio de cada estudiante
print("\nPromedio de cada estudiante:")
for i, estudiante in enumerate(notas, start=1):
    promedio = sum(estudiante) / len(estudiante)
    print(f"Estudiante {i}: {promedio:.2f}")

# Promedio de cada materia
promedios_materia = []
for materia in range(3):
    suma = 0
    for estudiante in notas:
        suma += estudiante[materia]
    promedio = suma / len(notas)
    promedios_materia.append(promedio)

print("\nPromedio de cada materia:")
for i, promedio in enumerate(promedios_materia, start=1):
    print(f"Materia {i}: {promedio:.2f}")


#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#-Inicializarlo con guiones "-" representando casillas vacías.
#-Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O"
#-Mostrar el tablero después de cada jugada.


tablero = [["-" for _ in range(3)] for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()

jugador = "X"
for turno in range(9):
    print(f"Turno {turno + 1} - jugador {jugador}")
    mostrar_tablero()

    while True:
        entrada = input("Ingrese fila y columna separados por espacio (0-2 0-2): ").strip().split()
        if len(entrada) != 2:
            print("Debe ingresar dos números.")
            continue

        fila, col = entrada
        if not (fila.isdigit() and col.isdigit()):
            print("Ingrese valores numéricos.")
            continue

        fila = int(fila)
        col = int(col)
        if fila not in range(3) or col not in range(3):
            print("Los valores deben estar entre 0 y 2.")
            continue

        if tablero[fila][col] != "-":
            print("Esa casilla ya está ocupada.")
            continue

        tablero[fila][col] = jugador
        break

    print("\nTablero después de la jugada:")
    mostrar_tablero()

    jugador = "O" if jugador == "X" else "X"

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#-Mostrar el total vendido por cada producto.
#-Mostrar el día con mayores ventas totales.
#-Indicar cuál fue el producto más vendido en la semana.

ventas = [
    [10, 12, 8, 15, 9, 11, 13],   # Producto 1
    [7, 9, 10, 8, 12, 11, 9],     # Producto 2
    [14, 13, 12, 16, 15, 14, 13], # Producto 3
    [5, 6, 7, 8, 9, 10, 7]        # Producto 4
]

# Total vendido por cada producto
totales_productos = []
for i, producto in enumerate(ventas, start=1):
    total = sum(producto)
    totales_productos.append(total)
    print(f"Producto {i} total vendido: {total}")

# Total vendido por cada día
totales_dias = []
for dia in range(7):
    total_dia = sum(ventas[producto][dia] for producto in range(4))
    totales_dias.append(total_dia)

dia_mayor_venta = totales_dias.index(max(totales_dias)) + 1
print(f"\nDía con mayores ventas totales: Día {dia_mayor_venta} ({totales_dias[dia_mayor_venta-1]} unidades)")

# Producto más vendido en la semana
producto_mas_vendido = totales_productos.index(max(totales_productos)) + 1
print(f"Producto más vendido en la semana: Producto {producto_mas_vendido} ({max(totales_productos)} unidades)")


#11) Crear una lista con los nombres de 10 estudiantes.
#-Solicitar al usuario que ingrese un nombre a buscar.
#-Indicar si el nombre se encuentra en la lista.
#-Mostrar la posición en la que aparece.
#-Si no se encuentra, informar que no está en la lista.


estudiantes = [
    "Ana",
    "Bruno",
    "Carla",
    "Diego",
    "Elena",
    "Fernando",
    "Gabriela",
    "Hugo",
    "Irene",
    "Javier"
]

nombre_buscar = input("Ingrese el nombre a buscar: ").strip()

if nombre_buscar in estudiantes:
    posicion = estudiantes.index(nombre_buscar) + 1
    print(f"El nombre '{nombre_buscar}' se encuentra en la lista.")
    print(f"Aparece en la posición {posicion}.")
else:
    print(f"El nombre '{nombre_buscar}' no está en la lista.")


#12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
#-Mostrar la lista original.
#-Mostrar la lista ordenada de menor a mayor.
#-Mostrar la lista ordenada de mayor a menor.

numeros = []

for i in range(1, 9):
    valor = int(input(f"Ingrese el número {i}: "))
    numeros.append(valor)

print("\nLista original:")
for i, n in enumerate(numeros, start=1):
    print(f"{i}. {n}")

lista_asc = sorted(numeros)
print("\nLista ordenada de menor a mayor:")
for i, n in enumerate(lista_asc, start=1):
    print(f"{i}. {n}")

lista_desc = sorted(numeros, reverse=True)
print("\nLista ordenada de mayor a menor:")
for i, n in enumerate(lista_desc, start=1):
    print(f"{i}. {n}")


#13) Dada la siguiente lista de puntajes de un videojuego:
#puntajes = [450, 1200, 875, 990, 300, 1500, 640]
#-Mostrar el puntaje más alto y el más bajo.
#-Mostrar la lista ordenada de mayor a menor (ranking).
#-Indicar en qué posición del ranking se encuentra el puntaje 990.

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

puntaje_max = max(puntajes)
puntaje_min = min(puntajes)
ranking = sorted(puntajes, reverse=True)

print(f"Puntaje más alto: {puntaje_max}")
print(f"Puntaje más bajo: {puntaje_min}")

print("\nRanking de mayor a menor:")
for i, puntaje in enumerate(ranking, start=1):
    print(f"{i}. {puntaje}")

puntaje_objetivo = 990
if puntaje_objetivo in ranking:
    posicion = ranking.index(puntaje_objetivo) + 1
    print(f"\nEl puntaje {puntaje_objetivo} está en la posición {posicion} del ranking.")
else:
    print(f"\nEl puntaje {puntaje_objetivo} no está en el ranking.")