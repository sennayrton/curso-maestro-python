###### TEMA 8 ######

# Ejemplo de implementación con Programación Estructurada
clientes = [
    {'Nombre': 'Hector',  'Apellidos': 'Costa Guzman',      'dni': '11111111A'},
    {'Nombre': 'Juan',    'Apellidos': 'González Márquez',  'dni': '22222222B'}
]
print(clientes)


def mostrar_cliente(clientes, dni):
    for c in clientes:
        if (dni == c['dni']):
            print('{} {}'.format(c['Nombre'], c['Apellidos']))
            return

    print('Cliente no encontrado')


mostrar_cliente(clientes, '11111111A')

mostrar_cliente(clientes, '11111111Z')


def borrar_cliente(clientes, dni):
    for i, c in enumerate(clientes):
        if (dni == c['dni']):
            del(clientes[i])
            print(str(c), "> BORRADO")
            return

    print('Cliente no encontrado')


borrar_cliente(clientes, '22222222V')

borrar_cliente(clientes, '22222222B')

print(clientes)

# Ejemplo de implementación con Programación Orientada a Objetos


class Cliente:

    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos

    def __str__(self):
        return '{} {}'.format(self.nombre, self.apellidos)


class Empresa:

    def __init__(self, clientes=[]):
        self.clientes = clientes

    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")

    def borrar_cliente(self, dni=None):
        for i, c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c), "> BORRADO")
                return
        print("Cliente no encontrado")


hector = Cliente(nombre="Hector", apellidos="Costa Guzman", dni="11111111A")
juan = Cliente("22222222B", "Juan", "Gonzalez Marquez")
empresa = Empresa(clientes=[hector, juan])
empresa.mostrar_cliente("11111111A")
empresa.borrar_cliente("22222222B")

# La clase es como un molde para crear objetos
# Definición de clase


class Galleta:
    pass


# Instanciación
una_galleta = Galleta()
otra_galleta = Galleta()

# Función type()
# Sirve para determinar la clase de un objeto.


def hola():
    pass


type(hola)

# Atributos y métodos de clase
# Atributos: Hacen referencia a las variables internas de la clase.
# Métodos: Hacen referencia a las funciones internas de la clase.


class Galleta:
    pass


una_galleta = Galleta()

# Definición de atributos dinámicos en los objetos
una_galleta.sabor = "Salado"
una_galleta.color = "Marrón"
print("El sabor de esta galleta es", una_galleta.sabor)

# Definición de atributos en la clase


class Galleta:
    chocolate = False


g = Galleta()
g.chocolate

# Método init()
# Se llama automáticamente al crear una instancia de clase.


class Galleta():
    chocolate = False

    def __init__(self):
        print("Se acaba de crear una galleta.")


g = Galleta()

# Métodos y la palabra self
# Self sirve para hacer referencia a los métodos y atributos base de una clase dentro de sus propios métodos.


class Galleta():
    chocolate = False

    def __init__(self):
        print("Se acaba de crear una galleta.")

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")


g = Galleta()
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()

# Parámetros en el init (argumentos al instanciar)


class Galleta():
    chocolate = False

    def __init__(self, sabor, forma):
        self.sabor = sabor
        self.forma = forma
        print("Se acaba de crear una galleta {} y {}".format(sabor, forma))

    def chocolatear(self):
        self.chocolate = True

    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")


g = Galleta("salada", "cuadrada")

# Métodos especiales de clase
# Constructor y destructor


class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película", self.titulo)

    # Destructor de clase
    def __del__(self):
        print("Se está borrando la película", self.titulo)

    # Redefinimos el método string
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos".format(self.titulo, self.lanzamiento, self.duracion)

    # Redefinimos el método length
    def __len__(self):
        return self.duracion


p = Pelicula("El Padrino", 175, 1972)
len(p)


class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:', self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)

# Creando un catálogo de películas


class Catalogo:

    peliculas = []  # Esta lista contendrá objetos de la clase Pelicula

    def __init__(self, peliculas=[]):
        self.peliculas = peliculas

    def agregar(self, p):  # p será un objeto Pelicula
        self.peliculas.append(p)

    def mostrar(self):
        for p in self.peliculas:
            print(p)  # Print toma por defecto str(p)


p = Pelicula("El Padrino", 175, 1972)
c = Catalogo([p])
# Añadimos una película directamente
c.agregar(Pelicula("El Padrino: Parte 2", 202, 1974))
c.mostrar()

"""En este ejercicio vas a trabajar el concepto de puntos, coordenadas y vectores sobre el plano cartesiano y cómo la programación Orientada a Objetos puede ser una excelente aliada para trabajar con ellos. No está pensado para que hagas ningún tipo de cálculo sino para que practiques la automatización de tareas.
Creo que es un ejemplo muy interesante, punto de partida en la programación de gráficos, pero si consideras que esto no lo tuyo puedes simplemente pasar de largo. Ahora bien, debes ser consciente de que te vas a perder uno de los ejercicios más interesantes del curso.
Antes de continuar voy a explicar brevemente los conceptos básicos por si alguien necesita un repaso.
El plano cartesiano
Representa un espacio bidimensional (en 2 dimensiones), formado por dos rectas perpendiculares, una horizontal y otra vertical que se cortan en un punto. La recta horizontal se denomina eje de las abscisas o eje X, mientras que la vertical recibe el nombre de eje de las ordenadas o simplemente eje Y. En cuanto al punto donde se cortan, se conoce como el punto de origen O.
Es importante remarcar que el plano se divide en 4 cuadrantes:
Puntos y coordenadas
El objetivo de todo esto es describir la posición de puntos sobre el plano en forma de coordenadas, que se forman asociando el valor del eje de las X (horizontal) con el valor del eje Y (vertical).
La representación de un punto es sencilla: P(X,Y) dónde X y la Y son la distancia horizontal (izquierda o derecha) y vertical (arriba o abajo) respectivamente, utilizando como referencia el punto de origen (0,0), justo en el centro del plano.
Vectores en el plano
Finalmente, un vector en el plano hace referencia a un segmento orientado, generado a partir de dos puntos distintos.
A efectos prácticos no deja de ser una línea formada desde un punto inicial en dirección a otro punto final, por lo que se entiende que un vector tiene longitud y dirección/sentido.
En esta figura, podemos observar dos puntos A y B que podríamos definir de la siguiente forma:

A(x1, y1) => A(2, 3)
B(x2, y2) => B(5, 5)
Y el vector se representaría como la diferencia entre las coordendas del segundo punto respecto al primero (el segundo menos el primero):

AB = (x2-x1, y2-y1) => (5-2, 5-3) => (3,2)
Lo que en definitiva no deja de ser: 3 a la derecha y 2 arriba.

Preparación
Crea una clase llamada Punto con sus dos coordenadas X e Y.
Añade un método constructor para crear puntos fácilmente. Si no se reciben una coordenada, su valor será cero.
Sobreescribe el método string, para que al imprimir por pantalla un punto aparezca en formato (X,Y)
Añade un método llamado cuadrante que indique a qué cuadrante pertenece el punto, o si es el origen.
Añade un método llamado vector, que tome otro punto y calcule el vector resultante entre los dos puntos.
(Optativo) Añade un método llamado distancia, que tome otro punto y calcule la distancia entre los dos puntos y la muestre por pantalla. La fórmula es la siguiente:

Nota: La función raíz cuadrada en Python sqrt() se debe importar del módulo math y utilizarla de la siguiente forma:

import math
math.sqrt(9)
> 3.0
Crea una clase llamada Rectangulo con dos puntos (inicial y final) que formarán la diagonal del rectángulo.
Añade un método constructor para crear ambos puntos fácilmente, si no se envían se crearán dos puntos en el origen por defecto.
Añade al rectángulo un método llamado base que muestre la base.
Añade al rectángulo un método llamado altura que muestre la altura.
Añade al rectángulo un método llamado area que muestre el area.
Puedes identificar fácilmente estos valores si intentas dibujar el cuadrado a partir de su diagonal. Si andas perdido, prueba de dibujarlo en un papel, ¡seguro que lo verás mucho más claro! Además recuerda que puedes utilizar la función abs() para saber el valor absolute de un número.

Experimentación
Crea los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0) e imprimelos por pantalla.
Consulta a que cuadrante pertenecen el punto A, C y D.
Consulta los vectores AB y BA.
(Optativo) Consulta la distancia entre los puntos 'A y B' y 'B y A'.
(Optativo) Determina cual de los 3 puntos A, B o C, se encuentra más lejos del origen, punto (0,0).
Crea un rectángulo utilizando los puntos A y B.
Consulta la base, altura y área del rectángulo."""
import math

class Punto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} pertenece al primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} pertenece al segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} pertenece al tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} pertenece al cuarto cuadrante".format(self))
        else:
            print("{} se encuentra sobre el origen".format(self))

    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.x - self.x, p.y - self.y))

    def distancia(self, p):
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))


class Rectangulo:
    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal

    def base(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        print("La base del rectángulo es {}".format(self.base))

    def altura(self):
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        print("La altura del rectángulo es {}".format(self.altura))

    def area(self):
        self.base = abs(self.pFinal.x - self.pInicial.x)
        self.altura = abs(self.pFinal.y - self.pInicial.y)
        self.area = self.base * self.altura
        print("El área del rectángulo es {}".format(self.area))


A = Punto(2, 3)
B = Punto(5, 5)
C = Punto(-3, -1)
D = Punto(0, 0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

R = Rectangulo(A, B)
R.base()
R.altura()
R.area()
