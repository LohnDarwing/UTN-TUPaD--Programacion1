# 1) 

print("Hola Mundo!")

# 2)

nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#3)

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Ingrese su lugar de residencia: ")

print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro

import math

radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))
area_circulo = round(math.pi * (radio_circulo)**2, 2)
perimetro_circulo = round(2 * math.pi * radio_circulo, 2)
print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")

#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale.

segundos = float(input("ingrese la cantidad de segundos: "))
horas = round (segundos /3600 , 2)
print(f"{segundos} segundos equivalen a {horas} horas.")

#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero_a_multiplicar = int(input("Por favor, ingrese un número entero: "))

print(f"""
    {numero_a_multiplicar} x 1 = {numero_a_multiplicar * 1}
    {numero_a_multiplicar} x 2 = {numero_a_multiplicar * 2}
    {numero_a_multiplicar} x 3 = {numero_a_multiplicar * 3} 
    {numero_a_multiplicar} x 4 = {numero_a_multiplicar * 4}
    {numero_a_multiplicar} x 5 = {numero_a_multiplicar * 5}
    {numero_a_multiplicar} x 6 = {numero_a_multiplicar * 6}
    {numero_a_multiplicar} x 7 = {numero_a_multiplicar * 7}
    {numero_a_multiplicar} x 8 = {numero_a_multiplicar * 8}
    {numero_a_multiplicar} x 9 = {numero_a_multiplicar * 9}
    {numero_a_multiplicar} x 10 = {numero_a_multiplicar * 10}
        """)

#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero_1 = int(input("Ingrese el primer número entero distinto de 0: "))
numero_2 = int(input("Ingrese el segundo número entero distinto de 0: "))
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2
print(f"""
    La suma de {numero_1} y {numero_2} es: {suma}
    La resta de {numero_1} y {numero_2} es: {resta}
    La multiplicación de {numero_1} y {numero_2} es: {multiplicacion}
    La división de {numero_1} y {numero_2} es: {division}
    """)

#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo IMC = peso / altura^2

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = round(peso / (altura ** 2), 2)
print(f"Su índice de masa corporal es: {imc}")

#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 = 9/5. 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

temperatura_celsius = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = round((9/5) * temperatura_celsius + 32, 2)
print(f"{temperatura_celsius} grados Celsius equivalen a {temperatura_fahrenheit} grados Fahrenheit.")

#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.

numero_1 = float(input("Ingrese el primer número: "))
numero_2 = float(input("Ingrese el segundo número: "))
numero_3 = float(input("Ingrese el tercer número: "))
promedio = round((numero_1 + numero_2 + numero_3) / 3, 2)
print(f"El promedio de los números ingresados es: {promedio}") 