import database, user_handler, match_handler, server

if __name__ == "__main__":
    database.init()
    user_handler.init()
    match_handler.init()
    server.init()
