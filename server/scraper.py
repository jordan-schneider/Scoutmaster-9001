# Robot Information Scraper
# Noah Kim

# Imports
from datetime import datetime
import argparse
import json
import sys
import requests


# Constants
DESCRIPTION = "Retrieves data from the Blue Alliance API and stores it in the Scoutmaster 9001 database."
EPILOG = "(c) 2015 Noah Kim, Antares Chen; Team 449"
REQUEST_HEADERS = {"X-TBA-App-Id": "frc449:scoutmaster:v02"}

DEFAULT_TEAM = "http://www.thebluealliance.com/api/v2/team/frc%s"
EVENT_MATCHES_BY_TEAM = "http://www.thebluealliance.com/api/v2/team/%s/event/%s/matches"

DEFAULT_EVENT = "http://www.thebluealliance.com/api/v2/events/%d"
DEFAULT_TEAMS_BY_EVENT = "http://www.thebluealliance.com/api/v2/event/%s/teams"
# Variable below is redundant
SPECIFIED_TEAMS_BY_EVENT = "http://www.thebluealliance.com/api/v2/team/%s/event/%s/matches"
MATCHES_BY_EVENT = "http://www.thebluealliance.com/api/v2/event/%s/matches"
RANKING_BY_EVENT = "http://www.thebluealliance.com/api/v2/event/%s/rankings"


class UpdateNotFoundException(Exception):
	"""Update not found exception is thrown when the scraped object has not been modified"""

	pass


# Scraper function
def scrape(key, url, force):
	"""Scrapes information from the Blue Alliance API"""

	# If forcing an update, then we will not include an if-modified-since tag

	if not force:
		current_time = datetime.utcnow()
		REQUEST_HEADERS["If-Modified-Since"] = current_time.strftime('%a, %d %b %Y %H:%M:%S GMT')


	print("Getting request: " + str(key))
	# print(REQUEST_HEADERS)
	response = requests.get(url%key, headers=REQUEST_HEADERS)
	
	print(response.status_code)

	# If not modified since, then it returns a 304
	if response.status_code == 304:
		raise UpdateNotFoundException
	return response.json()


def get_events(year, force=False):
	return scrape(year, DEFAULT_EVENT, force)


def get_matches(event, force=False):
	return scrape(event, MATCHES_BY_EVENT, force)


def get_rankings(event, force=False):
	return scrape(event, RANKING_BY_EVENT, force)


def get_teams(event, force=False):
	return scrape(event, DEFAULT_TEAMS_BY_EVENT, force)


def get_matches_by_team(team, event, force=False):
	return scrape((team, event), EVENT_MATCHES_BY_TEAM, force)



