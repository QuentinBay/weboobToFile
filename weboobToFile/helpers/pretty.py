import json

def pretty_print(jsonContent):
	print json.dumps(jsonContent, sort_keys=True, indent=4, separators=(',', ': '))

def get_pretty_json(jsonContent):
	return json.dumps(jsonContent, sort_keys=True, indent=4, separators=(',', ': '))
