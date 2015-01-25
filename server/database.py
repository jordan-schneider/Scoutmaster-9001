#!/usr/bin/python3
import pymongo
import conf

# Mongo client
client = None
# Default dabatase name (because adding it everywhere would be annoying
db_name = conf.lookup("db_name", "scoutmaster")


class DatabaseNotFoundException(Exception):
    pass


class CollectionNotFoundException(Exception):
    pass


class DocumentNotFoundException(Exception):
    pass


def get_database(name):
    """Get a database from mongodb"""
    if name in client.database_names():
        return client[name]
    raise DatabaseNotFoundException


def add_database(name):
    """Add a database to mongodb"""
    return client[name]


def get_collection(name, db=db_name):
    """Get a table from the database"""
    if name in client[db].collection_names():
        return client[db][name]
    raise CollectionNotFoundException


def add_collection(name, db=db_name):
    """Add a new table to the database"""
    return client[db][name]


def get_document(collection, key, db=db_name):
    """Get a document from the collection"""
    result = client[db][collection].find_one(key)
    if result is not None:
        return result
    raise DocumentNotFoundException


def add_document(collection, item, db=db_name):
    """Add a document to the collection"""
# Make sure that the item being added to the collection matches the schema of the collection


def init():
    """Initialize the database"""
    global client
    client = pymongo.MongoClient(conf.lookup("db"))
    

