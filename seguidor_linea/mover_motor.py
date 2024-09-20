import RPi.GPIO as GPIO #Libreria usada para controlar los pines de la RaspBerry
import time
import RPIservo #Libreria usada para controlar el servo de la direccion de llantas
import move #Libreria usada para el control de los motores

#definir entradas
line_pin_right = 19
line_pin_middle = 16
line_pin_left = 20

move.setup()
scGear = RPIservo.ServoCtrl()
scGear.moveInit()

#inicializacion
def setup():
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(line_pin_right,GPIO.IN)
    GPIO.setup(line_pin_middle,GPIO.IN)
    GPIO.setup(line_pin_left,GPIO.IN)
    
def izquierda(): # Giro a la izquierda
    scGear.moveAngle(0,30)
    time.sleep(0.1) 
    move.move(20, 'forward', 'no', 1)
   
    
def derecha(): # Giro a la derecha
    scGear.moveAngle(0,-30)
    time.sleep(0.1)
    move.move(20, 'forward', 'no', 1)
   
    
def frente(): # Avance Frontal    
    scGear.moveAngle(0,0)
    time.sleep(0.1)
    move.move(30, 'forward', 'no', 1)

def detener(): # Paro de motores
    move.motor_right(0, 0, 0)
    move.motor_left(0, 0, 0)
    
    
# Programa principal
def run():
    while 1:
        status_right = GPIO.input(line_pin_right)
        status_middle = GPIO.input(line_pin_middle)
        status_left = GPIO.input(line_pin_left)
        
        print("Valor Izquierda :: " + str(status_right) + " Valor Centro :: " + str(status_middle) + " Valor Derecha :: " + str(status_left))
        
        """
        x = input()

        if x == 'w':
            print("recto")
            frente()
        elif x == 'd':
            print('derecha')
            derecha()
        elif x == 'a':
            print('izquierda')
            izquierda()
        elif x =='s':
            detener()
            print('parar')
        """
        
        """
        Vista en primera persona
        Limites de grados desde -60 hatsa 60 grados
        """

        # Logica con 2 sensores
       
        if status_right == 0 and status_left == 0: # (0 0)
            frente()
            time.sleep(0.05)
        if status_right == 0 and status_left == 1: # (0 1)
            derecha()
            time.sleep(0.05)
        if status_right == 1 and status_left == 0: # (1 0)
            izquierda()
            time.sleep(0.05)
        if status_right == 1 and status_left == 1: # (1 1)
            frente()
       
        time.sleep(0.05)
        
        
        # pass
    """
    bloque de comentario
    """
    
if __name__ == '__main__':
    
    try:
        setup()
        move.setup()
        run()
        while 1:
            pass    

    except KeyboardInterrupt:
        move.destroy()
        print("Saliendo")
