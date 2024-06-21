import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient

# Load environment variables from .env file
load_dotenv()

# Get database configuration from environment variables
DB_PATH = os.getenv("DB_PATH")
DB_NAME = os.getenv("DB_NAME")
USERS_COLLECTION = os.getenv("USERS_COLLECTION")
LINKING_IDS_COLLECTION = os.getenv("LINKING_IDS_COLLECTION")

# Connect to MongoDB
client = MongoClient(DB_PATH)
db = client[DB_NAME]

# Access collections in the database
users_collection = db[USERS_COLLECTION]
linking_ids_collection = db[LINKING_IDS_COLLECTION]
