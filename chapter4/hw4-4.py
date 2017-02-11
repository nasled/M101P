#!/usr/bin/env python
import pymongo

connection = pymongo.MongoClient("mongodb://mongo.loc")
db = connection.m101
sysprofile = db.sysprofile

try:
    doc = sysprofile.find({ "ns": "school2.students" }).sort('millis', pymongo.DESCENDING).limit(1)

except Exception as e:
    print("Unexpected error:", type(e), e)

# 15820
print(doc[0]['millis'])