import sqlite3
from flask import g 
from application.cc import filemanager

DATABASE = 'db/data.db'
db = None

# database setup
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    conn = sqlite3.connect(DATABASE)
    schema = filemanager.get_file_content('db/schema.sql')
    conn.execute(schema)
    conn.close()
    conn
    
def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn

def close_db():
    if db is not None:
        db.close()
        
def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

# database reset
