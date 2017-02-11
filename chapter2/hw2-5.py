#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://mongo.loc")

# get a handle to the school database
db = connection.video
movieDetails = db.movieDetails


query = {
}

try:
    doc = movieDetails.find(query)

except Exception as e:
    print("Unexpected error:", type(e), e)

# 6
print(doc.count())

