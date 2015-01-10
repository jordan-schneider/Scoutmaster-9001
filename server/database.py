#!/usr/bin/python3
import dataset
import json

# Database
db = None

def init():
    """Initialize the database"""
    global db
    conf = json.loads(open("db.json").read())
    db = dataset.connect(conf["db"])

def get_table(name):
    """Get a table from the database"""
    return db.get_table(name)

def add_table(name):
    """Add a new table to the database"""
    return db.create_table(name)

