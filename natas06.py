#!/bin/python3

import requests
import sys

if len(sys.argv) < 1:
	print(f'Usage: python3 {sys.argv[0]} <url>')
else:
	#Commented code below lso works:
	#session = requests.Session()
	#payload = {'secret':'FOEIUWGHFEEUHOFUOIU', 'submit': 'Submit+Query'}
	#s = session.post(f'{sys.argv[1]}', data=payload, auth=('natas6', 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'))
	#print(s.status_code)
	#print(s.text)
	payload = {'secret':'FOEIUWGHFEEUHOFUOIU', 'submit': 'Submit+Query'}
	r = requests.post(f'{sys.argv[1]}', data=payload, auth=('natas6', 'aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'))
	print(r.status_code)
	print(r.text)
