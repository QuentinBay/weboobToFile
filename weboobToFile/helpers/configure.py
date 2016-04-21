# -*- coding: utf-8 -*-
# To configure Boobank with the appropriate backends and credentials

from boobankCommands import edit_backend


import sys
from fileIO import read, write, append, parse_json
from console import ask_bank, ask_done, ask_credentials
import banks as bank


# File containing paths
configFile = "/root/src/weboobToFile/.config"

def switch_to_local_update(sourceFile):
	content = "file:///root/src/weboob/modules"
	write(sourceFile, content)

def get_user_config():
	backends = []
	done = 'n'
	while done is not 'o' and done is not 'O':
		bank.list_banks()
		chosen_bank = ask_bank("Veuillez selectionner votre banque (q pour quitter) :", len(bank.banks))
		if chosen_bank is 'q':
			break
		login = ask_credentials("Numéro client (caché) :")
		password = ask_credentials("Code secret (caché) :")
		backend = {
			"name" : bank.banks[int(chosen_bank)-1]["module"],
			"website" : "pp",
			"login" : login,
			"password" : password
		}
		backends.append(backend)
		done = ask_done("Avez-vous terminé ? (o/n)")
	return backends


def set_modules(backendFile, modules):
	write(backendFile,"")
	for module in modules:
		content = "["+module['name']+"]\n"
		content += "_module = "+module['name']+"\n"
		content += "website = "+module['website']+"\n"
		content += "login = "+module['login']+"\n"
		content += "password = "+module['password']+"\n\n"
		append(backendFile, content)


def configure_backends():
	config = parse_json(configFile)
	switch_to_local_update(config['sourcesFile'])
	print("Bienvenue sur Weboob !")
	backends = get_user_config()
	set_modules(config['backendsFile'], backends)

	
def erase_credentials():
	config = parse_json(configFile)
	configPath = config['backendsFile']
	with open(configPath, 'wb') as file:
		file.write("Secret information erased..\n")

