#!/usr/bin/env python
import pymongo

connection = pymongo.MongoClient("mongodb://mongo.loc")
db = connection.test
zips = db.zips

try:
    cursor = zips.aggregate([
        {'$project': {'first_char': {'$substr': ["$city", 0, 1]}, 'population': "$pop" }},
        {'$match': {'first_char': {'$in': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']}}},
        {'$group': {'_id': 'res', 'sumTotal': {'$sum': '$population'}}},
        {'$limit': 1}
    ])

except Exception as e:
    print("Unexpected error:", type(e), e)

# 298015
print(list(cursor)[0]['sumTotal'])

