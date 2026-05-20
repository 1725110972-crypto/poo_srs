class Mesa:

    def __init__(self, color, patas, comodidad, ancho, largo, material, dureza, cantidad_soporte, precio, forma_base):
        self.color=color
        self.patas=patas
        self.comodidad=comodidad
        self.ancho=ancho
        self.largo=largo
        self.material=material
        self.dureza=dureza
        self.cantidad_soporte=cantidad_soporte
        self.precio=precio
        self.forma_base=forma_base

        print(f"Color de la mesa:{self.color}")
        print(f"Cantidad de patas:{self.patas}")
        print(f"Comodidad de la mesa:{self.comodidad}")
        print(f"Ancho de la mesa:{self.ancho}")
        print(f"Largo de la mesa:{self.largo}")
        print(f"Material de la mesa:{self.material}")
        print(f"Dureza de la mesa:{self.dureza}")
        print(f"Cantidad del soporte:{self.cantidad_soporte}")
        print(f"Precio:{self.precio}")
        print(f"Forma de la Base:{self.forma_base}")
    
    def recargar(self):
        print("Recargar en la mesa")
    def cargar(self):
        print("Cargar la mesa")
    def limpiar(self):
        print("Limpiar la mesa")
    def arrastrar(self):
        print("Arrastrar la mesa")
    def estudiar(self):
        print("Estudiar en la mesa")

reganet=Mesa("Blanca", "4 patas", "regular", "50cm", "76cm", "Plastico reforzado, acero", "media", "60kg", "800 pesos", "cuadrada")

reganet.recargar()
reganet.cargar()
reganet.limpiar()
reganet.arrastrar()
reganet.estudiar()