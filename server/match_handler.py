import database as db
import conf
import scraper


# Current year
current_year = conf.lookup("year")


# Matches database holds all the matches for all events
matches = None

# Events database holds all the information on events
events = None
events_collection = None


def get_match(event, qual, number):
    # Match ID
    match_id = event + "_"

    # Convert the qualification into a BlueAlliance value
    if qual == "final":
        match_id += "f1"
    elif qual[:6] == "sfinal":
        match_id += "sf" + qual[6:]
    elif qual[:6] == "qfinal":
        match_id += "qf" + qual[6:]
    elif qual == "qual":
        match_id += "qm"

    # Add the match number
    match_id += 'm' + str(number)

    # Look up and return the match
    matches = database.get_table(event)
    return matches.find_one(key=match_id)


def refresh_events(year=current_year):
    """Refreshes all the events in that year. This function will always force an update"""

    print("Refreshing events database!")

    event_list = scraper.get_events(year, force=True)
    for event in event_list:
        
        # Delete the alliances information in event json and add to collection
        del(event["alliances"])
        db.update_document(events, events_collection, "key", event)



def refresh_matches(force, events=[], year=current_year):
    """Refreshes all the matches in given by the events field."""

    print("Refreshing matches database!")

    # If no events are predefined then refresh all events.
    if events == []:

        # Get the list of events
        scraped_information = scraper.get_events(year, force=True)
        
        # For all events append the event key to the list to be processed
        for event in scraped_information:
            events.append(event["key"])
    
    # Iterate through all event keys
    for event_key in events:
        
        try:

            # Check if the collection 
            print("\nFind the collection: " + event_key)

            event_collection = db.get_collection(matches, event_key).name
        
        except db.CollectionNotFoundException:
            

            print("Collection Not found creating new one!")

            # Add the collection and force all events to be refreshed
            event_collection = db.add_collection(matches, event_key).name

        try:
            match_list = scraper.get_matches(event_key, force=force)
            print("Adding matches!")
            for match in match_list:
                db.update_document(matches, event_collection, "key", match)

        except scraper.UpdateNotFoundException:
            print("No update found!")


def init():
    """Initialize the event handler"""

    # Create the event table if it doesn't exist
    global matches
    global events
    global events_collection

    try:

        # Check if the database exists
        matches = db.get_database("matches").name
        events = db.get_database("events").name
        events_collection = db.get_collection(events, "events").name

    except db.DatabaseNotFoundException:

        # Create the matches database
        matches = db.add_database("matches").name

        # Create the events database
        events = db.add_database("events").name
        events_collection = db.add_collection(events, "events").name
        refresh_events()

    except db.CollectionNotFoundException:

        # Create the events table in the events database
        events_collection = db.add_collection(events, "events").name
        refresh_events()

    finally:

        # Refresh information on all events in the database
        refresh_matches(False)
