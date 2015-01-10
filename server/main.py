import database, usermgr, server

if __name__ == "__main__":
    database.init()
    usermgr.init()
    server.server_init()
