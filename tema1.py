###### TEMA 1 ######

palabra = "Python"

print(palabra[0])  # carácter en la posición 0
print(palabra[5])  # carácter en la posición 5

palabra[0:2]  # excluye el final
palabra[2:-1]  # excluye el final
palabra[2:]  # incluye el final, imprime thon
palabra[:2]
# Si en el slicing no se indica un índice se toma por defecto el principio y el final (incluídos)
palabra[:]

# python es inmutable, pero con slicing se pueden cambiar caracteres de cadenas
palabra = "N" + palabra[1:]
print(palabra)
print(len(palabra))


###### LISTAS ######
numeros = [1, 2, 3, 4]

datos = [4, "Una cadena", -15, 3.14, "Otra cadena"]

datos[0]  # primer item
datos[-1]  # ultimo item

print(numeros + [5, 6, 7, 8])
# no son inmutables, son modificables
pares = [0, 2, 4, 5, 8, 10]
pares[3] = 6  # asignamos nuevo item

print(pares)

# Integran funcionalidades internas, como el método .append() para añadir un ítem al final de la lista
pares.append(12)
# Y una peculiaridad, es que también aceptan asignación con slicing para modificar varios ítems en conjunto
letras = ['a', 'b', 'c', 'd', 'e', 'f']
letras[:3] = ['A', 'B', 'C']
print(letras)
# Asignar una lista vacía equivale a borrar los ítems de la lista o sublista
letras[:3] = []
print(letras)
letras = []  # vacía toda la lista
len(letras)  # es 0
len(pares)

# Listas dentro de listas (anidadas)
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
r = [a, b, c]
print(r)
print(r[0])
print(r[-1])
print(r[0][0])  # primera sublista y primer item de esta
print(r[1][1])

# El siguiente código pretende realizar una media entre 3 números, pero no funciona correctamente. ¿Eres capaz de identificar el problema y solucionarlo?

numero_1 = 9
numero_2 = 3
numero_3 = 6

# Hay que realizar primero la suma de los 3 números antes de dividir
media = (numero_1 + numero_2 + numero_3) / 3
print("La nota media es", media)

# Segunda parte con porcentajes de cada nota
nota_1 = 10
nota_2 = 7
nota_3 = 4

# Podemos multiplicar en tanto por 1 cada nota y sumarlas
media = numero_1 * 0.15 + numero_2 * 0.35 + numero_3 * 0.50
print("La nota media es", media)

# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición, y es que en cada fila, el cuarto elemento siempre debe ser el resultado de sumar los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la técnica del slicing?
matriz = [
    [1, 1, 1, 3],
    [2, 2, 2, 7],
    [3, 3, 3, 9],
    [4, 4, 4, 13]
]


matriz[1][-1] = sum(matriz[1][:-1])
matriz[3][-1] = sum(matriz[3][:-1])

print(matriz)

# Voltear una frase
cadena = "zeréP nauJ,01"

cadena_volteada = cadena[::-1]
print(cadena_volteada[3:], "ha sacado un", cadena_volteada[:2], "de nota.")
