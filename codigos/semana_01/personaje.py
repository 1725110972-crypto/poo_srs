class Personaje:
    def __init__(self, nombre, rol, poder, arma, armadura, nivel, colores_vestimenta, aceleracion, genero, habilidades):
        self.nombre=nombre
        self.rol=rol
        self.poder=poder
        self.arma=arma
        self.armadura=armadura
        self.nivel=nivel
        self.colores_vestimenta=colores_vestimenta
        self.aceleracion=aceleracion
        self.genero=genero
        self.habilidades=habilidades

        print(f"Nombre del personaje:{self.nombre}")
        print(f"Rol del personaje:{self.rol}")
        print(f"Poder del personaje:{self.poder}")
        print(f"Arma del personaje:{self.arma}")
        print(f"Armadura del personaje:{self.armadura}")
        print(f"Nivel del personaje:{self.nivel}")
        print(f"Colores de la Vestimenta del personaje:{self.colores_vestimenta}")
        print(f"Aceleracion del personaje:{self.aceleracion}")
        print(f"Genero del personaje:{self.genero}")
        print(f"Habilidades del personaje:{self.habilidades}")
    
    def dispara(self):
        print("Dispara el perosnaje")
    def cargar(self):
        print("Cargar el arma")
    def correr(self):
        print("Correr en el área")
    def lutear(self):
        print("Lútear el cofre")
    def saltar(self):
        print("Saltar las ventanas")
      

neon=Personaje("Neon", "Duelista", "Bioelectricidad", "ráfaga de rayos", "Escudo Corporal", None, "Azul, Negro", "Alta velocidad", "Femenino", "Sobrecarga")

neon.dispara()
neon.cargar()
neon.correr()
neon.lutear()
neon.saltar()  

        
