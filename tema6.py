###### TEMA 6 ######

# Las funciones
# Son fragmentos de código que se pueden ejecutar múltiples veces. Pueden recibir y devolver información para comunicarse con el proceso principal.
import math
# Definición y llamada


def saludar():
    print("Hola! Este print se llama desde la función saludar()")


saludar()

# Dentro de una función podemos utilizar variables y sentencias de control:


def dibujar_tabla_del_5():
    for i in range(10):
        print("5 * {} = {}".format(i, i*5))


dibujar_tabla_del_5()

# Ámbito de las variables
# Una variable declarada en una función no existe en la función principal:


def test():
    n = 10


test()

# Sin embargo, una variable declarada fuera de la función (al mismo nivel), sí que es accesible desde la función:
m = 10


def test():
    print(m)


test()

# Siempre que declaremos la variable antes de la ejecución, podemos acceder a ella desde dentro:


def test():
    print(l)


# test()
l = 10
test()

# En el caso que declaremos de nuevo una variable en la función, se creará un copia de la misma que sólo funcionará dentro de la función.
# Por tanto no podemos modificar una variable externa dentro de una función:


def test():
    o = 5  # variable que sólo existe dentro de la función
    print(o)


test()

o = 10  # variable externa, no modificable
test()
print(o)

# La instrucción global
# Para poder modificar una variable externa en la función, debemos indicar que es global de la siguiente forma:


def test():
    global o  # variable que hace referencia a la o externa
    o = 5
    print(o)


test()

o = 10
test()
print(o)

# La instrucción global
# Para poder modificar una variable externa en la función, debemos indicar que es global de la siguiente forma:


def test():
    global o  # variable que hace referencia a la o externa
    o = 5
    print(o)


test()

o = 10
test()
print(o)

# Retorno de valores
# Para comunicarse con el exterior, las funciones pueden devolver valores al proceso principal gracias a la instrucción return.

# En el momento de devolver un valor, la ejecución de la función finalizará:


def test():
    return "Una cadena retornada"


test()

# Los valores devueltos se tratan como valores literales directos del tipo de dato retornado:
print(test())
c = test()
print(c)


def test():
    return [1, 2, 3, 4, 5]


print(test())

print(test()[-1])

print(test()[1:4])

l = test()
l[-1]

# Retorno múltiple
# Una característica interesante, es la posibilidad de devolver múltiples valores separados por comas.


def test():
    return "Una cadena", 20, [1, 2, 3]


test()


# Éstos valores se tratan en conjunto como una tupla inmutable y se pueden reasignar a distintas variables:
c, n, l = test()
print(c)
print(n)
print(l)

# Envío de valores
# Para comunicarse con el exterior, las funciones no sólo pueden devolver valores, también pueden recibir información:


def suma(a, b):  # valores que se reciben
    return a+b


# Ahora podemos enviar dos valores a la función:
r = suma(2, 5)  # valores que se envían
print(r)

# Parámetros y argumentos
# En la definición de una función, los valores que se reciben se denominan parámetros, y en la llamada se denominan argumentos.

# Trabajando con argumentos y parámetros
# Argumentos por posición


def resta(a, b):
    return a-b


resta(1, 2)   # posición índice 0 valor 1, posición índice 1 valor 2

# Argumentos por nombre
resta(b=2, a=1)

# Parámetros por defecto
# Para solucionarlo podemos asignar unos valores por defecto nulos a los parámetros, y de ésa forma podríamos hacer una comprobación antes de ejecutar el código de la función:


def resta(a=None, b=None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return
    return a-b


resta(1, 5)

# Paso por valor y paso por referencia
# Paso por valor: Se crea una copia local de la variable dentro de la función.
# Paso por referencia: Se maneja directamente la variable, los cambios realizados dentro le afectarán también fuera.
# Tradicionalmente, los tipos simples se pasan automáticamente por valor y los compuestos por referencia.

# Simples: Enteros, flotantes, cadenas, lógicos...
# Compuestos: Listas, diccionarios, conjuntos...
# Ejemplo paso por valor


def doblar_valor(numero):
    numero *= 2


n = 10
doblar_valor(n)
print(n)

# Ejemplo paso por referencia


def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2


ns = [10, 50, 100]
doblar_valores(ns)
print(ns)

# Trucos
# Para modificar los tipos simples podemos devolverlos modificados y reasignarlos:


def doblar_valor(numero):
    return numero*2


n = 10
n = doblar_valor(n)
print(n)

# Y en el caso de los tipos compuestos, podemos evitar la modificación enviando una copia:


def doblar_valores(numeros):
    for i, n in enumerate(numeros):
        numeros[i] *= 2


ns = [10, 50, 100]
doblar_valores(ns[:])  # Una copia al vuelo de una lista con [:]
print(ns)

# Argumentos y parámetros indeterminados
# Quizá en alguna ocasión no sabemos de antemano cuantos elementos vamos a enviar a una función. En estos casos podemos utilizar los parámetros indeterminados por posición y por nombre.

# Por posición
# Para recibir un número indeterminado de parámetros por posición, debemos crear una lista dinámica de argumentos (una tupla en realidad):


def indeterminados_posicion(*args):
    for arg in args:
        print(arg)


indeterminados_posicion(5, "Hola", [1, 2, 3, 4, 5])

# Por nombre
# Para recibir un número indeterminado de parámetros por nombre (clave-valor), debemos crear un diccionario dinámico de argumentos:


def indeterminados_nombre(**kwargs):
    print(kwargs)


indeterminados_nombre(n=5, c="Hola", l=[1, 2, 3, 4, 5])


def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg)


indeterminados_nombre(n=5, c="Hola", l=[1, 2, 3, 4, 5])


def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg, " ", kwargs[kwarg])


indeterminados_nombre(n=5, c="Hola", l=[1, 2, 3, 4, 5])

# Por posición y nombre a la vez
# Si queremos aceptar ambos tipos de parámetros simultáneamente, entonces debemos crear ambas colecciones dinámicas:


def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t += arg
    print("Sumatorio indeterminado es: ", t)
    for kwarg in kwargs:
        print(kwarg, " ", kwargs[kwarg])


super_funcion(10, 50, -1, 1.56, 10, 20, 300, nombre="Hector", edad=27)

# Funciones recursivas
# Se trata de funciones que se llaman a sí mismas durante su propia ejecución. Funcionan de forma similar a las iteraciones, y debemos encargarnos de planificar el momento en que una función recursiva deja de llamarse o tendremos una función rescursiva infinita.

# Suele utilizarse para dividir una tarea en subtareas más simples de forma que sea más fácil abordar el problema y solucionarlo.

# Ejemplo sencillo sin retorno
# Cuenta regresiva hasta cero a partir de un número:


def cuenta_atras(num):
    num -= 1
    if num > 0:
        print(num)
        cuenta_atras(num)
    else:
        print("Boooooooom!")
    print("Fin de la función", num)


cuenta_atras(5)

# Ejemplo con retorno (factorial de un número)
# El factorial de un número corresponde al producto de todos los números desde 1 hasta el propio número:

# 3! = 1 x 2 x 3 = 6
# 5! = 1 x 2 x 3 x 4 x 5 = 120


def factorial(num):
    print("Valor inicial ->", num)
    if num > 1:
        num = num * factorial(num - 1)
    print("valor final ->", num)
    return num


factorial(5)

# Realiza una función llamada area_rectangulo() que devuelva el área del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura.


def area_rectangulo(base, altura):
    return base*altura


print(area_rectangulo(15, 10))

# Realiza una función llamada area_circulo() que devuelva el área de un círculo a partir de un radio. Calcula el área de un círculo de 5 de radio:
# Puedes utilizar el valor 3.14159 como pi o importarlo del módulo math:

#import math
# print(math.pi)
# > 3.1415...


def area_circulo(radio):
    return (radio**2) * math.pi


print(area_circulo(5))


# Realiza una función llamada relacion() que a partir de dos números cumpla lo siguiente:

# Si el primer número es mayor que el segundo, debe devolver 1.
# Si el primer número es menor que el segundo, debe devolver -1.
# Si ambos números son iguales, debe devolver un 0.
# Comprueba la relación entre los números: '5 y 10', '10 y 5' y '5 y 5'

def relacion(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0


print(relacion(5, 10))
print(relacion(10, 5))
print(relacion(5, 5))

# Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:
# El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2
# Comprueba el punto intermedio entre -12 y 24


def intermedio(a, b):
    return (a + b) / 2


print(intermedio(-12, 24))


# Realiza una función llamada recortar() que reciba tres parámetros. El primero es el número a recortar, el segundo es el límite inferior y el tercero el límite superior. La función tendrá que cumplir lo siguiente:
# Devolver el límite inferior si el número es menor que éste
# Devolver el límite superior si el número es mayor que éste.
# Devolver el número sin cambios si no se supera ningún límite.
# Comprueba el resultado de recortar 15 entre los límites 0 y 10

def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero


print(recortar(15, 0, 10))

# Realiza una función separar() que tome una lista de números enteros y devuelva dos listas ordenadas. La primera con los números pares, y la segunda con los números impares:
#pares, impares = separar([6,5,2,1,7])
# print(pares)   # valdría [2, 6]
# print(impares)  # valdría [1, 5, 7]
# Para ordenar una lista automáticamente puedes usar el método .sort().

numeros = [-12, 84, 13, 20, -33, 101, 9]


def separar(lista):
    numeros.sort()
    pares = []
    impares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    return pares, impares


pares, impares = separar(numeros)
print(pares)
print(impares)
