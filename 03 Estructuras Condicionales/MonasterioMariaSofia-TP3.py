from statistics import mode, median, mean
import random

#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
#print("Ingrese su edad:")
#edad = int(input())
#if edad >= 18:
#    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”
#print("Ingrese su nota:")
#nota = int(input())
#if nota >= 6:
#    print("Aprobado")
#else:
#    print("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
#print("Ingrese un número:")
#numero = int(input())
#if numero % 2 == 0:
#    print("Ha ingresado un número par")
#else:
#    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.
#print("Ingrese su edad:")
#edad = int(input())
#if edad < 12:
#    print("Niño/a")
#elif edad >= 12 and edad < 18:
#    print("Adolescente")
#elif edad >= 18 and edad < 30:
#    print("Adulto/a joven")
#elif edad >= 30:
#    print("Adulto/a")
#else:
#    print("Edad no válida")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string.
#print("Ingrese su contraseña:")
#contraseña = input()
#if len(contraseña) >= 8 and len(contraseña) <= 14:
#    print("Ha ingresado una contraseña correcta")
#else:
#    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6)Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
#numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
#if len(numeros_aleatorios) > 0:
#    print("Lista de números aleatorios:", numeros_aleatorios)
#    moda = mode(numeros_aleatorios)
#    mediana = median(numeros_aleatorios)
#    media = mean(numeros_aleatorios)
#
#    print("Moda:", moda)
#    print("Mediana:", mediana)
#    print("Media:", media)
#
#    if media > mediana > moda:
#        print("Sesgo positivo o a la derecha")
#    elif media < mediana < moda:
#        print("Sesgo negativo o a la izquierda")
#    else:
#        print("Sin sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
#print("Ingrese una frase o palabra:")
#frase = input()
#if frase[-1].lower() in "aeiou":
#    frase += "!"
#    print("Resultado:", frase)
#else:
#   print("Resultado:", frase)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
#print("Ingrese su nombre:")
#nombre = input()
#print("Seleccione una opción:")
#print("1. Mayúsculas")
#print("2. Minúsculas")
#print("3. Primera letra mayúscula")
#opcion = int(input())
#if opcion == 1:
#    nombre = nombre.upper()
#    print("Nombre en mayúsculas:", nombre)
#elif opcion == 2:
#    nombre = nombre.lower()
#    print("Nombre en minúsculas:", nombre)
#elif opcion == 3:
#    nombre = nombre.title()
#    print("Nombre con primera letra mayúscula:", nombre)
#else:
#    print("Opción no válida")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
#print("Ingrese la magnitud del terremoto:")
#magnitud = float(input())
#if magnitud < 3:
#    print("Muy leve (imperceptible)")
#elif magnitud >= 3 and magnitud < 4:
#    print("Leve (ligeramente perceptible)")
#elif magnitud >= 4 and magnitud < 5:
#    print("Moderado (sentido por personas, pero generalmente no causa daños)")
#elif magnitud >= 5 and magnitud < 6:
#    print("Fuerte (puede causar daños en estructuras débiles)")
#elif magnitud >= 6 and magnitud < 7:
#    print("Muy Fuerte (puede causar daños significativos)")
#elif magnitud >= 7:
#print("Extremo (puede causar graves daños a gran escala)")
#else:
#    print("Magnitud no válida")

#10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.
dinero = 1000
dinero_retirar = float(input("Ingrese la cantidad de dinero a retirar: "))
if dinero > dinero_retirar:
    dinero -= dinero_retirar
    print("Dinero restante:", dinero)
else:
    print(int "saldo insuficiente, saldo actual ${dinero}")



print("Ingrese el hemisferio (N/S):")
hemisferio = input().upper()
print("Ingrese el mes (1-12):")
mes = int(input())
print("Ingrese el día (1-31):")
dia = int(input())
if hemisferio == "N":
    if mes in [3, 4, 5]:
        print("Primavera")
    elif mes in [6, 7, 8]:
        print("Verano")
    elif mes in [9, 10, 11]:
        print("Otoño")
    elif mes in [12, 1, 2]:
        print("Invierno")
elif hemisferio == "S":
    if mes in [3, 4, 5]:
        print("Otoño")
    elif mes in [6, 7, 8]:
        print("Invierno")
    elif mes in [9, 10, 11]:
        print("Primavera")
    elif mes in [12, 1, 2]:
        print("Verano")
else:
    print("Hemisferio no válido")