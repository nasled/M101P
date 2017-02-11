#!/usr/bin/env python
import pymongo

connection = pymongo.MongoClient("mongodb://mongo.loc")
db = connection.blog
posts = db.posts

try:
    cursor = posts.aggregate([
        {'$unwind': '$comments'},
        {'$group': {'_id': '$comments.author', 'count': {'$sum': 1}}},
        {'$sort': {'count': pymongo.DESCENDING}},
        {'$limit': 1}
    ])

except Exception as e:
    print("Unexpected error:", type(e), e)

# Elizabet Kleine
print(list(cursor)[0]['_id'])

