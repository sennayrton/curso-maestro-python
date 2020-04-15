###### TEMA 9 ######

# Estructura para los productos de una tienda
# Ejemplo sin herencia


class Producto:
    def __init__(self, referencia, tipo, nombre, pvp, descripcion, productor=None, distribuidor=None, isbn=None, autor=None):
        self.referencia = referencia
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor


adorno = Producto('000A', 'ADORNO', 'Vaso Adornado',
                  15, 'Vaso de porcelana con dibujos')
print(adorno.tipo)

# Creando una jerarquía de productos con clases
# Superclase Producto


class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)

# Subclase Adorno


class Adorno(Producto):
    pass


a = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana adornado con árboles")
print(a)

# Subclase Alimento


class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)


alim = Alimento(2035, "Botella de Aceite de Oliva Extra", 5, "250 ML")
alim.productor = "La Aceitera"
alim.distribuidor = "Distribuciones SA"

print(alim)

# Subclase Libro


class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
ISBN\t\t{}
AUTOR\t\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor)


li = Libro(2036, "Cocina Mediterránea", 9, "Recetas sanas y buenas")
li.isbn = "0-123456-78-9"
li.autor = "Doña Juana"

print(li)

# Trabajando con clases heredadas en conjunto


class Producto:
    def __init__(self, referencia, nombre, pvp, descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion)


class Adorno(Producto):
    pass


class Alimento(Producto):
    productor = ""
    distribuidor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
PRODUCTOR\t{}
DISTRIBUIDOR\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.productor, self.distribuidor)


class Libro(Producto):
    isbn = ""
    autor = ""

    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}
ISBN\t\t{}
AUTOR\t\t{}""".format(self.referencia, self.nombre, self.pvp, self.descripcion, self.isbn, self.autor)


# Creamos algunos objetos
ad = Adorno(2034, "Vaso adornado", 15,
            "Vaso de porcelana adornado con árboles")

al = Alimento(2035, "Botella de Aceite de Oliva Extra", 5, "250 ML")
al.productor = "La Aceitera"
al.distribuidor = "Distribuciones SA"

li = Libro(2036, "Cocina Mediterránea", 9, "Recetas sanas y buenas")
li.isbn = "0-123456-78-9"
li.autor = "Doña Juana"

# Lista de productos
productos = [ad, al]

# Lectura secuencial de productos con un for .. in
for p in productos:
    print(p, "\n")

# Podemos acceder a los atributos si son compartidos entre todos los objetos
for p in productos:
    print(p.referencia, p.nombre)

# Tendremos que tratar cada subclase de forma distinta, gracias a la función isistance():
for p in productos:
    if(isinstance(p, Adorno)):
        print(p.referencia, p.nombre)
    elif(isinstance(p, Alimento)):
        print(p.referencia, p.nombre, p.productor)
    elif(isinstance(p, Libro)):
        print(p.referencia, p.nombre, p.isbn)

# Herencia múltiple
# Posibilidad de que una subclase herede de múltiples superclases.
# El problema aparece cuando las superclases tienen atributos o métodos comunes.
# En estos casos, Python dará prioridad a las clases más a la izquierda en el momento de la declaración de la subclase.


class A:
    def __init__(self):
        print("Soy de clase A")

    def a(self):
        print("Este método lo heredo de A")


class B:
    def __init__(self):
        print("Soy de clase B")

    def b(self):
        print("Este método lo heredo de B")


class C(B, A):
    def c(self):
        print("Este método es de C")


c = C()

c.a()
c.b()
c.c()

# En este ejercicio vas a trabajar el concepto de herencia un poco más en profundidad, aprovechando para introducir un nuevo concepto muy importante que te facilitará mucho la vida.
# Hasta ahora sabemos que una clase heredada puede fácilmente extender algunas funcionalidades, simplemente añadiendo nuevos atributos y métodos, o sobreescribiendo los ya existentes. Como en el siguiente ejemplo


class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


c = Coche("azul", 4, 150, 1200)
print(c)

# Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
# Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
# Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
# Recordatorio: Puedes utilizar el atributo especial de clase name de la siguiente forma para recuperar el nombre de la clase de un objeto:


class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "color {}, {} ruedas".format(self.color, self.ruedas)


class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad, cilindrada):
        super().__init__(color, ruedas)  # utilizamos super() sin self en lugar de Vehiculo
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


# Completa el ejercicio aquí

class Camioneta(Coche):

    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + ", {} kg de carga".format(self.carga)


class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)


class Motocicleta(Bicicleta):

    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)


def catalogar(vehiculos):
    for v in vehiculos:
        print(type(v).__name__, v)


def catalogar(vehiculos, ruedas=None):

    # Primera pasada, mostrar recuento
    if ruedas != None:
        contador = 0
        for v in vehiculos:
            if v.ruedas == ruedas:
                contador += 1
        print("\nSe han encontrado {} vehículos con {} ruedas:".format(
            contador, ruedas))

    # Segnda pasada, mostrar vehículos
    for v in vehiculos:
        if ruedas == None:
            print(type(v).__name__, v)
        else:
            if v.ruedas == ruedas:
                print(type(v).__name__, v)


lista = [
    Coche("azul", 4, 150, 1200),
    Camioneta("blanco", 4, 100, 1300, 1500),
    Bicicleta("verde", 2, "urbana"),
    Motocicleta("negro", 2, "deportiva", 180, 900)
]

catalogar(lista)
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)
