# Robot Information Scraper
# Noah Kim

# Import
import argparse
import json
import sys

import requests

# Constant
DESCRIPTION = "Retrieves data from the Blue Alliance API and stores it in the Scoutmaster 9001 database."
EPILOG = "(c) 2015 Noah Kim, Antares Chen; Team 449"

TEAMS_BY_NUMBER = "http://www.thebluealliance.com/api/v2/team/frc%s"
TEAMS_BY_EVENT = "http://www.thebluealliance.com/api/v2/event/%s/teams"
REQUEST_HEADERS = {"X-TBA-App-Id": "frc449:scoutmaster:v02"}

def scrape(key, url):
    response = requests.get(url%str(key), headers=REQUEST_HEADERS)
    json_data = json.loads(response.text)
    return json_data

sys.argv += ["-t", "449"]

parser = argparse.ArgumentParser(description=DESCRIPTION, epilog=EPILOG)
parser.add_argument("-t", "--team", help="Team number to retrieve data from", metavar="<team #>", nargs="*", type=int)
parser.add_argument("-e", "--event", help="Event to retrieve teams' data from", metavar="\"<event key>\"")
parser.add_argument("-o", "--overwrite", help="Overwrite previous team data", action="store_true")
args = parser.parse_args()

if args.team and args.region:
    print("You cannot look up a team and a region at the same time!", file=sys.stderr)
elif not (args.team or args.region):
    print("Please specify what to look up!", file=sys.stderr)

for team in args.team:
    print(scrape(team, TEAMS_BY_NUMBER))
for event in args.event:
    print(scrape(event, TEAMS_BY_EVENT))