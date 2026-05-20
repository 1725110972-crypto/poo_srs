class Perro:
    def __init__(self, nombre, raza, edad, tamaño, color, peso, energia, estado_animo, pelaje, salud):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.tamaño=tamaño
        self.color=color
        self.peso=peso
        self.energia=energia
        self.estado_animo=estado_animo
        self.pelaje=pelaje
        self.salud=salud

        print(f"Nombre del perro:{self.nombre}")
        print(f"Raza del perro:{self.raza}")
        print(f"Edad:{self.edad}")
        print(f"Tamaño:{self.tamaño}")
        print(f"Color del pelaje:{self.color}")
        print(f"Peso:{self.peso}")
        print(f"Energía del perro:{self.energia}")
        print(f"Estado de Animo:{self.estado_animo}")
        print(f"Tamaño del pelaje:{self.pelaje}")
        print(f"Salud del perro:{self.pelaje}")

    def ladrar(self):
        ("El perro ladra")
    def correr(self):
        ("El perro corre")
    def comer(self):
        ("El perro come")
    def sentarse(self):
        ("El perro se sienta")
    def jugar(self):
        ("El perro juega")

pastor_Aleman=Perro("Lucas", "Pastor Aleman", "6 años", "62 cm", "negro, cafe", "38kg", "Mucha", "Felíz, Enojado, Triste", "Corto", "Buena")

pastor_Aleman.ladrar()
pastor_Aleman.correr()
pastor_Aleman.comer()
pastor_Aleman.sentarse()
pastor_Aleman.jugar()