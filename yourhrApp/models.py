from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['yourhr_db']

def save_user(user_data):
    db.users.insert_one(user_data)
