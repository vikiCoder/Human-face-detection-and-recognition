import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

def proximity_init():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.output(TRIG, False)

    GPIO.setup(ECHO, GPIO.IN)

    time.sleep(1)

def proximity_getDistance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        startTime = time.time()

    while GPIO.input(ECHO) == 1:
        stopTime = time.time()

    return round((stopTime - startTime) * 17150, 2)
    #print ("Distance = " + str(round(d, 2)) + " cm")

def proximity_GPIO_cleanup():
  GPIO.cleanup()
    
def main():
    proximity_init()

    print ("Starting Measurement....")

    while 1:
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            startTime = time.time()

        while GPIO.input(ECHO) == 1:
            stopTime = time.time()

        d = (stopTime - startTime) * 17150
        print ("Distance = " + str(round(d, 2)) + " cm")

        time.sleep(1)

    GPIO.cleanup()

if __name__ == '__main__':

  try:
    main()
  except KeyboardInterrupt:
    pass
  finally:
    GPIO.cleanup()
