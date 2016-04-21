# -*- coding: utf-8 -*-
import json
from subprocess import Popen, PIPE, check_output, CalledProcessError

def weboob_update():
	try:
		print "Updating boobank modules..."
		result = Popen(["weboob-config", "update"], stdout=PIPE).communicate()
	except CalledProcessError as e:
	    print e.output

def edit_backend(name):
	try:
		print "Editing backend..."
		result = Popen(["boobank", "backends", "edit", "", name], stdout=PIPE).communicate()
	except CalledProcessError as e:
	    print e.output

	print result

def get_accounts():
	try:
		print "Scrapping accounts..."
		result = Popen(["boobank", "list", "--count=500", "-f", "json"], stdout=PIPE).communicate()
	except CalledProcessError as e:
	    print e.output

	accounts = json.loads(result[0])
	return accounts

def get_transactions(accountId):
	try:
		print "Scrapping transactions..."
		result = Popen(["boobank", "history", accountId, "--count=500", "-f", "json"], stdout=PIPE).communicate()
	except CalledProcessError as e:
	    print e.output

	transactions = json.loads(result[0])
	return transactions

def get_coming(accountId):
	try:
		print "Scrapping comming transactions..."
		result = Popen(["boobank", "coming", accountId, "--count=500", "-f", "json"], stdout=PIPE).communicate()
	except CalledProcessError as e:
	    print e.output

	coming = json.loads(result[0])
	return coming
