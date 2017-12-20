import cv2
import proximity
import newUser
import time
import lcd

THRESHOLD = 100

def takePicture():
    vc = cv2.VideoCapture(0)
    rval, frame = vc.read()
    if rval == True:
        cv2.imwrite("image.jpg", frame)

def doTask():
    lcd.lcd_print("Taking Picture")
    takePicture()
    #time.sleep(1)
    newUser.main()

if __name__=="__main__":
    lcd.lcd_init()
    proximity.proximity_init()
    distance = proximity.proximity_getDistance()
    while True:
	if distance <= THRESHOLD:
	    doTask()
        distance = proximity.proximity_getDistance()
        lcd.lcd_print("Waiting...")
        time.sleep(1)