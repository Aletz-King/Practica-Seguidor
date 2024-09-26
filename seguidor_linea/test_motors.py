import RPi.GPIO as GPIO
from time import sleep

# Pines del Motor izquierdo visto desde primera persona

motor_A_pin1 = 27
motor_A_pin2 = 18
motor_A_ctrl = 17
pwm_A = 0

# Pines del Motor derecho visto desde primera persona
motor_B_pin1 = 26
motor_B_pin2 = 21
motor_B_ctrl = 4
pwm_B = 0

def setup(): # Definicion de estados
    global pwm_A, pwm_B
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM) # Usa los pines de GPIO
    # Definicion para motor izquierdo
    GPIO.setup(motor_A_pin1, GPIO.OUT)
    GPIO.setup(motor_A_pin2, GPIO.OUT)
    GPIO.setup(motor_A_ctrl, GPIO.OUT)
    # Definicion para motor derecho
    GPIO.setup(motor_B_pin1, GPIO.OUT)
    GPIO.setup(motor_B_pin2, GPIO.OUT)
    GPIO.setup(motor_B_ctrl, GPIO.OUT)
    try:
        pwm_A = GPIO.PWM(motor_A_ctrl, 1000)
        pwm_B = GPIO.PWM(motor_B_ctrl, 1000)
    except:
        pass
    

def motor_izquierdo(encendido, velocidad):
    if encendido==0:
        GPIO.output(motor_A_pin1, GPIO.LOW)
        GPIO.output(motor_A_pin2, GPIO.LOW)
        pwm_A.stop()
    else:
        GPIO.output(motor_A_pin1, GPIO.HIGH)
        GPIO.output(motor_A_pin2, GPIO.LOW)
        pwm_A.start(0)
        pwm_A.ChangeDutyCycle(velocidad)


def delante_derecha():
    GPIO.output(motor_B_pin1, GPIO.HIGH)
    GPIO.output(motor_B_pin2, GPIO.LOW)
    pwm_B.start(0)
    sleep(1)
    pwm_B.ChangeDutyCycle(40)
    sleep(1)
    pwm_B.ChangeDutyCycle(100)


def stop():
    GPIO.output(motor_B_pin1, GPIO.LOW)
    GPIO.output(motor_B_pin2, GPIO.LOW)
    GPIO.output(motor_A_pin1, GPIO.LOW)
    GPIO.output(motor_A_pin2, GPIO.LOW)
def destroy():
    stop()
    GPIO.cleanup()
    print("Saliendo")
def void_loop():
    motor_izquierdo(1, 40)
    sleep(5)
    motor_izquierdo(0, 100)
    sleep(2)
    motor_izquierdo(1, 80)
    sleep(5)
    stop()
    sleep(2)

if __name__ == '__main__':

    try:

        #--configuracion--
        setup()
        #-----------------

        while 1: #ciclo principal
            void_loop()

    except KeyboardInterrupt:
        destroy()

