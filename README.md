# Scoutmaster-9001
Behold, the much awaited for update to the uncompleted scoutmaster 9000! SCOUTMASTER 9001. This application will efficiently facilitate synergistic utilization of next-generation scalable web technology with an unparalleled client-server architecture. And...

SYNERGY

## Root URL
* /
** GET - Redirect to /login if not logged in, or /teams if logged in

## User API
* /login
** GET - Login form
** POST - User login request
* /logout
** GET/POST - Log out of a session
* /user
** GET - Get list of users
* /user/%d
** GET - Show user information
** POST - Set user information

## Team API
* /teams
** GET - Get list of teams
* /teams/%d
** GET - Get team data
** POST - Post pictures and reviews

## Match API
* /matches
** GET - Match data
* /matches/%s/%d
** GET - Specific match
