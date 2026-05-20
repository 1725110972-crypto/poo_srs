class  HolaMundo: 
    
    def __init__(self):
        print("Constructor")

    def metodoUno(self):
           print ("Metodo Uno")


    def metodoUno(self, variable_uno:int, variable_dos:float)->int:
    ##Ejemplo de Docstring
   
        """"
        Este método recibe 2 variables enteras, la suma y regresa el resultado de la suma

        Args:

        variable_uno:int - Primer número entero
        variable_dos:int - Segundo número entero

        Return:

        suma:int - Suma de los dos números enteros
        """
    

        suma=variable_uno + variable_dos
        return int(suma)
    
    def metodoTres(self, variable_tres:str)->None:
         print(f"Número de caracteres: {len(variable_tres)}")
     

nombre_objeto = HolaMundo()
nombre_objeto.metodoUno()




