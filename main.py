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




def Inicio():
    #MENU()
    m = MENUs(">>>>>>>>>>>>> MINIWAR <<<<<<<<<<<<", ["Jugar", "Continuar", "Salir"])
    m.Titulo()
    m.Opciones()
    m.Opcion()      
    print(m.getOpcion())
    
    while True:
        if m.getOpcion() == 1:
            Jugar()
        elif m.getOpcion() == 2:
            Continuar()
        elif m.getOpcion() == 3:
            break
        else:
            print("esa opcion no existe")
    


def Jugar():

    P = Pantalla()
    m = MENUs(">>>> Configuracion de juego <<<<", ["Selecciona un tamano de mapa", "Selecciona un caracter", "Continuar"])

    while True:
        m.Titulo()
        m.Opciones()
        m.Opcion()
        if m.getOpcion() == 1: 
            while True:
                m2 = MENUs(">>>>>>>>>>>>>>> Mapas <<<<<<<<<<<<<", ["30 * 120", "20 * 80", "10 * 40"])
                m2.Titulo()
                m2.Opciones()
                m2.Opcion()
                if m2.getOpcion() == 1:
                    P.setPantalla(pantalla = 30)
                    break
                elif m2.getOpcion() == 2:
                    P.setPantalla(pantalla = 20)
                    break
                elif m2.getOpcion() == 3:
                    P.setPantalla(pantalla = 10)
                    break
                else:
                    print("Esa opcion no existe...")

        
        elif m.getOpcion() == 2:
            Caractere = input("Ingresa tu caracter... ")
            P.setCaracter(Caractere)
            
        elif m.getOpcion() == 3:
            break
        else:
            print("Esa opcion no existe")

    time.sleep(1)
    print("el juego iniciara en... 3")
    time.sleep(1)
    print("el juego iniciara en... 2")
    time.sleep(1)
    print("el juego iniciara en... 1")
    time.sleep(1)

    P.Ejecutar()
    P.Lista_pantalla()

    #MOVIMIENTO
    y = 0
    x = 0

    #Main loop
    while True:
        # Get user input
        c = get_key()

        # Move cursor based on input
        if c == 'w':
    
            y -= 1
            P.InsertarXY(x,y) 
            print("Presiononaste W")
            P.Lista_pantalla()
            
        elif c == 's':
            
            y += 1
            P.InsertarXY(x,y)
            print("Presiononaste s")
            P.Lista_pantalla()
            
        elif c == 'a':
            
            x -= 1
            P.InsertarXY(x,y)
            print("Presiononaste a")
            P.Lista_pantalla()
            
        elif c == 'd':
            
            x += 1
            P.InsertarXY(x,y)
            print("Presiononaste d")
            P.Lista_pantalla()
            

        # Quit if q is pressed
        elif c == 'q':
            break

def Continuar():
    pass
    
#Aqui se ejecuta el programa
Inicio()