import RPi.GPIO as GPIO
import time

red = 11
green = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.output(red, GPIO.HIGH)
time.sleep(1)
f = open("test.txt", "w")
f.write("sample words\n")
f.write(str(time.time()))
f.close()


GPIO.output(red, GPIO.LOW)
GPIO.output(green, GPIO.HIGH)
time.sleep(1)
GPIO.output(green, GPIO.LOW)
GPIO.cleanup();