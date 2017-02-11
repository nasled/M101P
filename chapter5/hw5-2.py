#!/usr/bin/env python
import pymongo

connection = pymongo.MongoClient("mongodb://mongo.loc")
db = connection.test
zips = db.zips

try:
    cursor = zips.aggregate([
        {'$match': {'state': {'$in': ['CA', 'NY']}}},
        {'$group': {'_id': {'city': '$city', 'state': '$state'}, 'popTotal': {'$sum': '$pop'}}},
        {'$match': {'popTotal': { '$gt': 25000}}},
        {'$group': {'_id': 'res', 'popAvg': {'$avg': '$popTotal'}}},
        {'$limit': 1}
    ])

except Exception as e:
    print("Unexpected error:", type(e), e)

# 44805
print(round(list(cursor)[0]['popAvg']))

