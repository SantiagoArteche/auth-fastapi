from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

db_client = MongoClient(f"{os.getenv('MONGO_URL')}")
db = db_client["userfapi"]