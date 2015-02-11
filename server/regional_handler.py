#!/usr/bin/python3

import database as db
import conf

current_year = conf.lookup("year")
regional = None


def add_team_review(team, event, review):
	
	"""Adds a review to the team document"""


def add_team_picture(team, event, picture):

	"""Adds a picture to the team document"""

def get_all_teams(event): 

	"""Gets all the teams competing at an event"""


def get_team(team, event=None):

	"""Get all documents that are associated with the specified team"""


def get_team_reviews(team, event=None):

	"""Get all the reviews of a specified team"""


def get_team_pictures(team, event=None):

	"""Get all pictures of a specified team"""


def get_team_statistics(team, event=None):

	"""Get the statistics associated to a specified team"""


def refresh_teams(events=[], year=current_year, force=False):
	
	"""Refresh all team information in the specified events"""

	# if no events specified:
		# fill event array with all events
	# for each event in array:
		# for each team_document in event:
			# get the matches from the match table 
			# commit changes to the stuff


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
        event_list = [] # scrub from scraper
        for event in event_list:
        	event_collection = db.add_collection(regional, event)
        	team_list = [] # scrub from scraper
        	for team in team_list:
        		document = {}

        		db.add_document(regional, event_collection, {})

    

