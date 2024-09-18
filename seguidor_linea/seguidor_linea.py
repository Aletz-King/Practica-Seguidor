import RPi.GPIO as GPIO
import time

import move

#definir entradas
line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20


#inicializacion
def setup():
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(line_pin_right,GPIO.IN)
    GPIO.setup(line_pin_middle,GPIO.IN)
    GPIO.setup(line_pin_left,GPIO.IN)

#programa principal
def run():

    status_right = GPIO.input(line_pin_right)
    status_middle = GPIO.input(line_pin_middle)
    status_left = GPIO.input(line_pin_left)
    
    print("Valor Derecha :: " + str(status_right) + " Valor Centro :: " + str(status_middle) + " Valor Izquierda :: " + str(status_left))


    if status_middle == 1:
        move.move(100, 'forward','no',1)
    elif status_left == 1:
        move.move(50, 'forward','right',0.6)
    elif status_right == 1:
        move.move(50, 'forward','left',0.6)
    else:
        move.move(50, 'backward','no',1)
    
    """
    bloque de comentario
    """
    print("ss")
if __name__ == '__main__':
    try:
        setup()
        move.setup()
        while 1:
            run()
        pass
    except KeyboardInterrupt:
        move.destroy()
        print("Saliendo")
