import RPi.GPIO as GPIO            #GPIO用のモジュールをインポート
import time                        #時間制御用のモジュールをインポート
import sys                         #sysモジュールをインポート

#ポート番号の定義
Servo_pin = 3
Recive_pin = 4

def setup():
    GPIO.setmode(GPIO.BCM)              #GPIOのモードを"GPIO.BCM"に設定
    GPIO.setup(Recive_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(Servo_pin, GPIO.OUT)

#角度からデューティ比を求める関数
def servo_angle(angle):
    Servo = GPIO.PWM(Servo_pin, 50)     #GPIO.PWM(ポート番号, 周波数[Hz])
    Servo.start(0)#Servo.start(デューティ比[0-100%])
    duty = 2.5 + (12.0- 2.5) * (angle + 90) / 180   #角度からデューティ比を求める
    Servo.ChangeDutyCycle(duty)     #デューティ比を変更
    time.sleep(0.3)                 #0.3秒間待つ

#while文で無限ループ
#サーボモータの角度をデューティ比で制御
#Servo.ChangeDutyCycle(デューティ比[0-100%])
try:
    setup()
    servo_angle(0)
    print("servo running")
    
    while True:
        while True:
            SwitchStatus = GPIO.input(Recive_pin)
            if  SwitchStatus == 1:
                print("recived trigger signal")
                servo_angle(45)
                time.sleep(2)
                break
            time.sleep(0.01)
        while True:
            SwitchStatus = GPIO.input(Recive_pin)
            if  SwitchStatus == 1:
                print("recived trigger signal")
                servo_angle(0)
                time.sleep(2)
                break
            time.sleep(0.01)
        
except KeyboardInterrupt:          #Ctrl+Cキーが押された
    GPIO.cleanup()                 #GPIOをクリーンアップ
    sys.exit()                     #プログラムを終了
    
GPIO.cleanup()                 #GPIOをクリーンアップ
sys.exit()                     #プログラムを終了

























