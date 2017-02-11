#!/usr/bin/env python

import pymongo

connection = pymongo.MongoClient("mongodb://mongo.loc")
db = connection.m101
collection = db.hw1
document = collection.find_one()

# 42
print(int(document['answer']))
