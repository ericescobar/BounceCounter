#!/usr/bin/python
from datetime import datetime
import time

def count_bounces():
	log_file = open('bounce.log', 'r') 
	line = log_file.readlines()
	previous_bounces = 0
	for date in line:
		log_day = date.split(' ')
		if str(log_day[0]) == str(datetime.today().date()):
			previous_bounces += 1
	return previous_bounces
