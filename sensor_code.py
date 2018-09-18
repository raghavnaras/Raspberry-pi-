import RPi.GPIO as GPIO
from twilio.rest import Client
import time

GPIO_TRIGGER = 18 
GPIO_ECHO = 24


account_sid ="AC7c1252b4cf3901bf025cc9fd437502a3" 
auth_token ="def18d34623bbf59f63164eef2fe4c23" 

client = Client(account_sid, auth_token)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
if __name__ == '__main__': 
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

            if (dist>=20):
            	message = client.api.account.message.create(
            		to="+14089135710", # Put your cellphone number here
					from_="+18315083916", # Put your Twilio number here
					body="Your laundry hamper is full!")
            		


 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()



