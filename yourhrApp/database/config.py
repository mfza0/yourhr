from pymongo import MongoClient

def get_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['yourhr_db']
    return db

db = get_db()
