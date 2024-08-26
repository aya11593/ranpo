import serial
import time

import YB_Pcb_Car
car=YB_Pcb_Car.YB_Pcb_Car()
car.Ctrl_Servo(3,90)

# Configure the serial port (replace 'COM3' with your port)
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
t=0


def read_ultrasonic_data():
    t=0
    while t<=12:
        
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            try:
                car.Car_Back(25,30)
                car.Ctrl_Servo(3,90)
                # Parse the distances
                distances = line.split(',')
                
                if len(distances) == 2:
                    
                    distance2 = float(distances[0])
                    print(distance2)
                    color=distances[1]     
                    print(color)
                    
                    
                    # Check if the middle sensor reads less than 70 cm
                    '''if distance1 <= 90:
                        car.Ctrl_Servo(3,110)
                        time.sleep(1)
                        car.Ctrl_Servo(3,90)
                        time.sleep(0.1)
                        
                    if distance2 <= 22:
                        car.Ctrl_Servo(3,110)                                                        
                        time.sleep(.4)

                    if distance3 <=22:
                        car.Ctrl_Servo(3,70)
                        time.sleep(.4)'''

                    if color=="b":
                        car.Ctrl_Servo(3,60)
                        time.sleep(1)
                        car.Ctrl_Servo(3,90)
                        time.sleep(0.1)

                    if color=="r" :
                        t+=1
                        print(t)
                        car.Car_Back(70,70)
                        car.Ctrl_Servo(3,120)
                        time.sleep(1.5)

                        car.Ctrl_Servo(3,90)
                        time.sleep(1.6)
                        
                        
                       




                    if color=="w":
                        car.Ctrl_Servo(3,90)

                    car.Ctrl_Servo(3,90)
                    time.sleep(0.1)

            
            except ValueError:
                print("Error parsing data")
        time.sleep(0.1) # Sleep for a short time
    car.Car_Stop()
if _name_ == "_main_":
    read_ultrasonic_data()
