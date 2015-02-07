import database
import user_handler
import match_handler
import server

if __name__ == "__main__":
	print("SENTINEL")
    database.init()
    user_handler.init()
    match_handler.init()
    server.init()
