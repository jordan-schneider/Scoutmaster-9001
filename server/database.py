#!/usr/bin/python3
import dataset
import json

db = None


def db_init():
    """Initialize the database"""
    global db
    conf = json.loads(open("db.json").read())
    db = dataset.connect(conf["db"])


def db_get_table(name):
    return db.get_table(name)

