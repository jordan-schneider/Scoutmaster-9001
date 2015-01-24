#!/usr/bin/python3

import json

conf = json.loads(open("scoutmaster.conf", "r").read())

def lookup(key):
	"""Returns constants from conf.json in python dict format"""
	return conf[key]

