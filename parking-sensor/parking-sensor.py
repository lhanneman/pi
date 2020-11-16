import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)

TRIG=4
ECHO=18
GREEN=17
YELLOW=27
RED=22

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)

def lightsoff():
	GPIO.output(RED,GPIO.LOW)
	GPIO.output(YELLOW,GPIO.LOW)
	GPIO.output(GREEN,GPIO.LOW)

def green_light():
	print("Green")
	GPIO.output(GREEN,GPIO.HIGH)
	GPIO.output(YELLOW,GPIO.LOW)
	GPIO.output(RED,GPIO.LOW)

def yellow_light():
	print("yellow")
	GPIO.output(GREEN,GPIO.LOW)
	GPIO.output(YELLOW,GPIO.HIGH)
	GPIO.output(RED,GPIO.LOW)

def red_light():
	print("red")
	GPIO.output(GREEN,GPIO.LOW)
	GPIO.output(YELLOW,GPIO.LOW)
	GPIO.output(RED,GPIO.HIGH)

def get_distance():
	GPIO.output(TRIG,True)
	time.sleep(0.00001)
	GPIO.output(TRIG,False)
	start = time.time()
	while GPIO.input(ECHO)==0:
		start = time.time()
	while GPIO.input(ECHO)==1:
		end = time.time()
	elapsed = end-start
	distance = (elapsed * 34300)/2
	return distance

def calculate_average():
  # This function takes 3 measurements and returns the average.
  distance1=get_distance()
  time.sleep(0.1)
  distance2=get_distance()
  time.sleep(0.1)
  distance3=get_distance()
  distance = distance1 + distance2 + distance3
  distance = distance / 3
  return distance


GPIO.output(TRIG,False)

# light test
print("beginning light test")
GPIO.output(GREEN,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(YELLOW,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(RED,GPIO.HIGH)
time.sleep(0.5)
lightsoff()

try:
	while True:
		distance = calculate_average()
		time.sleep(0.05)
		print(distance)
		if distance >= 100:
			lightsoff()
		elif distance >= 50:
			green_light()
		elif distance > 30:
			yellow_light()
		else:
			red_light()
		time.sleep(0.5)


except KeyboardInterrupt:
	# User pressed CTRL-C
	# Reset GPIO settings
	lightsoff()
	GPIO.cleanup()
