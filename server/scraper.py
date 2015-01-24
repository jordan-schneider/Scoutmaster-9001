# Robot Information Scraper
# Noah Kim

# Imports
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


# Scraper function
def scrape(key, url):
	response = requests.get(url%key, headers=REQUEST_HEADERS)
	json_data = json.loads(response.text)
	# with open("output.json", "w") as f:
	# 	f.write(json.dumps(json_data))
	return json_data


def get_events(year):
	response = requests.get(DEFAULT_EVENT%year, headers=REQUEST_HEADERS)
	return json.loads(response.text)


def get_matches(event):
	response = requests.get(MATCHES_BY_EVENT%event, headers=REQUEST_HEADERS)
	return json.loads(response.text)


def get_rankings(event):
	response = requests.get(RANKING_BY_EVENT%event, headers=REQUEST_HEADERS)
	return json.loads(response.text)


def get_teams(event):
	response = requests.get(DEFAULT_TEAMS_BY_EVENT%event, headers=REQUEST_HEADERS)
	return json.loads(response.text)





