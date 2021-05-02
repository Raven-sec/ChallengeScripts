#!/bin/python3

import requests
import sys

if len(sys.argv) < 1:
	print(f'Usage: python3 {sys.argv[0]} <url>')
else:
	r = requests.get(f'{sys.argv[1]}', headers={'Referer': 'http://natas5.natas.labs.overthewire.org/'}, auth=('natas4', 'Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'))
	print(r.headers)
	print(r.status_code)
	print(r.text)
