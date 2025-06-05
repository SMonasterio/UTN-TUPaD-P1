#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
ej1 = range(1, 100, 4)

#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
#¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
ej2 = ["perro", "gato", "conejo", "pez", "loro"]
print(ej2[-2])

#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. 
ej3 = []
ej3.append("perro")
ej3.append("gato")
ej3.append("loro")
print(ej3)

#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente.
#  Imprimir la lista resultante por pantalla. 
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)

#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)
#El programa crea una lista de números y luego elimina el número máximo de esa lista.

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
ej6 = list(range(10, 31, 5))
print(ej6[:2])

#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "camioneta"
autos[2] = "pickup"
print(autos)

#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
ej8 = []
ej8.append(5 * 2)
ej8.append(10 * 2)
ej8.append(15 * 2)
print(ej8)

#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
#a) Agregar "jugo" a la lista del tercer cliente usando append.
compras[2].append("jugo")
print(compras)
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
compras[1][1] = "tallarines"
print(compras)
#c) Eliminar "pan" de la lista del primer cliente.
compras[0].remove("pan")
print(compras)
#d) Imprimir la lista resultante por pantalla
print(compras)


#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
#● Posición lista_anidada[2][0]: 25.5
#● Posición lista_anidada[2][1]: 57.9
#● Posición lista_anidada[2][2]: 30.6
#● Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla.

#debe imprimir por consola 12357

for n in range (1,11):
    bandera=False
    d=0

    for c in range(1, n +1):
        if n% c==0:
            d+=1
            if d<=2:
                bandera=True
            else:
                bandera=False
    if bandera:
        print(n)

#debe imprimir por consola 1
N=5
A=[0]*N 
B=[0]*N
for i in range(N):
    A[i]=i +i +i
for i in range(N):
    B[i]= i*2
contador=0

for i in range(N):
    if A[0] == A[i] and A[0] == B[i]:
        contador+=1
        N=N-contador
resultado = str(contador)
print("resultado" +resultado)
if A[0] < 1:
    resultado = "verdadero"
elif A[0] == 2:
    resultado = "2"
elif A[0] == 3:
    resultado = "falso"

print("resultado" +resultado)

#resultado_final debe ser 51

num1 =3
num2=7
num3=4

if num2%2 == 0:
    x = num2*2
else:
    x=3*num2

if x%2 == 0:
    t=x+num3
else:
    t=x-num3    

if t > 10:
    resultado_final = t * num1
else:
    resultado_final = t + num1

print(f"resultado final", {resultado_final})

#salida 5
contador = 1
sum=0
b = True

num1 =3
while b:
    num2=5
    sum=sum+num2
    contador=contador+1
    while contador <= num1:
        print (f"suam", {sum})
        b=False
        if contador == num1:
            b=True
        break

#salida 6
num1=3
vec=[4,6,1]
may=vec[0]

for i in range (1, num1):
    if vec[i] > may:
        may=vec[i]

print(f"mayor", {may})

#imprimir "D"
# Entrada de datos
dia = 6
mes = 2
anio = 7

if mes in [1, 3, 5, 7, 8, 10, 12]:
    dd = 31
elif mes in [4, 6, 9, 11]:
    dd = 30
elif mes == 2:
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        dd = 29
    else:
        dd = 28
else:
    print("A")
    dd = -1

if dd != -1:
    if dia < 1 or dia > dd:
        print("B")
    elif mes < 1 or mes > 12:
        print("C")
    else:
        print("D")
