import os
import keyboard
import time

class Pantalla():
    def __init__(self, pantalla = 20):
        self.LPantalla = []
        
        self.pantalla = pantalla
    def Lista_pantalla(self):
        time.sleep(0.5)
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
        self.LPantalla[Y][X] = ("*")
        



P = Pantalla(pantalla = 30)
P.Ejecutar()


def Movimiento(tecla):
    X = 1
    Y = 1
    while True:
        if tecla.name == 'up':
            Y += 1
            P.Lista_pantalla()
            P.InsertarXY(X,Y)
            print("arriba")
            keyboard.hook(Movimiento)
        
        elif tecla.name == 'down':
            Y -= 1
            P.Lista_pantalla()
            P.InsertarXY(X,Y)
            print("abajo")
            keyboard.hook(Movimiento)

        elif tecla.name == 'left':
            X += 1
            P.Lista_pantalla()
            P.InsertarXY(X,Y)
            print("derecha")
            keyboard.hook(Movimiento)
            
        elif tecla.name == 'right':
            X -= 1
            P.Lista_pantalla()
            P.InsertarXY(X,Y)
            print("Izquierda")
            keyboard.hook(Movimiento)
            
        else:
            break
        

keyboard.hook(Movimiento)

# Esto mantendrá el programa en ejecución hasta que presiones Esc.
keyboard.wait('esc')


    
        


    
    





class Movimiento():
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
    def Movimiento(self):
        pass
        


#Movi=Movimiento(1,2)