#!/usr/bin/env python
import pymongo

connection = pymongo.MongoClient("mongodb://mongo.loc")
db = connection.test
grades = db.grades

try:
    cursor = grades.aggregate([
        {'$unwind': '$scores'},
        {'$match': {'scores.type': {'$in': ['exam', 'homework']}}},
        {'$group': {'_id': {'student_id': '$student_id', 'class_id': '$class_id'},
                    'studentScoreAvg': {'$avg': '$scores.score'}}},
        {'$group': {'_id': '$_id.class_id', 'scoreAvg': {'$avg': '$studentScoreAvg'}}},
        {'$sort': {'scoreAvg': pymongo.DESCENDING}},
        {'$limit': 1}
    ])

except Exception as e:
    print("Unexpected error:", type(e), e)

# 1
print(list(cursor)[0]['_id'])

