#!/bin/python3

import requests
import sys

if len(sys.argv) < 1:
	print(f"Usage: python3 {sys.argv[0]} <url>")
else:
	r = requests.get(f"{sys.argv[1]}", auth=("natas0", "natas0"))
	print(r.headers)
	print(r.status_code)
	print(r.text)
	
