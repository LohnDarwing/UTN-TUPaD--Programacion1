#Ejercicio 1— “Caja del Kiosco”

cliente = input("Cliente: ").strip()
while not cliente.isalpha():
    print("El nombre del cliente no puede estar vacío. Por favor, ingrese un nombre válido.")
    cliente = input("Cliente: ").strip()
#uso .strip() para eliminar espacios en blanco al inicio y al final del nombre del cliente, y .isalpha() para asegurarme de que el nombre solo contenga letras.
# Si el cliente ingresa un nombre vacío o con caracteres no alfabéticos, se le pedirá que ingrese un nombre válido hasta que lo haga correctamente.

cantidad = input("Cantidad de productos a comprar: ").strip()
while not cantidad.isdigit() or int(cantidad) <= 0:
    cantidad = input("cantidad de productos que desea comprar: ").strip()
cantidad = int(cantidad)    
# uso .isdigit() para verificar que la cantidad ingresada sea un número entero positivo. Si el cliente ingresa una cantidad no válida (como un número negativo, cero o un valor no numérico),
# se le pedirá que ingrese una cantidad válida hasta que lo haga correctamente.

total_sin_descuentos = 0
total_con_descuentos = 0
productos = []

for i in range(1, cantidad + 1):
    precio = input(f"Producto {i} - Precio: ").strip()
    while not precio.isdigit() or int(precio) < 0:
        precio = input(f"Producto {i} - Precio: ").strip()
    precio = int(precio)

    descuento = input(f"Producto {i} - Descuento (S/N): ").strip().lower()
    while descuento not in ("s", "n"):
        descuento = input(f"Producto {i} - Descuento (S/N): ").strip().lower()

    productos.append(f"Producto {i} - Precio: {precio} Descuento (S/N): {descuento}")
    total_sin_descuentos += precio
    if descuento == "s":
        total_con_descuentos += precio * 0.9
    else:
        total_con_descuentos += precio

ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

print(f"Cliente: {cliente}")
print(f"Cantidad de productos: {cantidad}")
for linea in productos:
    print(linea)
print(f"Total sin descuentos: ${total_sin_descuentos:.2f}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")


#Ejercicio 2 — “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 1
acceso = False

while intentos <= 3:
    usuario = input(f"Intento {intentos}/3 - Usuario: ").strip()
    clave = input("Clave: ").strip()

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break

    print("Error: credenciales inválidas.")
    intentos += 1

if not acceso:
    print("Cuenta bloqueada.")
else:
    while True:
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ").strip()

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        opcion = int(opcion)
        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue

        if opcion == 1:
            print("Inscripto")
        elif opcion == 2:
            while True:
                nueva_clave = input("Nueva clave: ").strip()
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                    continue

                confirmar = input("Confirmar clave: ").strip()
                if nueva_clave != confirmar:
                    print("Error: las claves no coinciden.")
                    continue

                clave_correcta = nueva_clave
                print("Clave actualizada.")
                break
        elif opcion == 3:
            print("Sigue adelante, cada día aprendes algo nuevo.")
        else:
            break



# Ejercicio 3 — “Agenda de Turnos con Nombres (sin listas)”
operador = input("Operador: ").strip()
while not operador.isalpha():
    operador = input("Operador: ").strip()

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

while True:
    print("1) Reservar turno 2) Cancelar turno 3) Ver agenda del día 4) Ver resumen general 5) Cerrar sistema")
    opcion = input("Opción: ").strip()
    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue
    opcion = int(opcion)
    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        continue

    if opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ").strip()
        if not dia.isdigit() or dia not in ("1", "2"):
            print("Error: día inválido.")
            continue

        nombre = input("Nombre del paciente: ").strip()
        while not nombre.isalpha():
            nombre = input("Nombre del paciente: ").strip()

        if dia == "1":
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Error: el paciente ya tiene turno reservado en Lunes.")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            elif lunes3 == "":
                lunes3 = nombre
            elif lunes4 == "":
                lunes4 = nombre
            else:
                print("No hay turnos disponibles para Lunes.")
        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Error: el paciente ya tiene turno reservado en Martes.")
            elif martes1 == "":
                martes1 = nombre
            elif martes2 == "":
                martes2 = nombre
            elif martes3 == "":
                martes3 = nombre
            else:
                print("No hay turnos disponibles para Martes.")

    elif opcion == 2:
        dia = input("Día (1=Lunes, 2=Martes): ").strip()
        if not dia.isdigit() or dia not in ("1", "2"):
            print("Error: día inválido.")
            continue

        nombre = input("Nombre del paciente: ").strip()
        while not nombre.isalpha():
            nombre = input("Nombre del paciente: ").strip()

        encontrado = False
        if dia == "1":
            if nombre == lunes1:
                lunes1 = ""
                encontrado = True
            elif nombre == lunes2:
                lunes2 = ""
                encontrado = True
            elif nombre == lunes3:
                lunes3 = ""
                encontrado = True
            elif nombre == lunes4:
                lunes4 = ""
                encontrado = True
        else:
            if nombre == martes1:
                martes1 = ""
                encontrado = True
            elif nombre == martes2:
                martes2 = ""
                encontrado = True
            elif nombre == martes3:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado.")
        else:
            print("No se encontró el paciente en ese día.")

    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ").strip()
        if not dia.isdigit() or dia not in ("1", "2"):
            print("Error: día inválido.")
            continue

        if dia == "1":
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    elif opcion == 4:
        ocup_lunes = 0
        if lunes1 != "":
            ocup_lunes += 1
        if lunes2 != "":
            ocup_lunes += 1
        if lunes3 != "":
            ocup_lunes += 1
        if lunes4 != "":
            ocup_lunes += 1
        libre_lunes = 4 - ocup_lunes

        ocup_martes = 0
        if martes1 != "":
            ocup_martes += 1
        if martes2 != "":
            ocup_martes += 1
        if martes3 != "":
            ocup_martes += 1
        libre_martes = 3 - ocup_martes

        print("Lunes - Ocupados:", ocup_lunes, "Disponibles:", libre_lunes)
        print("Martes - Ocupados:", ocup_martes, "Disponibles:", libre_martes)

        if ocup_lunes > ocup_martes:
            print("Día con más turnos: Lunes")
        elif ocup_martes > ocup_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Día con más turnos: Empate entre Lunes y Martes")

    else:
        break



# Ejercicio 4 — “Escape Room: La Bóveda”
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_rachas = 0

agente = input("Nombre del agente: ").strip()
while not agente.isalpha():
    agente = input("Nombre del agente: ").strip()

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
    print("Agente:", agente)
    print("Energía:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", "ON" if alarma else "OFF")
    print("1) Forzar cerradura 2) Hackear panel 3) Descansar")
    opcion = input("Opción: ").strip()
    while not opcion.isdigit() or opcion not in ("1", "2", "3"):
        print("Error: ingrese un número válido.")
        opcion = input("Opción: ").strip()
    opcion = int(opcion)

    if opcion == 1:
        forzar_rachas += 1
        energia -= 20
        tiempo -= 2

        if forzar_rachas == 3:
            alarma = True
            print("La cerradura se trabó y se activó la alarma.")
        else:
            if energia < 40:
                riesgo = input("Número de riesgo 1-3: ").strip()
                while not riesgo.isdigit() or riesgo not in ("1", "2", "3"):
                    print("Error: ingrese un número válido.")
                    riesgo = input("Número de riesgo 1-3: ").strip()
                if riesgo == "3":
                    alarma = True
                    print("Se activó la alarma durante el intento de forzar.")
            if not alarma and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("Cerradura forzada con éxito.")
    elif opcion == 2:
        forzar_rachas = 0
        energia -= 10
        tiempo -= 3
        for paso in range(1, 5):
            codigo_parcial += "ABCD"[paso - 1]
            print(f"Hackeando... Paso {paso}/4")
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Se abrió una cerradura usando el panel.")
    else:
        forzar_rachas = 0
        energia += 15
        if energia > 100:
            energia = 100
        tiempo -= 1
        if alarma:
            energia -= 10
            print("Alarma activa: descansas con mayor costo de energía.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("La alarma bloqueó el sistema y el juego termina.")
        break

if cerraduras_abiertas == 3:
    print("VICTORIA: abriste la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA: te quedaste sin energía o sin tiempo.")
elif alarma and tiempo <= 3 and cerraduras_abiertas < 3:
    print("DERROTA (bloqueo por alarma).")
else:
    print("DERROTA.")



# Ejercicio 5 — “Escape Room: La Arena del Gladiador”
print("=== BIENVENIDO A LA ARENA ===")
gladiador = input("Nombre del Gladiador: ").strip()
while not gladiador.isalpha():
    print("Error: Solo se permiten letras.")
    gladiador = input("Nombre del Gladiador: ").strip()

vida_gladiador = 100
vida_enemigo = 100
pociones = 3
danio_pesado = 15
danio_enemigo = 12
turno_gladiador = True
juego_activo = True

print("=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0 and juego_activo:
    if turno_gladiador:
        print(f"{gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")
        opcion = input("Opción: ").strip()
        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ").strip()
        opcion = int(opcion)
        while opcion not in (1, 2, 3):
            print("Error: Opción fuera de rango.")
            opcion = input("Opción: ").strip()
            while not opcion.isdigit():
                print("Error: Ingrese un número válido.")
                opcion = input("Opción: ").strip()
            opcion = int(opcion)

        if opcion == 1:
            if vida_enemigo < 20:
                danio = danio_pesado * 1.5
            else:
                danio = float(danio_pesado)
            danio_real = int(danio)
            vida_enemigo -= danio_real
            print(f"¡Atacaste al enemigo por {danio_real} puntos de daño!")
        elif opcion == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for _ in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")
        else:
            if pociones > 0:
                pociones -= 1
                vida_gladiador += 30
                if vida_gladiador > 100:
                    vida_gladiador = 100
                print("¡Te curaste y recuperaste 30 puntos de vida!")
            else:
                print("¡No quedan pociones!")
        turno_gladiador = False
    else:
        if vida_enemigo > 0:
            vida_gladiador -= danio_enemigo
            print(f"¡El enemigo te atacó por {danio_enemigo} puntos de daño!")
        turno_gladiador = True
    if vida_gladiador > 0 and vida_enemigo > 0:
        print("=== NUEVO TURNO ===")

if vida_gladiador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")