# -*- coding: utf-8 -*-

import helpers.boobankCommands as boobank
import helpers.objectTypes as types
from helpers.pretty import pretty_print
from helpers.configure import configure_backends, erase_credentials
from helpers.serializer import serialize
import webbrowser
import os



filename = '/root/src/weboobToFile/files/test.json'


def process_boobank():
	bank = dict()
	bank['name'] = 'Jean-Mi'
	bank['accounts'] = boobank.get_accounts()
	
	for account in bank['accounts']:
		account['type'] = types.set_account_type(account['type'])

		account.update({'coming_operations': []})
		account['coming_operations'] = boobank.get_coming(account['id'])

		account.update({'transactions': []})
		account['transactions'] = boobank.get_transactions(account['id'])
		
		for transaction in account['transactions']:
			transaction['type'] = types.set_transaction_type(transaction['type'])
	
	return bank

def main():
	configure_backends()
	os.system("chmod 666 /root/.config/weboob/backends")
	os.system("chmod 666 /root/.config/weboob/sources.list")
	boobank.weboob_update()

	bank = dict()
	bank = process_boobank()
	if not bank:
		bank['Error'] = 'Fail to execute Boobank..'

	erase_credentials()
	serialize(bank)
	os.system('cat %s' % (filename))