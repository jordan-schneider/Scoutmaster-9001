#!/usr/bin/python3
import dataset
import conf

# Database
db = None

def init():
    """Initialize the database"""
    global db
    db = dataset.connect(conf.lookup("db"))

def get_table(name):
    """Get a table from the database"""
    return db.load_table(name)

def add_table(name):
    """Add a new table to the database"""
    return db.create_table(name)

