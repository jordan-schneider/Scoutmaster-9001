#!/usr/bin/python3

import database as db
import conf

current_year = conf.lookup("year")


def add_team_review(team, event, review):
	

def add_team_picture(team, event, picture):


def get_all_teams(event): 


def get_team(team, event=None):


def get_team_reviews(team, event=None):


def get_team_pictures(team, event=None):


def get_team_statistics(team, event=None):


def refresh_teams(events=[], year=current_year, force=False):
	


def init():
	"""Initializes the regional handler"""
	global regional

	# Set global 
	try:
        
        # Get the regional database
        regional = db.get_database("regionals")

    except db.DatabaseNotFoundException:
        
        # Create the user table
        regional = database.add_database("regionals")

