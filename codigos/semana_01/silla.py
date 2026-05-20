class Silla:
    def __init__(self, patas, color, material, altura, capacidad_peso, marca, tipo, comodidad, estilo, precio):
        self.patas=patas
        self.color=color
        self.material=material
        self.altura=altura
        self.capacidad_peso=capacidad_peso
        self.marca=marca
        self.tipo=tipo
        self.comodidad=comodidad
        self.estilo=estilo
        self.precio=precio

        print(f"Cantidad de Patas:{self.patas}")
        print(f"Color de la mesa:{self.color}")
        print(f"Material:{self.material}")
        print(f"Altura de la mesa:{self.altura}")
        print(f"Capacidad de peso:{self.capacidad_peso}")
        print(f"Marca de la mesa{self.marca}")
        print(f"Tipo se silla(Proposito):{self.tipo}")
        print(f"Comodidad:{self.comodidad}")
        print(f"Estilo de la silla:{self.estilo}")
        print(f"Precio:{self.precio}")

    def cargar(self):
        print("Cargar la silla")
    def recargar(self):
        print("Recargar en la mesa")
    def arrastrar(self):
        print("Arrastrar la silla")
    def tirar(self):
        print("Tirar la silla")
    def comer(self):
        print("Comer en la mesa") 
furnitureR = Silla("4 patas", "crema, cafe", "Cuero sintético, Metal", "76.5 cm", "120 KGS", "Cocina, sala", "medio", "nórdico", "$3,338")   

furnitureR.cargar()
furnitureR.recargar()
furnitureR.arrastrar()
furnitureR.tirar()
furnitureR.comer()