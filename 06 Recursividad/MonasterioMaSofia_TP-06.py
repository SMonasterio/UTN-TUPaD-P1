# 1) Factorial recursivo y mostrar todos los factoriales hasta n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = int(input("Ingrese un número para ver los factoriales desde 1 hasta ese número: "))
for i in range(1, n + 1):
    print(f"{i}! = {factorial(i)}")

# 2) Fibonacci recursivo y mostrar la serie hasta n
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

m = int(input("\nIngrese hasta qué posición mostrar la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(m + 1):
    print(f"F({i}) = {fibonacci(i)}")

# 3) Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("\nIngrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

# 4) Decimal a binario recursivo
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

num = int(input("\nIngrese un número decimal para convertir a binario: "))
binario = decimal_a_binario(num)
print(f"El número {num} en binario es: {binario if binario else '0'}")

# 5) Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

palabra = input("\nIngrese una palabra para verificar si es palíndromo: ")
print(f"¿'{palabra}' es palíndromo?: {es_palindromo(palabra)}")

# 6) Suma de dígitos recursiva
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

num = int(input("\nIngrese un número para sumar sus dígitos: "))
print(f"La suma de los dígitos de {num} es: {suma_digitos(num)}")

# 7) Contar bloques en pirámide recursivo
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

niveles = int(input("\nIngrese la cantidad de bloques en el nivel más bajo de la pirámide: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

# 8) Contar dígito recursivo
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

numero = int(input("\nIngrese un número para contar un dígito: "))
digito = int(input("Ingrese el dígito a contar (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}")