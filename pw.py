#! /usr/bin/python3
# pw.py - An insecure password locker program

import sys,pyperclip

# python dict
PASSWORDS = {'email': 'test1',
             'blog': 'test2',
             'luggage': 'test3'}

if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)