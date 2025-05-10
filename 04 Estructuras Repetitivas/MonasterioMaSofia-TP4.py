#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

def ejercicio1():
    for i in range(101):
        print(i)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.

def ejercicio2():
    numero = int(input("Ingrese un número entero: "))
    cantidad_digitos = len(str(abs(numero))) 
    print(f"El número {numero} tiene {cantidad_digitos} dígitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

def ejercicio3():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el segundo valor: "))
    
    if valor1 > valor2:
        valor1, valor2 = valor2, valor1  
    
    suma = sum(range(valor1 + 1, valor2))  
    print(f"La suma de los números entre {valor1} y {valor2} es: {suma}")

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

def ejercicio4():
    suma = 0
    while True:
        numero = int(input("Ingrese un número entero (0 para salir): "))
        if numero == 0:
            break
        suma += numero
    print(f"La suma total es: {suma}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random
def ejercicio5():
    numero_aleatorio = random.randint(0, 9)
    intentos = 0
    while True:
        intento = int(input("Adivina el número entre 0 y 9: "))
        intentos += 1
        if intento == numero_aleatorio:
            print(f"¡Felicidades! Adivinaste el número {numero_aleatorio} en {intentos} intentos.")
            break
        elif intento < numero_aleatorio:
            print("Demasiado bajo. Intenta de nuevo.")
        else:
            print("Demasiado alto. Intenta de nuevo.")

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

def ejercicio6():
    for i in range(100, -1, -1):
        if i % 2 == 0:
            print(i)

#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

def ejercicio7():
    numero = int(input("Ingrese un número entero positivo: "))
    if numero < 0:
        print("Por favor, ingrese un número entero positivo.")
        return
    suma = sum(range(numero + 1))  
    print(f"La suma de los números entre 0 y {numero} es: {suma}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

def ejercicio8():
    cantidad_numeros = 100
    numeros = []

    for i in range(cantidad_numeros):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)

    pares = sum(1 for n in numeros if n % 2 == 0)
    impares = sum(1 for n in numeros if n % 2 != 0)
    negativos = sum(1 for n in numeros if n < 0)
    positivos = sum(1 for n in numeros if n > 0)

    print(f"Números pares: {pares}")
    print(f"Números impares: {impares}")
    print(f"Números negativos: {negativos}")
    print(f"Números positivos: {positivos}")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).
def ejercicio9():
    cantidad_numeros = 100
    numeros = []

    for i in range(cantidad_numeros):
        numero = int(input(f"Ingrese el número {i + 1}: "))
        numeros.append(numero)

    media = sum(numeros) / cantidad_numeros
    print(f"La media de los números ingresados es: {media}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745
def ejercicio10():
    numero = input("Ingrese un número: ")
    numero_invertido = numero[::-1]
    print(f"El número invertido es: {numero_invertido}")

ejercicio10()