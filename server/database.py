#!/usr/bin/python3
import sqlite3
import dataset
conn = sqlite3.connect('database.db')
db = dataset.connect('sqlite:///database.db')

# Initialize the database
def db_init():
    pass

