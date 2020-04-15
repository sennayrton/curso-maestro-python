###### TEMA 5 ######

# Entradas por teclado
# Ya conocemos la función input() que lee una cadena por teclado. Su único inconveniente es que debemos transformar el valor a numérico si deseamos hacer operaciones con él:

decimal = float(input("Introduce un número decimal con punto: "))
valores = []
print("Introduce 3 valores: ")
for x in range(3):
    valores.append(input("Introduce un valor >: "))

print(valores)

# Salida por pantalla
# La función print() es la forma general de mostrar información por pantalla. Generalmente podemos mostrar texto y variables separándolos con comas:
v = "otro texto"
n = 10
print("Un texto", v, "y un número", n)

# El método .format()
# Es una funcionalidad de las cadenas de texto que nos permite formatear información en una cadena (variables o valores literales) cómodamente utilizando identificadores referenciados:
c = "Un texto '{}' y un número '{}'".format(v, n)
print(c)

# También podemos referenciar a partir de la posición de los valores utilizando índices:
print("Un texto '{1}' y un número '{0}'".format(v, n))

# O podemos utilizar identificador con una clave y luego pasarlas en el format:
print("Un texto '{v}' y un número '{n}'".format(n=n, v=v))

print("{v},{v},{v}".format(v=v))
