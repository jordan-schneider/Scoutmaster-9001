import json

conf = json.loads(open("scoutmaster.conf", "r").read())


def lookup(key, default=None):
    """Returns constants from conf.json in python dict format"""
    try:
        return conf[key]
    except KeyError:
        if default is not None:
            return default
        raise

