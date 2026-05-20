class LibroDeUnaBiblioteca:
    
      def __init__(self, ancho, largo, titulo, paginas, autor, genero_literario, idioma, capitulos, color, editorial):
            self.ancho=ancho
            self.largo=largo
            self.titulo=titulo
            self.paginas=paginas
            self.autor=autor
            self.genero_literario=genero_literario
            self.idioma=idioma
            self.capitulos=capitulos
            self.color=color
            self.editorial=editorial

            print(f"Ancho del Libro:{self.ancho}")
            print(f"Largo del Libro::{self.largo}")
            print(f"Titulo del libro:{self.titulo}")
            print(f"Paginas del Libro:{self.paginas}")
            print(f"Autor del Libro:{self.autor}")
            print(f"Genero Literario:{self.genero_literario}")
            print(f"Idioma del libro:{self.idioma}")
            print(f"Capitulos del Libro:{self.capitulos}")
            print(f"Color del Libro:{self.color}")
            print(f"Editorial del Libro:{self.editorial}")
    
      def leer(self):
          print("Leer el Libro")
      def abrir(self):
          print("Abrir el Libro")
      def aprender(self):
          print("Aprender del Libro")
      def hojear(self):
          print("Hojear el Libro")
      def cerrar(self):
          print("Cerrar el Libro")
      

principito=LibroDeUnaBiblioteca("15.5cm","21.9cm","Principito","26 paginas","Antoine de Saint","Infantil","Español","27 Capitulos","Salamandra,Emece,Aima Editorial","Azul,Amarillo")    

principito.leer()
principito.aprender()
principito.hojear()
principito.abrir()
principito.cerrar()