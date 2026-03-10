from pymongo import MongoClient

MONGO_URL = "mongodb://localhost:27017"

client = MongoClient(MONGO_URL)

db = client["ticket_system"]

users_collection = db["users"]
tickets_collection = db["tickets"]