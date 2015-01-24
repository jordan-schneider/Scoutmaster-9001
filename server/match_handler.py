#!/usr/bin/python3

import database as db
import conf




def get_match_list():
	

def get_match(number):


def add_match():


def remove_match():


def edit_match():





def init():
	"""Initializes the regional handler"""
	global regional

	# Set global 
	try:
        regional = db.get_table("regionals")
    except:
        # Create the user table
        regional = database.add_table("regionals")