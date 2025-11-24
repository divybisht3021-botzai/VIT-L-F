import json
import os

userfile='users.json'
itemfile='items.json'

def loadfile(filename):
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return [] 

def savefile(filename, content):
    with open(filename, 'w') as f:
        return json.dump(content, f)

def loadusers():
    return loadfile(userfile)

def saveuser(users):
    savefile(userfile, users)

def loaditems():
    return loadfile(itemfile)

def saveitem(items):
    savefile(itemfile, items)
