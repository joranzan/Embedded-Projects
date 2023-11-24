# gpio-interrupt-test.py
# GPIO12에 입력이 들어오면 문장을 출력한다
 
# 라이브러리 불러오기
import RPi.GPIO as GPIO 
import time 

# 스위치 눌렸을 때 콜백함수
def switchPressed(channel): 
    print(1)
    print('channel %s pressed!!'%channel) 
 

# GPIO setup 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) 


# interrupt 선언 (버튼이 눌렸는지 확인하고 있는 작은 Thread)
 
GPIO.add_event_detect(12, GPIO.RISING, callback=switchPressed, bouncetime=200) 


# 메인루프
try: 
    while 1: 
        print(".") 
        time.sleep(0.1) 
finally: 
    GPIO.cleanup()
