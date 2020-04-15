###### TEMA 7 ######

# Las excepciones
# Son bloques de código excepcionales que nos permiten continuar con la ejecución de un programa pese a que ocurra un error.
# Creando la excepción - Bloques try y except
# Para prevenir el error, debemos poner el código propenso a error un bloque try y luego encadenaremos un bloque except para tratar la excepción:

try:
    n = float(input("Introduce un número: "))
    m = 4
    print("{}/{}={}".format(n, m, n/m))
except:
    print("Ha ocurrido un error, introduce bien el número")

# Utilizando un while(true), podemos asegurárnos de que el usuario introduce bien el valor
# Repitiendo la lectura por teclado hasta que lo haga bien, y entonces rompemos el bucle con un break:

while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n, m, n/m))
        break  # Importante romper la iteración si todo ha salido bien
    except:
        print("Ha ocurrido un error, introduce bien el número")

# Bloque else en excepciones
# Es posible encadenar un bloque else después del except para comprobar el caso en que todo funcione correctamente (no se ejecuta la excepción).
# El bloque else es un buen momento para romper la iteración con break si todo funciona correctamente:
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n, m, n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien

# Bloque finally en excepciones
# Por último es posible utilizar un bloque finally que se ejecute al final del código, ocurra o no ocurra un error:
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n, m, n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien
    finally:
        print("Fin de la iteración")  # Siempre se ejecuta

# La instrucción raise
# Gracias a raise podemos lanzar un error manual pasándole el identificador. Luego simplemente podemos añadir un except para tratar esta excepción que hemos lanzado:


def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error! No se permite un valor nulo")
    except ValueError:
        print("Error! No se permite un valor nulo (desde la excepción)")


mi_funcion()

