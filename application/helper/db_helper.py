#from flask import Flask
#from flask.ext.pymongo import PyMongo

### https://flask-pymongo.readthedocs.io/en/latest/
### http://api.mongodb.com/python/current/tutorial.html
### https://pythonhosted.org/Flask-MongoAlchemy/ <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< cai nay hay
### http://stackoverflow.com/questions/2404742/how-to-install-mongodb-on-windows
### http://api.mongodb.com/python/current/api/index.html

#app = Flask(__name__)
#mongo = PyMongo("testcloud")

#def test():
    #mongo.db.users.find({'online': True})
    #pass

from pymongo import MongoClient
import pprint

client = MongoClient('mongodb://localhost:27017/')

db = client['testcloud']

def get_collection(collection):
    return db[collection]

user = {"email":"minhgaga@gmail.com", "password": "spms2006"}

tblUser = db.users
user_id = tblUser.insert_one(user).inserted_id
print user_id

pprint.pprint(tblUser.find_one())

pprint.pprint(tblUser.find_one({"_id": user_id}))

#collection = db.create_collection('tblProjects')
print "ok"