import sys
import termios
import tty
from main import Pantalla

def get_key():
    """
    Wait for a key press and return the key pressed.
    """
    # Save the terminal settings
    old_settings = termios.tcgetattr(sys.stdin)
    try:
        # Set the terminal to raw mode
        tty.setraw(sys.stdin.fileno())

        # Wait for a key press
        ch = sys.stdin.read(1)
    finally:
        # Restore the terminal settings
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

    return ch

P = Pantalla(pantalla = 30)
P.Ejecutar()
P.Lista_pantalla()
y = 0
x = 0
# Main loop
while True:
    # Get user input
    c = get_key()

    # Move cursor based on input
    if c == 'w':
        y -= 1
        print("Presiononaste W")
        P.Lista_pantalla()
        P.InsertarXY(x,y)
    elif c == 's':
        y += 1
        print("Presiononaste sW")
        P.Lista_pantalla()
        P.InsertarXY(x,y)
    elif c == 'a':
        x -= 1
        print("Presiononaste a")
        P.Lista_pantalla()
        P.InsertarXY(x,y)
    elif c == 'd':
        x += 1
        print("Presiononaste d")
        P.Lista_pantalla()
        P.InsertarXY(x,y)

    # Quit if q is pressed
    elif c == 'q':
        break
