# Robot Information Scraper
# Noah Kim

# Import
import urllib
import datetime
import json
import re

import bs4
import requests

# Constant
URL_EVENTS = "http://www.thebluealliance.com/api/v2/event/%s/teams"
HEADERS = {"X-TBA-App-Id": "frc449:scoutmaster:v02"}

def get_teams(event_key) -> list:
    """Return the teams that participated in the event specified by event_key.
    Event key should be of the form <YYYY><CODE>."""
    response = requests.get(URL_EVENTS % event_key, headers=HEADERS)
    json_data = json.loads(response.text)
    return json_data

