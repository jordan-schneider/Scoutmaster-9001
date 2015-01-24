import datetime
import conf, database, scraper


# Current year
year = datetime.date.today().year


# Event list table in the database
events = None


# Initialize the event handler
def init():
    # Create the event table if it doesn't exist
    global events
    try:
        events = database.get_table("events")
    except:
        # Create the event table
        events = database.add_table("events")

        # Override the current year if it's in the configuration file
        try:
            year = conf.lookup("year")
        except:
            pass

        # Get a list of events from the Blue Alliance API and add it
        eventes.insert(scraper.get_events(year))
