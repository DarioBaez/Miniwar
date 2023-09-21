#Este script es el encargado de mostrar el menu principal de opciones para escoger los parametros que iniciaran el juego

class MENUs():
    def __init__(self, titulo, opc):
        self.titulo = titulo
        self.opciones = opc
        self.opcion = 0
    
    def Titulo(self):
        print(self.titulo)

    def Opciones(self):
        opcnum = 0
        for I in self.opciones:
            opcnum += 1
            print(opcnum,") ", I)

    def Opcion(self):
        self.opcion = int(input("Seleccione una opcion... "))
    
    def getOpcion(self):
        return self.opcion
    
    def __del__(self):
        print("Menu destruido")



