import RPi.GPIO as GPIO
from twilio.rest import Client
import time
import sys

GPIO_TRIGGER = 18 
GPIO_ECHO = 24


account_sid ="AC7c1252b4cf3901bf025cc9fd437502a3" 
auth_token ="def18d34623bbf59f63164eef2fe4c23" 

client = Client(account_sid, auth_token)

def close(signal,frame):
	print("\n Sensor disconnected \n")
	GPIO.cleanup()
	sys.exit(0)

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

while True:
	# set Trigger to HIGH
	GPIO.output(pinTrigger, True)
	# set Trigger after 0.01ms to LOW
	time.sleep(0.00001)
	GPIO.output(pinTrigger, False)

	startTime = time.time()
	stopTime = time.time()

	# save start time
	while 0 == GPIO.input(pinEcho):
		startTime = time.time()

	# save time of arrival
	while 1 == GPIO.input(pinEcho):
		stopTime = time.time()

	# time difference between start and arrival
	TimeElapsed = stopTime - startTime
	# multiply with the sonic speed (34300 cm/s)
	# and divide by 2, because there and back
	distance = (TimeElapsed * 34300) / 2

	print ("Distance: %.1f cm" % distance)
	time.sleep(1)

	if(distance<=20):
		message = client.api.account.message.create(
			to="+14089135719",
			from_ = "+18315083916",
			message = "Your laundry hamper is full")

