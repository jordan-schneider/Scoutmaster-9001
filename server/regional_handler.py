#!/usr/bin/python3

import database as db
import conf




def create_team_list():
	"""Fills a table with the list of teams at the respective regional"""
	

def get_team_list():
	"""Returns a list of teams at a regional"""



def init():
	"""Initializes the regional handler"""
	global regional

	# Set global 
	try:
        regional = db.get_table("regionals")
    except:
        # Create the user table
        regional = database.add_table("regionals")