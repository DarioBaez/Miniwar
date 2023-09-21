import sys
import termios
import tty
#from main import Pantalla

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

