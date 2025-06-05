import math

# 1. Imprimir "Hola Mundo!"
def imprimir_hola_mundo():
    print("Hola Mundo!")

# 2. Saludo personalizado
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# 3. Información personal
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# 4. Área y perímetro de un círculo
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# 5. Segundos a horas
def segundos_a_horas(segundos):
    return segundos / 3600

# 6. Tabla de multiplicar
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

# 7. Operaciones básicas
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Infinito"
    return (suma, resta, multiplicacion, division)

# 8. Calcular IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# 9. Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# 10. Calcular promedio
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__":
    # 1
    imprimir_hola_mundo()

    # 2
    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))

    # 3
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)

    # 4
    radio = float(input("Ingrese el radio del círculo: "))
    print(f"Área: {calcular_area_circulo(radio):.2f}")
    print(f"Perímetro: {calcular_perimetro_circulo(radio):.2f}")

    # 5
    segundos = int(input("Ingrese la cantidad de segundos: "))
    print(f"Equivalen a {segundos_a_horas(segundos):.2f} horas")

    # 6
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
    tabla_multiplicar(numero)

    # 7
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    suma, resta, multiplicacion, division = operaciones_basicas(a, b)
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

    # 8
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")

    # 9
    celsius = float(input("Ingrese la temperatura en Celsius: "))
    print(f"{celsius}°C equivalen a {celsius_a_fahrenheit(celsius):.2f}°F")

    # 10
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    c = float(input("Ingrese el tercer número: "))
    print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")