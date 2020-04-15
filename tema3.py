###### TEMA 3 ######

# Condiciones:

# Sentencia If (Si)
# Permite dividir el flujo de un programa en diferentes caminos. El if se ejecuta siempre que la expresión que comprueba devuelva True.

if True:  # equivale a if not False
    print("Se cumple la condición")
    print("También se muestre este print")

# encadenar varios if
a = 5
if a == 2:
    print("a vale 2")
if a == 5:
    print("a vale 5")

# un if dentro de otro if
a = 5
b = 10
if a == 5:
    print("a vale", a)
    if b == 10:
        print("y b vale", b)

# Sentencia Else (Sino)
# Se encadena a un If para comprobar el caso contrario (en el que no se cumple la condición).
n = 11
if n % 2 == 0:
    print(n, "es un numero par")
else:
    print(n, "es un numero impar")

# Sentencia Elif (Sino Si)
# Se encadena a un if u otro elif para comprobar múltiples condiciones, siempre que las anteriores condiciones no se ejecuten.
comando = "OTRO"
if comando == "ENTRAR":
    print("Bienvenido al sistema")
elif comando == "SALUDAR":
    print("Hola, te mando un saludo")
elif comando == "SALIR":
    print("Saliendo del sistema...")
else:
    print("Este comando no se reconoce")


nota = float(input("Introduce una nota: "))
if nota >= 9:
    print("Sobresaliente")
elif nota >= 7:
    print("Notable")
elif nota >= 6:
    print("Bien")
elif nota >= 5:
    print("Suficiente")
else:
    print("Insuficiente")

# Iteraciones
# Iterar significa realizar una acción varias veces. Cada vez que se repite se denomina iteración.

# Sentencia While (Mientras)
# Se basa en repetir un bloque a partir de evaluar una condición lógica, siempre que ésta sea True.

# Queda en las manos del programador decidir el momento en que la condición cambie a False para hacer que el While finalice.

a = 0
while a <= 5:
    a += 1
    print("a vale: ", a)

# Sentencia Else en bucle While
# Se encadena al While para ejecutar un bloque de código una vez la condición ya no devuelve True (normalmente al final).

a = 0
while a <= 5:
    a += 1
    print("a vale: ", a)
else:
    print("Se ha completado toda la iteración y a vale: ", a)

# Instrucción Break
# Sirve para "romper" la ejecución del While en cualquier momento. No se ejecutará el Else, ya que éste sólo se llama al finalizar la iteración.

a = 0
while a <= 5:
    a += 1
    if (a == 4):
        print("Se rompe el bucle cuando a vale: ", a)
        break
    print("a vale: ", a)
else:
    print("Se ha completado toda la iteración y a vale: ", a)


# menu interactivo
print("¡Hola! Bienvenido al menú interactivo")
while(True):
    print("""¿Qué quieres hacer? Escribe una opción
    1) Saludar
    2) Sumar dos números
    3) Salir""")
    opcion = input()
    if opcion == '1':
        print("Hola, espero que te lo estés pasando bien")
    elif opcion == '2':
        n1 = float(input("Introduce el primer número: "))
        n2 = float(input("Introduce el segundo número: "))
        print("El resultado de la suma es: ", n1+n2)
    elif opcion == '3':
        print("¡Hasta luego! Ha sido un placer ayudarte")
        break
    else:
        print("Comando desconocido, vuelve a intentarlo")

# Recorriendo los elementos de una lista utilizando While

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
indice = 0
while indice < len(numeros):
    print(numeros[indice])
    indice += 1

# Sentencia For (Para) con listas

for numero in numeros:  # Para [variable] en [lista]
    print(numero)

# Modificar ítems de la lista al vuelo
# Para asignar un nuevo valor a los elementos de una lista mientras la recorremos, podríamos intentar asignar al número el nuevo valor:
for numero in numeros:
    numero *= 10
print(numeros)

# Sin embargo, ésto no funciona. La forma correcta de hacerlo es haciendo referencia al índice de la lista en lugar de la variable:
indice = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    numeros[indice] *= 10
    indice += 1
print(numeros)

# For con cadenas
cadena = "Hola amigos"
for caracter in cadena:
    print(caracter)

# Pero debemos recordar que las cadenas son inmutables:
cadena2 = ""
for caracter in cadena:
    cadena2 += caracter * 2

# La función range()
# Sirve para generar una lista de números que podemos recorrer fácilmente, pero no ocupa memoria porque se interpreta sobre la marcha:
for i in range(10):
    print(i)

for i in [0, 1, 2, 3, 4, 5, 6, 7, 9]:
    print(i)

# Si queremos conseguir la lista literal podemos transformar el range a una lista:

print(list(range(10)))

# ejemploFinal
n = 0
while n < 10:
    if (n % 2) == 0:
        print(n, 'Es un número par')
    else:
        print(n, 'Es un número impar')
    n = n + 1

# Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:

# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# En caso de no introducir una opción válida, el programa informará de que no es correcta.

n1 = float(input("Inserte el primer numero: "))
n2 = float(input("Inserte el segundo numero: "))
opcion = 0

print("¿Qué quieres hacer? \n1) Sumar los dos números\n2) Restar los dos números\n3) Multiplicar los dos números")
opcion = int(input("Introduce un número como opcion: "))

if opcion == 1:
    print("La suma de los dos numeros es: ", n1+n2)
elif opcion == 2:
    print("La resta de los dos numeros es: ", n1-n2)
elif opcion == 3:
    print("La multiplicacion de los dos numeros es: ", n1*n2)
else:
    print("La opcion introducida no es correcta/no existe")

# Realiza un programa que lea un número impar por teclado. Si el usuario no introduce un número impar, debe repetise el proceso hasta que lo introduzca correctamente.
numero = 0
while numero % 2 == 0:  # Mientras sea par repetimos el proceso
    numero = int(input("Introduce un número impar: "))

# Realiza un programa que sume todos los números pares desde el 0 hasta el 100:
# range(0, 101, 2), hasta 101 porque queremos que incluya el 100, y el 2 porque solo queremos los pares

suma = sum(range(0, 101, 2))
print(suma)

# Segunda forma con bucles
num = 0
suma = 0

while num <= 100:
    if num % 2 == 0:
        suma += num
    num += 1

print(suma)

# Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números y realiza una media aritmética:
suma = 0
cantidad = int(input("¿Cuántos números quiere introducir?: "))
for x in range(cantidad):
    suma += float(input("Introduzca un número: "))
print("Se han introducido", cantidad, "números que en total han sumado: ",
      suma, "y la media es: ", suma/cantidad)

# Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
# La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)
numeros = [1, 3, 6, 9]

while True:
    numero = int(input("Escribe un número del 0 al 9: "))
    if numero >= 0 and numero <= 9:
        break
if numero in numeros:
    print("El número", numero, "se encuentra en la lista", numeros)
else:
    print("El número", numero, "no se encuentra en la lista", numeros)


# Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:

# Todos los números del 0 al 10 0, 1, 2, ..., 10
# Todos los números del -10 al 0 -10, -9, -8, ..., 0
# Todos los números pares del 0 al 20 0, 2, 4, ..., 20
# Todos los números impares entre -20 y 0 -19, -17, -15, ..., -1
# Todos los números múltiples de 5 del 0 al 50 0, 5, 10, ..., 50
# Utiliza el tercer parámetro de la función range(inicio, fin, salto).

print(list(range(0, 11)))
print(list(range(-10, 1)))
print(list(range(0, 21, 2)))
print(list(range(-19, 0, 2)))
print(list(range(0, 51, 5)))

# Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetise ningún elemento en la nueva lista:

lista1 = ["h", 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
lista2 = ["h", 'o', 'l', 'a', ' ', 'l', 'u', 'n', 'a']

lista3 = []

for letra in lista1:
    if letra in lista2 and letra not in lista3:
        lista3.append(letra)

print(lista3)
