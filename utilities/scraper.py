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

DEFAULT_EVENT = "http://www.thebluealliance.com/api/v2/event/%s"
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

# Parser settings
parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
parser.add_argument("target", 
					help="Specify the target of the scraper. If an alpha-numeric key is given then the program will target a regional, else it will target a team.",  
					type=str)
parser.add_argument("-e", "--event", 
					help="Scrape the team for its participated events.",  
					nargs="+", 
					type=str)
parser.add_argument("-t", "--team", 
					help="Scrape the event for its participating teams.",
					nargs="*", 
					type=str)
parser.add_argument("-m", "--match", 
					help="Scrape all matches from the target event", 
					action="store_true")
parser.add_argument("-r", "--ranking", 
					help="Scrape the ranking of teams at the target event",
					action="store_true")

parser.add_argument("-o", "--overwrite", help="Overwrite previous team data", action="store_true")
args = parser.parse_args()


# If target is numeric then it is a team code, else event code
if args.target.isnumeric():	
	if args.event:
		for event in args.event:
			print(scrape((args.target, event), EVENT_MATCHES_BY_TEAM))
	else:
		print(scrape(args.target, DEFAULT_TEAM))
else:
	if args.team:
		if len(args.team) == 0:
			print(scrape(args.target, DEFAULT_TEAMS_BY_EVENT))
		else:
			for team in args.team:
				print(scrape((args.target, team), SPECIFIED_TEAMS_BY_EVENT))
	elif args.match:
		print(scrape(args.target, MATCHES_BY_EVENT))
	elif args.ranking:
		print(scrape(args.target, RANKING_BY_EVENT))
	else:
		print(scrape(args.target, DEFAULT_EVENT))



