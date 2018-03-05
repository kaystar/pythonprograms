#! python3
#pvault.py - Dungeon of passwords
import sys
import pyperclip

PASSWORDS = {'email' : 'erger',
             'facebook' : 'sdfrferg',
             'MEW' : 'sds#'
             }

if len(sys.argv) < 2:
    print('Usage: python pvault.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]      # first command line arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + ' copied')
else:
    print("There is no account in the system named " + account)