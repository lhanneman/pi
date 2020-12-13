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

# distance variables
MAX_DISTANCE=200 # light off over 100 cm out
KEEP_GOING=70 # show green when we're within 200cm
GETTING_CLOSE=50 # show yellow as we approach the final parking spot

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(GREEN,GPIO.OUT)
GPIO.setup(YELLOW,GPIO.OUT)
GPIO.setup(RED,GPIO.OUT)

def off():
	GPIO.output(RED,GPIO.LOW)
	GPIO.output(YELLOW,GPIO.LOW)
	GPIO.output(GREEN,GPIO.LOW)

def green():
	GPIO.output(GREEN,GPIO.HIGH)
	GPIO.output(YELLOW,GPIO.LOW)
	GPIO.output(RED,GPIO.LOW)

def yellow():
	GPIO.output(GREEN,GPIO.LOW)
	GPIO.output(YELLOW,GPIO.HIGH)
	GPIO.output(RED,GPIO.LOW)

def red():
	GPIO.output(GREEN,GPIO.LOW)
	GPIO.output(YELLOW,GPIO.LOW)
	GPIO.output(RED,GPIO.HIGH)

def get_distance():
	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)
	start = time.time()
	while GPIO.input(ECHO) == 0:
		start = time.time()
	while GPIO.input(ECHO) == 1:
		end = time.time()
	elapsed = end - start
	distance = (elapsed * 34300) / 2
	return distance

# def calculate_average():
#   # This function takes 3 measurements and returns the average.
#   distance1=get_distance()
#   time.sleep(0.1)
#   distance2=get_distance()
#   time.sleep(0.1)
#   distance3=get_distance()
#   distance = distance1 + distance2 + distance3
#   distance = distance / 3
#   return distance

def test():
	green()
	time.sleep(0.5)
	yellow()
	time.sleep(0.5)
	red()
	time.sleep(0.5)
	off()
	

# light test
test()
GPIO.output(TRIG,False)

time.sleep(5)

try:
	while True:
		distance = get_distance()
		time.sleep(0.05)
		
		if distance > MAX_DISTANCE:
			off()
		elif distance > KEEP_GOING:
			green()
		elif distance > GETTING_CLOSE:
			yellow()
		else:
			red()
		time.sleep(2)


except KeyboardInterrupt:
	# User pressed CTRL-C
	# Reset GPIO settings
	off()
	GPIO.cleanup()
