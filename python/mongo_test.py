import pymongo
from pymongo import MongoClient
import pprint
from IPython.display import clear_output

# Replace XXXX with your connection URI from the Atlas UI
client = MongoClient("mongodb+srv://samin:flower456@cluster0-myteb.mongodb.net/?retryWrites=true")

pipeline = [
    {
        '$group': {
            '_id': {"language": "$language"},
            'count': {'$sum': 1}
        }
    }
]

clear_output()
pprint.pprint(list(client.newdb.new_collection.aggregate(pipeline)))
