#!/usr/bin/env python
import pymongo

connection = pymongo.MongoClient("mongodb://mongo.loc")
collection = connection.enron.messages

try:
    doc = collection.find({'headers.From': 'andrew.fastow@enron.com',
                           '$and': [{'headers.To': {'$in': ['jeff.skilling@enron.com']}}]}).count()


except Exception as e:
    print("Unexpected error:", type(e), e)

# 3
print(doc)
