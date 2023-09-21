import os
import time
from Control import get_key
from Menu import MENUs

class Pantalla():
    def __init__(self, pantalla = 20):
        self.LPantalla = []
        self.caracter = "*"
        self.pantalla = pantalla
        
    def Lista_pantalla(self):
        #time.sleep(0.2)
        os.system('clear')
        #Este metodo crea una pantalla visual de las listas (pixeles)
        print(len(self.LPantalla))
        for I in range(0, len(self.LPantalla)):            
            print(''.join(self.LPantalla[I]))
            

    def Ejecutar(self):
        for I in range(0, self.pantalla):
            self.LPantalla.append([])

            for J in range(0, self.pantalla*4):
                self.LPantalla[I].append("_")
    
    def InsertarXY(self, X, Y):
        self.LPantalla[Y][X] = (self.caracter)

    def setCaracter(self, caracter):
        self.caracter = caracter
    def setPantalla(self, pantalla):
        self.pantalla = pantalla



P = Pantalla()
P.Ejecutar()

Nvuelta = 0
for I in range(0,15):
    
    time.sleep(0.1)
    P.setCaracter("|")
    P.InsertarXY(4 + Nvuelta,5)
    P.Lista_pantalla()
    time.sleep(0.1)
    P.setCaracter("/")
    P.InsertarXY(4 + Nvuelta,5)
    P.Lista_pantalla()
    time.sleep(0.1)
    P.setCaracter("ᜭ")
    P.InsertarXY(4 + Nvuelta,5)
    P.Lista_pantalla()
    time.sleep(0.1)
    P.setCaracter("\\")
    P.InsertarXY(4 + Nvuelta,5)
    P.Lista_pantalla()

    Nvuelta += 1
P.setCaracter("H")
P.InsertarXY(4, 9)
time.sleep(0.1)
P.Lista_pantalla()

P.setCaracter("O")
P.InsertarXY(5, 9)
time.sleep(0.1)
P.Lista_pantalla()

P.setCaracter("L")
P.InsertarXY(6, 9)
time.sleep(0.1)
P.Lista_pantalla()

P.setCaracter("A")
P.InsertarXY(7, 9)
time.sleep(0.1)
P.Lista_pantalla()

P.setCaracter(" ")
P.InsertarXY(8, 9)
time.sleep(0.1)
P.Lista_pantalla()

P.setCaracter("D")
P.InsertarXY(9, 9)
time.sleep(0.1)
P.Lista_pantalla()

P.setCaracter("B")
P.InsertarXY(10, 9)
time.sleep(0.1)
P.Lista_pantalla()