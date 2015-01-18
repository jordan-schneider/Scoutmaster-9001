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

EVENTS_BY_YEAR = "http://www.thebluealliance.com/api/v2/events/%s"
TEAMS_BY_NUMBER = "http://www.thebluealliance.com/api/v2/team/frc%s"
TEAMS_BY_EVENT = "http://www.thebluealliance.com/api/v2/event/%s/teams"
REQUEST_HEADERS = {"X-TBA-App-Id": "frc449:scoutmaster:v02"}


# Scraper function
def scrape(key, url):
	response = requests.get(url%str(key), headers=REQUEST_HEADERS)
	json_data = json.loads(response.text)
	# with open("output.json", "w") as f:
	# 	f.write(json.dumps(json_data))
	return json_data

# Parser settings
parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
parser.add_argument("-y", "--year", help="Year to retrieve event list from", metavar="<year #>", nargs="*", type=int)
parser.add_argument("-t", "--team", help="Team number to retrieve data from", metavar="<team #>", nargs="*", type=int)
parser.add_argument("-e", "--event", help="Event to retrieve teams' data from", metavar="\"<event key>\"", nargs="*", type=str)
parser.add_argument("-o", "--overwrite", help="Overwrite previous team data", action="store_true")
args = parser.parse_args()


# if args.team and args.event:
#     print("You cannot look up a team and a region at the same time!", file=sys.stderr)
# elif not (args.team or args.event):
#     print("Please specify what to look up!", file=sys.stderr)

# More parser settings
if args.year:
	for year in args.year:
		print(scrape(year, EVENTS_BY_YEAR))
if args.team:
	for team in args.team:
	    print(scrape(team, TEAMS_BY_NUMBER))
if args.event:
	for event in args.event:
		print(scrape(event, TEAMS_BY_EVENT))


