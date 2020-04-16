#!/usr/bin/python

#Libraries
from datetime import datetime
import RPi.GPIO as GPIO
import time
import log_count
import ultra_sonic

# This script must be run as root for GPIO to work!
if not os.geteuid()==0:
        print('must run as root for GPIO to work!')
        exit()

constants = []
try:
	calibration_data = open('calibration_readings.txt', 'r') 
        data = calibration_data.readlines()
	for line in data:
		constants.append(line)
except:
	print('Run calibrate.py to set distance constants!')
	exit()


bounces_from_today = log_count.count_bounces()
print('Previous logged bounces from today:  '+str(bounces_from_today))
print('')
print('Starting the bounce counter!')


if __name__ == '__main__':
    try:
	avg_max_deflection= float(constants[1])
	state = 'up'
	bounce = bounces_from_today
        while True:
	    start = datetime.now()
            deflection = ultra_sonic.distance()
            time.sleep(.025)
	    if deflection >= avg_max_deflection and state == 'up':
		state = 'down'
		bounce += 1
		print(bounce)
	    	f = open('/var/www/html/bounce.txt','w')
	    	f.write(str(bounce))
	    	f.close()
	    	log = open('bounce.log','a')
		log.write(str(datetime.now())+","+str(bounce)+","+str(deflection)+"\n")
		log.close()
            if deflection < avg_max_deflection and state == 'down':
		state = 'up'

# Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
