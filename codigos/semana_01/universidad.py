class Universidad:
    def __init__(self, logo, oferta_educativa, localidad, sistema_informatica, modalidad, servicios, ubicacion, talleres, cantidad_salones, rector):
            self.logo=logo
            self.oferta_educativa=oferta_educativa
            self.localidad=localidad
            self.sistema_informatica=sistema_informatica
            self.modalidad=modalidad
            self.servicios=servicios
            self.ubicacion=ubicacion
            self.talleres=talleres
            self.cantidad_salones=cantidad_salones
            self.rector=rector

            print(f"Logotipo de la Universidad:{self.logo}")
            print(f"Oferta Educativa:{self.oferta_educativa}")
            print(f"Localidad de la Universidad:{self.localidad}")
            print(f"Sistema Informatico:{self.sistema_informatica}")
            print(f"Modalidad de la Univerdidad:{self.modalidad}")
            print(f"Servicios de la Universidad:{self.servicios}")
            print(f"Ubicacion de la Universidad:{self.ubicacion}")
            print(f"Talleres de la Universidad:{self.talleres}")
            print(f"Cantidad de Salones de la Universidad:{self.cantidad_salones}")
            print(f"Rector de la Universidad:{self.rector}")

unideh = Universidad("logo.jpg","ing.Software,Turismo","San Miguel","CADU","Virtual","Biblioteca Digital","Santa Catarina",None,None,"Octavio Casillo")    

    
    