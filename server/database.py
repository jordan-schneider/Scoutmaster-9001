#!/usr/bin/python3
import pymongo
import conf

# Mongo client
client = None


class DatabaseNotFoundException(Exception):
    pass


class CollectionNotFoundException(Exception):
    pass


class DocumentNotFoundException(Exception):
    pass


class InvalidUpsertFieldException(Exception):
    pass


def get_database(name):
    """Get a database from mongodb"""
    if name in client.database_names():
        return client[name]
    raise DatabaseNotFoundException


def add_database(name):
    """Add a database to mongodb"""
    return client[name]


def get_collection(db, name):
    """Get a table from the database"""
    if name in client[db].collection_names():
        return client[db][name]
    raise CollectionNotFoundException


def add_collection(db, name):
    """Add a new table to the database"""
    return client[db][name]


def get_document(db, collection, key={}):
    """Get a document from the collection"""
    result = [posts for posts in client[db][collection].find(key)]
    if result != []:
        return result
    raise DocumentNotFoundException


# Make sure that the item being added to the collection matches the schema of the collection
def add_document(db, collection, upsert_field, item):
    """Add a document to the collection"""
    target = client[db][collection]
    posts = target.posts

    try:

        # Make sure to upsert based on a field that will be maintained in both document version
        upsert_key = {upsert_field : item[upsert_field]}
        return posts.update(upsert_key, item, upsert=True)

    except KeyError:

        # If there is a keyerror when trying to create the upsert field
        raise InvalidUpsertFieldException


def init():
    """Initialize the database"""
    global client
    client = pymongo.MongoClient(conf.lookup("db"))
    

