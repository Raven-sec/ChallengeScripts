#!/bin/python3

#Based on Null bytes tool: https://null-byte.wonderhowto.com/how-to/build-directory-brute-forcing-tool-python-0169477/

#Modules
import pyfiglet
import os
import requests
import sys


#What we need to supply
url = sys.argv[1]
wordlist = sys.argv[2]


#Convinient newline function
def nl():
	print('\n')

#Tuples, as we don't want the list to be erased
success = list()
redirects = list()
other = list()

script_name = pyfiglet.figlet_format('PyWebBruteforcer')
print(script_name)
print(f'Usage guide: python3 {sys.argv[0]} <url> <wordlist>')
nl()
try:
	print('[*]Parsing Wordlist...')
	try:
		with open(f'{wordlist}', 'r') as f:
			to_check = f.read().split('\n')
	except IOError:
		print(f'[!] Could not read from {wordlist}')
		sys.exit(1)
	else:	
		print(f'Total Paths to check: {len(to_check)}')
		nl()
		print('[*] Starting Enumeration')
		for i in range(len(to_check)):
			word = to_check[i]
			r = requests.get(f'{url}/{word}', auth=('natas2','ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'))
			if r.status_code == 200 and len(r.content) > 0:
				print(f'Success for path: {word}')
				success.append(to_check)
			elif r.status_code == 301:
				print(f'Permenant Redirect \({r.status_code}\) on: {word}')
				data1 = (url,r.history)
				redirects.append(data1)
			elif r.status_code == 302:
				print(f'Temporary Redirect \({r.status_code}\) on: {word}')
				data2 = (url,r.history)
				redirects.append(data2)
			elif r.status_code == 303:
				print(f'Temporary Redirect \({r.status_code}\) on: {word}')
				data3 = (url,r.history)
				redirects.append(data3)
			elif r.status_code == 307:
				print(f'Temporary Redirect \({r.status_code}\) on: {word}')
				data4 = (url,r.history)
				redirects.append(data4)           
			else:
				print(f'Returned status code {r.status_code} on: {word}')
				data5 = (url,r.history)
				other.append(data5)
	print('[+] Enumeration complete')
	nl()
	print(f'Discovered directories: {success}')		 
	nl()
	print(f'Redirects: {redirects}')
	nl()
	print(f'Other URL\'s: {other}')
	decision = input('Write to files? y or n ')
	if decision == 'y':
		f = open('success.txt', 'w')
		for a in success:
			line = ' '.join(str(x) for x in a)
			f.write(line + '\n')
		f.close()
		f = open('redirects.txt', 'w')
		for b in redirects:
			line = ' '.join(str(x) for x in b)
			f.write(line + '\n')
		f.close()
		f = open('other.txt', 'w')
		for c in other:
			line = ' '.join(str(x) for x in c)
			f.write(line + '\n')
		f.close()
		print('Files created!')
		sys.exit(1)
	elif decision == 'n':
		print(f'Exiting {sys.argv[0]}...')
		sys.exit(1)
	else:
		print('Please supply \'y\' or \'n\'')
		sys.exit(1)


except KeyboardInterrupt:
	print(f'Exiting {sys.argv[0]}')
	sys.exit(1)

except requests.exceptions.RequestException as er :
	print(f'Server returned error {er}')    

