from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Your MongoDB Atlas URI
uri = "mongodb+srv://harish:Vny6pwFrgCtWX65y@funfact.84pnzrc.mongodb.net/?retryWrites=true&w=majority"

# Connect to MongoDB Atlas with ServerApi version 1
client = MongoClient(uri, server_api=ServerApi('1'))

# Replace 'funfacts' with your actual database name
db = client['funfact']

# Replace 'funfacts' with your actual collection name
collection = db['funfact']

# Use the $sample stage to retrieve a random document
random_fun_fact = collection.aggregate([{'$sample': {'size': 1}}]).next()

# Print only the 'fun_fact' value
print(random_fun_fact['fun_fact'])
