###### TEMA 2 ######

a = 10
b = 5
a > b

l1 = [0, 1, 2]
l2 = [2, 3, 4]
l1 == l2

# Encontramos 3 básicos:
# Not
# And
# Or

# Expresiones anidadas:
# Se pueden solucionar empleando las reglas de precedencia:
# 1. Primero los paréntesis porque tienen prioridad.
# 2. Segundo, las expresiones aritméticas por sus propias reglas.
# 3. Tercero, las expresiones relacionales.
# 4. Cuarto, las expresiones lógicas.

a = 10
b = 5
a * b - 2**b >= 20 and not (a % b) != 0

# Operadores de asignación

n = 0  # Asignación de 0 en n
while n < 10:  # Expresión relacional n < 10, que devuelve True
    if (n % 2) == 0:  # Expresión aritmética y expresión relacional
        print(n, 'es un número par')
    else:
        print(n, 'es un número impar')
    n += 1  # expresión aritmética n = n + 1 equivalente a operación en asignación n+=1


def operaciones(a, b, c):

    # print(a+b+c)
    # print(a-b-c)
    # print(a*b*c)
    # print(a/b/c)

    suma = (a+b+c)
    resta = (a-b-c)
    multi = (a*b*c)
    divis = (a/b/c)

    return suma, resta, multi, divis


total = operaciones(12, 7, 9)
print(total)


# Realiza un programa que lea 2 números por teclado y determine los siguientes aspectos (es suficiene con mostrar True o False):

# Si los dos números son iguales
# Si los dos números son diferentes
# Si el primero es mayor que el segundo
# Si el segundo es mayor o igual que el primero


n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))

print("¿Son iguales n1 y n2? ", n1 == n2)
print("¿Son diferentes n1 y n2?", n1 != n2)
print("¿El primero es mayor que el segundo?", n1 > n2)
print("¿El segundo es mayor o igual que el primero?", n1 <= n2)

# Utilizando operadores lógicos, determina si una cadena de texto introducida por el usuario tiene una longitud mayor o igual que 3
#  y a su vez es menor que 10 (es suficiene con mostrar True o False):

cadena = input("Escribe una cadena: ")
print("¿La longitud de la cadena es >=3 y <10?",
      len(cadena) >= 3 and len(cadena) < 10)


# Realiza un programa que cumpla el siguiente algoritmo utilizando siempre que sea posible operadores en asignación:

# Guarda en una variable numero_magico el valor 12345679 (sin el 8)
# Lee por pantalla otro numero_usuario, especifica que sea entre 1 y 9 (asegúrate que sea un número entero)
# Multiplica el numero_usuario por 9 en sí mismo
# Multiplica el numero_magico por el numero_usuario en sí mismo
# Finalmente muestra el valor final del numero_magico por pantalla

numero_magico = 12345679
numero_usuario = int(input("Introduce un entero entre 1 y 9: "))
print("¿El numero_usuario es mayor que 1 y menor que 9?")
numero_usuario *= 9
numero_magico *= numero_usuario
print("Numero magico: ", numero_magico)
