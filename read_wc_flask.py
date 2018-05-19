from flask import Flask
from pymongo import MongoClient
import json
import pymongo

app = Flask(__name__)

client = MongoClient()
db = client['hashtags']
coll = db['tags']

@app.route("/")
def serve_mongo_data():
    results = []
    for i in coll.find().limit(100).sort("_2", pymongo.DESCENDING):
        results.append(i)
    return str({"results":results})



if __name__ == "__main__":
    app.run()