#!/bin/python3

import sys

if len(sys.argv) < 1:
	print("Please provide a password!")
	print(f"Usage: python3 {sys.argv[0]} jsRE_solve.py")
	sys.exit()

if len(sys.argv[1]) < 10 or len(sys.argv[1]) >20:
	print("Password should be more than 10 chars but less than 20 chars!")
	sys.exit()
	
else:
	i =1
	for char in sys.argv[1]:
		i +=ord(char)
		modulo = i % 421
		
	if modulo == 0:
		print(f"You found it! {sys.argv[1]} is the password!")
	else:
		print("Keep going!")
		
	suggest = 421 - modulo
	
	#Nums in http://www.asciitable.com/
	if suggest > 31 and suggest < 127:
		random = chr(suggest)
		print(f"Try adding {random} to the current password")
		print(f"E.g. {sys.argv[1]}\+{random}")

		
