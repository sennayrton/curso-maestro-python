###### TEMA 4 ######

# Las Tuplas
# Son unas colecciones parecidas a las listas, con la peculiaridad de que son inmutables.
from collections import deque
tupla = (100, "Hola", [1, 2, 3], -50)
print(tupla)

# Indexación y slicing
tupla[0]

tupla[-1]

print(tupla[2:])

# Función len()
len(tupla)
len(tupla[2])

# Métodos integrados
# index()
# Sirve para buscar un elemento y saber su posición en la tupla. Da error si no se encuentra.
tupla.index(100)
tupla.index('Hola')

# count()
# Sirve para contar cuantas veces aparece un elemento en una tupla.

tupla.count(100)
tupla = (100, 100, 100, 50, 10)
tupla.count(100)

# Los conjuntos
# Son colecciones desordenadas de elementos únicos utilizados para hacer pruebas de pertenencia a grupos y eliminación de elementos duplicados.

conjunto = set()
conjunto = {1, 2, 3}
print(conjunto)

# Método add()
# Sirve para añadir elementos al conjunto. Si un elemento ya se encuentra, no se añadirá de nuevo.

conjunto.add(4)
print(conjunto)
conjunto.add(0)
print(conjunto)

# Pertenencia a grupos con in
grupo = {'Hector', 'Juan', 'Mario'}
'Hector' in grupo
'Maria' in grupo

# Cast de lista a conjunto y viceversa
# Es muy útil transformar listas a conjuntos para borrar los elementos duplicados automáticamente.

l = [1, 2, 3, 3, 2, 1]
print(l)

c = set(l)
print(c)
l = list(c)
print(l)
l = [1, 2, 3, 3, 2, 1]
# En una línea
l = list(set(l))
print(l)

# Cast de cadena a conjunto
# Sirve para crear un conjunto con todos los caracteres de la cadena.
s = "Al pan pan y al vino vino"
set(s)

# Los diccionarios
# Son junto a las listas las colecciones más utilizadas. Se basan en una estructura mapeada donde cada elemento de la colección se encuentra identificado con una clave única. Por tanto, no puede haber dos claves iguales. En otros lenguajes se conocen como arreglos asociativos.

vacio = {}
type(vacio)

# Definición
# Para cada elemento se define la estructura -> clave:valor

colores = {'amarillo': 'yellow', 'azul': 'blue'}

# También se pueden añadir elementos sobre la marcha
colores['verde'] = 'green'
print(colores)
colores['azul']
colores['amarillo']

# Modificación de valor a partir de la clave
colores['amarillo'] = 'white'
print(colores)

# Función del()
# Sirve para borrar un elemento del diccionario.
del(colores['amarillo'])

# Trabajando directamente con registros
edades = {'Hector': 27, 'Juan': 45, 'Maria': 34}
edades['Hector'] += 1
print(edades)
edades['Juan'] + edades['Maria']

# Lectura secuencial con for .. in ..
# Es posible utilizar una iteraciín for para recorrer los elementos del diccionario:
for edad in edades:
    print(edad)

# El problema es que se devuelven las claves, no los valores
# Para solucionarlo deberíamos indicar la clave del diccionario para cada elemento.

for clave in edades:
    print(edades[clave])

# El método .items()
# Nos facilita la lectura en clave y valor de los elementos porque devuelve ambos valores en cada iteración automáticamente:

for c, v in edades.items():
    print(c, v)

# Ejemplo utilizando diccionarios y listas a la vez
# Podemos crear nuestras propias estructuras avanzadas mezclando ambas colecciones. Mientras los diccionarios se encargarían de manejar las propiedades individuales de los registros, las listas nos permitirían manejarlos todos en conjunto.
personajes = []
p = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Humano'}
personajes.append(p)
print(personajes)
p = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo'}
personajes.append(p)
p = {'Nombre': 'Gimli', 'Clase': 'Guerrero', 'Raza': 'Enano'}
personajes.append(p)
print(personajes)

for p in personajes:
    print(p['Nombre'], p['Clase'], p['Raza'])

# Las pilas
# Son colecciones de elementos ordenados que únicamente permiten dos acciones:

# Añadir un elemento a la pila
# Sacar un elemento de la pila
# La peculiaridad es que el último elemento en entrar es el primero en salir. En inglés se conocen como estructuras LIFO (Last In First Out).

# Las podemos crear como listas normales y añadir elementos al final con el append():

pila = [3, 4, 5]
pila.append(6)
pila.append(7)

# Para sacar los elementos utilizaremos el método .pop():
# Al utilizar pop() devolveremos el último elemento, pero también lo borraremos. Si queremos trabajar con él deberíamos asignarlo a una variable o lo perderemos:
pila.pop()  # saca el ultimo elemento y nos lo muestra, debemos asignarlo a una variable
n = pila.pop()  # aqui asignamos el 6 que sale, a una variable
print(n)

# Si hacemos pop() de una pila vacía, devolverá un error:
# Debemos asegurarnos siempre de que la len() de la pila sea mayor que 0 antes de extraer un elemento automáticamente.

# Realiza un programa que siga las siguientes instrucciones:

# Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
# Crea un conjunto llamado administradores con los administradores Juan y Marta.
# Borra al administrador Juan del conjunto de administradores.
# Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
# Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.
# Los conjuntos se pueden recorrer dinámicamente utilizando el bucle for de forma similar a una lista. También cuentan con un método llamado .discard(elemento) que sirve para borrar un elemento.

usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}

administradores.discard("Juan")
administradores.add("Marcos")

for usuario in usuarios:
    if usuario in administradores:
        print(usuario, "Es administrador")
    else:
        print(usuario, "No es administrador")


# Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

# El caballero tiene el doble de vida y defensa que un guerrero.
# El guerrero tiene el doble de ataque y alcance que un caballero.
# El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.
# Muestra como quedan las propiedades de los tres personajes.

caballero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}
guerrero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}
arquero = {'vida': 2, 'ataque': 2, 'defensa': 2, 'alcance': 2}

caballero['vida'] = guerrero['vida'] * 2
caballero['defensa'] = guerrero['defensa'] * 2

guerrero['ataque'] = caballero['ataque'] * 2
guerrero['alcance'] = caballero['alcance'] * 2

arquero['vida'] = guerrero['vida']
arquero['ataque'] = guerrero['ataque']
arquero['defensa'] = guerrero['defensa'] / 2
arquero['alcance'] = guerrero['alcance'] * 2

print("Caballero:\t", caballero)
print("Guerrero:\t", guerrero)
print("Arquero:\t", arquero)


# Durante la planificación de un proyecto se han acordado una lista de tareas. Para cada una de estas tareas se ha asignado un orden de prioridad (cuanto menor es el número de orden, más prioridad).
# ¿Eres capaz de crear una estructura del tipo cola con todas las tareas ordenadas pero sin los números de orden?
# Para ordenar automáticamente una lista es posible utilizar el método .sort().

tareas = [
    [6, 'Distribución'],
    [2, 'Diseño'],
    [1, 'Concepción'],
    [7, 'Mantenimiento'],
    [4, 'Producción'],
    [3, 'Planificación'],
    [5, 'Pruebas']
]

print("**Tareas desordenadas**")
for tarea in tareas:
    print(tarea[0], tarea[1])


tareas.sort()

cola = deque()
for tarea in tareas:
    cola.append(tarea[1])

print("\n=**Tareas ordenadas**")
for tarea in cola:
    print(tarea)
