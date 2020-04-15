#!/usr/bin/python
from datetime import datetime
import RPi.GPIO as GPIO
import time
import ultra_sonic

ultra_sonic.distance()
def average_distance():
	start = time.time()
	dataset = []
	while time.time()-start < 5:
		dist = ultra_sonic.distance()
        	time.sleep(.025)
		#print(dist)
		dataset.append(dist)
	dist_min = min(dataset)
	dist_max = max(dataset)
	dist_avg = sum(dataset)/len(dataset)
	dist_samples = len(dataset)
	error1 = dist_avg - dist_min
	error2 = dist_max - dist_avg
	if error1 > error2:
		dist_error = error1
	else:
		dist_error = error2
	if dist_avg / 10 < dist_error:
		print('Invalid results for test')
		print('Please rerun!')
		exit()

 	#print "Error min: " + str(error1) + "Error max: " + str(error2)
	#print "Min " + str(dist_min)
	#print "Max " + str(dist_max)
	#print "Avg " + str(dist_avg)
	#print "# of samples: " + str(dist_samples)
	return dist_avg
def max_deflection():
	start = time.time()
	dataset = []
	while time.time()-start < 5:
		dist = ultra_sonic.distance()
        	time.sleep(.025)
		#print(dist)
		dataset.append(dist)
	num_samples = len(dataset)
	five_percent_samples = int(num_samples / 10)
	sorted_data = sorted(dataset)
	lowest_10 = sorted_data[:five_percent_samples]
	avg_max_deflection = sum(lowest_5)/len(lowest_5)
	return avg_max_deflection 
try:
	print('Stand still on trampoline')
	time.sleep(3)
	avg_distance = average_distance()
	print avg_distance
	print('Starting Distance: ' + str(round(avg_distance,1)))
	time.sleep(3)
	print('Now jump 5 times')
	time.sleep(3)
	deflection = max_deflection()
	print('Distance deflected during jump: ' + str(deflection))
        f = open('calibration_readings.txt','w')
        f.write(str(avg_distance)+'\n'+str(deflection))
        f.close()
	print('Calibration data saved!')

# Reset by pressing CTRL + C
except KeyboardInterrupt:
	print("Measurement stopped by User")
        GPIO.cleanup()
