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
	return response.json()


def get_events(year):
	return scrape(year, DEFAULT_EVENT)


def get_matches(event):
	return scrape(event, MATCHES_BY_EVENT)


def get_rankings(event):
	return scrape(event, RANKING_BY_EVENT)


def get_teams(event):
	return scrape(event, DEFAULT_TEAMS_BY_EVENT)


def get_matches_by_team(team, event):
	return scrape((team, event), EVENT_MATCHES_BY_TEAM)



