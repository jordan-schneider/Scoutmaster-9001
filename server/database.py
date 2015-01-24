#!/usr/bin/python3
import pymongo
import conf

# Database
db = None


class TableNotFoundException(Exception):
    pass


def get_table(name):
    """Get a table from the database"""
    if name in db.collection_names:
        return pymongo.Collection(db, name)
    raise TableNotFoundException


def add_table(name):
    """Add a new table to the database"""
    return pymongo.Collection(db, name)


def init():
    """Initialize the database"""
    global db
    conn = pymongo.MongoClient("localhost", 9002)
    db = conn[conf.lookup("db")]

