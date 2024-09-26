import RPi.GPIO as GPIO
from time import sleep

# Pines del Motor izquierdo visto desde primera persona
"""
motor_A_pin1 = 27
motor_A_pin2 = 18
motor_A_ctrl = 17
pwm_A = 0
"""
# Pines del Motor derecho visto desde primera persona
motor_B_pin1 = 26
motor_B_pin2 = 21
motor_B_ctrl = 4
pwm_B = 0

def setup(): # Definicion de estados
    global pwm_B
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) # Usa los pines de GPIO
    """
    GPIO.setup(motor_A_pin1, GPIO.OUT)
    GPIO.setup(motor_A_pin2, GPIO.OUT)
    GPIO.setup(motor_A_ctrl, GPIO.OUT)
    """
    GPIO.setup(motor_B_pin1, GPIO.OUT)
    GPIO.setup(motor_B_pin2, GPIO.OUT)
    GPIO.setup(motor_B_ctrl, GPIO.OUT)

       # pwm_A = GPIO.PWM(motor_A_ctrl, 1000)
    pwm_B = GPIO.PWM(motor_B_ctrl, 1000)
    
    
"""
def delante_izquierda():
    GPIO.output(motor_A_pin1, GPIO.HIGH)
    GPIO.output(motor_A_pin2, GPIO.LOW)
    pwm_A.start(0)
    sleep(1)
    pwm_A.ChangeDutyCycle(40)
    sleep(1)
    pwm_A.ChangeDutyCycle(100)
"""
def delante_derecha():
    GPIO.output(motor_B_pin1, GPIO.HIGH)
    GPIO.output(motor_B_pin2, GPIO.LOW)
    pwm_B.start(0)
    print("velocidad 0")
    sleep(0.5)
    pwm_B.ChangeDutyCycle(40)
    print("velocidad 40")
    sleep(5)
    pwm_B.ChangeDutyCycle(80)
    print("velocidad 80")
    sleep(5)
    pwm_B.ChangeDutyCycle(0)
    print("velocidad 0")
    sleep(5)
    pwm_B.stop()
def atras():
    GPIO.output(motor_B_pin1, GPIO.LOW)
    GPIO.output(motor_B_pin2, GPIO.HIGH)
def stop():
    GPIO.output(motor_B_pin1, GPIO.LOW)
    GPIO.output(motor_B_pin2, GPIO.LOW)
def destroy():
    stop()
    GPIO.cleanup()
    print("Saliendo")
def void_loop():
     delante_derecha()
     sleep(1)

if __name__ == '__main__':

    try:

        #--configuracion--
        setup()
        #-----------------

        while 1: #ciclo principal
            void_loop()

    except KeyboardInterrupt:
        destroy()

