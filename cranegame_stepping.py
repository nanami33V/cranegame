import RPi.GPIO as GPIO
from time import sleep
import sys

SW_GPIOx = 23
PS_PINx = 22 
IN_A_PINx = 17
IN_B_PINx = 27
STEP_ANGLE = 1.8
countx = 0

STEP_ANGLE = 1.8

SW_GPIOy = 24
PS_PINy = 21 
IN_A_PINy = 16
IN_B_PINy = 20
county = 0

SW_GPIOz = 23
PS_PINz = 22 
IN_A_PINz = 17
IN_B_PINz = 27

Servo_pin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(Servo_pin, GPIO.OUT) 

Servo = GPIO.PWM(Servo_pin, 50)     #GPIO.PWM(ポート番号, 周波数[Hz])
Servo.start(0)

#GPIO.setup(SW_GPIOx, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW_GPIOy, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SW_GPIOz, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#x軸y軸z軸のモーター制御
def rotateCwx(speed, degree):
    d = int(degree / STEP_ANGLE / 4)
    for i in range(d):
        GPIO.output(IN_A_PINx, True)
        GPIO.output(IN_B_PINx, True)
        sleep(speed)
        
        GPIO.output(IN_A_PINx, False)
        GPIO.output(IN_B_PINx, True)
        sleep(speed)

        GPIO.output(IN_A_PINx, False)
        GPIO.output(IN_B_PINx, False)
        sleep(speed)

        GPIO.output(IN_A_PINx, True)
        GPIO.output(IN_B_PINx, False)
        sleep(speed)

def rotateCcwx(speed, degree):  
    d = int(degree / STEP_ANGLE / 4)
    for i in range(d):
        GPIO.output(IN_A_PINx, True)
        GPIO.output(IN_B_PINx, True)
        sleep(speed)

        GPIO.output(IN_A_PINx, True)
        GPIO.output(IN_B_PINx, False)
        sleep(speed)

        GPIO.output(IN_A_PINx, False)
        GPIO.output(IN_B_PINx, False)
        sleep(speed)

        GPIO.output(IN_A_PINx, False)
        GPIO.output(IN_B_PINx, True)
        sleep(speed)
        
def rotateCwy(speed, degree):
    d = int(degree / STEP_ANGLE / 4)
    for i in range(d):
        GPIO.output(IN_A_PINy, True)
        GPIO.output(IN_B_PINy, True)
        sleep(speed)
        
        GPIO.output(IN_A_PINy, False)
        GPIO.output(IN_B_PINy, True)
        sleep(speed)

        GPIO.output(IN_A_PINy, False)
        GPIO.output(IN_B_PINy, False)
        sleep(speed)

        GPIO.output(IN_A_PINy, True)
        GPIO.output(IN_B_PINy, False)
        sleep(speed)

def rotateCcwy(speed, degree):  
    d = int(degree / STEP_ANGLE / 4)
    for i in range(d):
        GPIO.output(IN_A_PINy, True)
        GPIO.output(IN_B_PINy, True)
        sleep(speed)

        GPIO.output(IN_A_PINy, True)
        GPIO.output(IN_B_PINy, False)
        sleep(speed)

        GPIO.output(IN_A_PINy, False)
        GPIO.output(IN_B_PINy, False)
        sleep(speed)

        GPIO.output(IN_A_PINy, False)
        GPIO.output(IN_B_PINy, True)
        sleep(speed)
        
def rotateCwz(speed, degree):
    d = int(degree / STEP_ANGLE / 4)
    for i in range(d):
        GPIO.output(IN_A_PINz, True)
        GPIO.output(IN_B_PINz, True)
        sleep(speed)
        
        GPIO.output(IN_A_PINz, False)
        GPIO.output(IN_B_PINz, True)
        sleep(speed)

        GPIO.output(IN_A_PINz, False)
        GPIO.output(IN_B_PINz, False)
        sleep(speed)

        GPIO.output(IN_A_PINz, True)
        GPIO.output(IN_B_PINz, False)
        sleep(speed)

def rotateCcwz(speed, degree):  
    d = int(degree / STEP_ANGLE / 4)
    for i in range(d):
        GPIO.output(IN_A_PINz, True)
        GPIO.output(IN_B_PINz, True)
        sleep(speed)

        GPIO.output(IN_A_PINz, True)
        GPIO.output(IN_B_PINz, False)
        sleep(speed)

        GPIO.output(IN_A_PINz, False)
        GPIO.output(IN_B_PINz, False)
        sleep(speed)

        GPIO.output(IN_A_PINz, False)
        GPIO.output(IN_B_PINz, True)
        sleep(speed)
        
def setupx():
    GPIO.setup(IN_A_PINx, GPIO.OUT)
    GPIO.setup(IN_B_PINx, GPIO.OUT)
    GPIO.setup(PS_PINx, GPIO.OUT)
    
def setupy():
    GPIO.setup(IN_A_PINy, GPIO.OUT)
    GPIO.setup(IN_B_PINy, GPIO.OUT)
    GPIO.setup(PS_PINy, GPIO.OUT)

def setupz():
    GPIO.setup(IN_A_PINz, GPIO.OUT)
    GPIO.setup(IN_B_PINz, GPIO.OUT)
    GPIO.setup(PS_PINz, GPIO.OUT)
    GPIO.setup(Servo_pin, GPIO.OUT)

    
    GPIO.output(PS_PINz, False)
    GPIO.output(IN_A_PINz, False)
    GPIO.output(IN_B_PINz, False)
    sleep(0.5)
    
def servo_angle(angle):
    duty = 2.5 + (12.0- 2.5) * (angle + 90) / 180   #角度からデューティ比を求める
    Servo.ChangeDutyCycle(duty)     #デューティ比を変更
    sleep(0.3)
    
def mainx():
    rotateCwx(0.003,10)
    sleep(0.003)
    
def mainy():
    rotateCwy(0.003,10)
    sleep(0.003)
    
def mainz():
    rotateCwz(0.003,720)
    sleep(3)
    servo_angle(50)
    Servo.stop()
    GPIO.cleanup()
    sleep(1)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Servo_pin, GPIO.OUT)
    setupy()
    setupz()
    sleep(1)
    rotateCwz(0.003,720)
    sleep(3)
    
#巻き戻し
def mainxb():
    rotateCcwx(0.003,10)
    sleep(0.003)
    
def mainyb():
    rotateCcwy(0.003,10)
    sleep(0.003)

     
while True:
    SwitchStatusx = GPIO.input(SW_GPIOx)
    print(SwitchStatusx)
    if SwitchStatusx == 1:#x軸ボタンが押されているか
        
        setupx()
        mainx()
        
        countx = countx + 1
        if countx == 1000:
            break
    if countx != 0 and GPIO.input(SW_GPIOy) == 1:
        break

while True:
    SwitchStatusy = GPIO.input(SW_GPIOy)
    
    if SwitchStatusy == 1:#y軸ボタンが押されているか
        
        setupy()
        mainy()
        
        county = county + 1
        if county == 1000:
            break
    if county != 0 and GPIO.input(SW_GPIOz) == 1:
        break

setupz()
mainz()
for i in range(county):
    setupy()
    mainyb()
    