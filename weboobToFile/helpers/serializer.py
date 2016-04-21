# -*- coding: utf-8 -*-

import json
import time
from pretty import get_pretty_json
import webbrowser

def create_fileName():
	name = str(time.strftime("%d-%m-%YT%H:%M:%S"))+"_comptes_jean-mi.json"
	return name
	# print sum(len(v) for v in content.itervalues())

def write_content(filePath, content):
	content = get_pretty_json(content)
	with open(filePath, 'wb') as file:
		file.write(content+'\n')

def serialize(content):
	filePath = "/root/src/weboobToFile/files/"+create_fileName()
	print "Saving results to file : "+filePath
	write_content(filePath, content)
	webbrowser.open("file://"+filePath)

