import RPi.GPIO as GPIO
import time
import YB_Pcb_Car
car=YB_Pcb_Car.YB_Pcb_Car()

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for HC-SR04


# Set up GPIO pins

car.Ctrl_Servo(3,90)

def get_distance(TRIG:int,ECHO:int):
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    # Send a pulse to the sensor
    GPIO.output(TRIG, False)
    time.sleep(.2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Measure the duration of the pulse
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    # Calculate the distance
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance

try:
    while True:
        t=0
       
        car.Car_Back(70,70)
        dist = get_distance(27,22)
            #dist1 = get_distance(6,5)
            #dist2 = get_distance(17,27)
            
        car.Ctrl_Servo(3,88)
        if dist<=80 :
            car.Ctrl_Servo(3,110)
            time.sleep(1.3)
            car.Ctrl_Servo(3,90)
            time.sleep(0.1)
            
        else:
            car.Ctrl_Servo(3,88)
            time.sleep(0.1)
        #if dist<25 or dist==0 or dist>=3000:
            #car.Car_Run(100,100)
           # time.sleep(0.5)
