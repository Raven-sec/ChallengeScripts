#!/bin/python3

import base64
import requests
import sys

url = sys.argv[1]
hexString = sys.argv[2]

if len(sys.argv) < 1:
	print(f'Usage: python3 {sys.argv[0]} <url> <hex string>')
else:
	part1 = bytes.fromhex(f'{sys.argv[2]}').decode('utf-8')
	part2 = part1.encode('ascii')
	part3 = part2[::-1]
	part4 = base64.b64decode(part3)
	part5 = part4.decode('ascii')
	payload = {'secret':f'{part5}', 'submit': 'Submit+Query'}
	r = requests.post(f'{url}', data=payload, auth=('natas8', 'DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'))
	print(r.status_code)
	print(r.text)
	
#Resources used
#https://stackoverflow.com/questions/3470546/python-base64-data-decode
#https://stackoverflow.com/questions/931092/reverse-a-string-in-python
#https://stackoverflow.com/questions/54855296/how-do-i-encode-hexadecimal-to-base64-in-python
#https://stackoverflow.com/questions/3283984/decode-hex-string-in-python-3
#https://stackabuse.com/encoding-and-decoding-base64-strings-in-python/
