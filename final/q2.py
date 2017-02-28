#!/usr/bin/env python
import pymongo

connection = pymongo.MongoClient("mongodb://mongo.loc")
collection = connection.enron.messages

try:
    doc = collection.aggregate([
        {'$unwind': "$headers.To"},
        {'$group': {'_id': "$_id", 'from': { '$first': "$headers.From"}, 'to': { '$addToSet': "$headers.To"}}},
        {'$unwind': "$to"},
        {'$group': {'_id': {'from':'$from','to':'$to'}, 'total': {'$sum': 1}}},
        {'$sort': {'total': -1}},
        {'$limit': 1}
    ])
    res = list(doc)[0]

except Exception as e:
    print("Unexpected error:", type(e), e)

# susan.mara@enron.com to jeff.dasovich@enron.com
print(res['_id']['from'], 'to', res['_id']['to'])
