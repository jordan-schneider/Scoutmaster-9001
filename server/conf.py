#!/usr/bin/python3

import json

conf = json.loads(open("conf.json", "rb"))


def lookup(key):
	'''Returns constants from conf.json in python dict format'''

	# try looking things up by first level keys
	try:
		return conf[key]
	# if no key
	except KeyError as e:
		print("[!]KeyError: %s" % key)

