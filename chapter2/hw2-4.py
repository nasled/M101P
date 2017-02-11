#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://mongo.loc")

# get a handle to the school database
db = connection.video
movieDetails = db.movieDetails


query = {
    "rated": "PG-13",
    "year": 2013,
    "awards.wins": 0
}

try:
    doc = movieDetails.find_one(query)

except Exception as e:
    print("Unexpected error:", type(e), e)

# A Decade of Decadence, Pt. 2: Legacy of Dreams
print(doc['title'])

