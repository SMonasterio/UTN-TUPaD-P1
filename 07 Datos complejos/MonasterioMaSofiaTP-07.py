precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
# 1, 2, 3
# Añadir las nuevas frutas con sus precios
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Actualizar los precios solicitados
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Crear una lista con solo las frutas (las claves del diccionario)
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

# 4 Programa para almacenar y consultar números telefónicos

# Crear un diccionario vacío para los contactos
contactos = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    contactos[nombre] = numero

# Consultar un número por nombre
consulta = input("Ingresá el nombre del contacto que querés buscar: ")
if consulta in contactos:
    print(f"El número de {consulta} es {contactos[consulta]}")
else:
    print("Ese contacto no existe.")

# 5 Solicitar una frase al usuario
frase = input("Ingresá una frase: ")

# Separar la frase en palabras
palabras = frase.split()

# Obtener palabras únicas usando un set
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# Contar la cantidad de veces que aparece cada palabra
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("Cantidad de veces que aparece cada palabra:", contador_palabras)

# 6 Ingresar nombres de 3 alumnos y sus 3 notas
alumnos = {}

for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas_str = input(f"Ingresá las 3 notas de {nombre} separadas por espacio: ")
    notas = tuple(float(n) for n in notas_str.split())
    alumnos[nombre] = notas

# Mostrar el promedio de cada alumno
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")

# 7 Ejemplo de sets de estudiantes que aprobaron cada parcial
aprobados_parcial1 = {101, 102, 103, 104, 105}
aprobados_parcial2 = {104, 105, 106, 107}

# Estudiantes que aprobaron ambos parciales (intersección)
ambos = aprobados_parcial1 & aprobados_parcial2
print("Aprobaron ambos parciales:", ambos)

# Estudiantes que aprobaron solo uno de los dos (diferencia simétrica)
solo_uno = aprobados_parcial1 ^ aprobados_parcial2
print("Aprobaron solo uno de los dos parciales:", solo_uno)

# Lista total de estudiantes que aprobaron al menos un parcial (unión)
al_menos_uno = aprobados_parcial1 | aprobados_parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

# 8 # Diccionario de países y sus capitales
paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción"
}

# Construir un nuevo diccionario con capitales como claves y países como valores
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print(capitales_paises)

# 10 Diccionario de productos y stock
stock_productos = {}

# Permitir al usuario consultar y modificar el stock
producto = input("Ingresá el nombre del producto que querés consultar o agregar: ")

if producto in stock_productos:
    print(f"Stock actual de {producto}: {stock_productos[producto]}")
    agregar = int(input(f"¿Cuántas unidades querés agregar al stock de {producto}? "))
    stock_productos[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock_productos[producto]}")
else:
    nuevo_stock = int(input(f"{producto} no existe. Ingresá el stock inicial para agregarlo: "))
    stock_productos[producto] = nuevo_stock
    print(f"{producto} agregado con stock: {stock_productos[producto]}")